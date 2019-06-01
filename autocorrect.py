import minEditDist as med
import pandas as pd
from collections import defaultdict
import numpy as np
import time

def main():
	t0 = time.time()
	sentence = "This class is thouhght prrovoking and chalengin"
	#word = "sotoe"

	#datasets
	personal_words = list()
	trigrams = pd.read_csv("~/w3_.txt", encoding="ISO-8859-1", sep='\t', names=["count", "first", "second", "third"])
	allwords = pd.read_csv("~/english-words/google-10000-english-usa.txt", sep='\n')
	#words.txt
	print("built dataframes")
	#print(getCandidateWords(word, allwords))
	#print(calcMinEditDist('anyone', 'anipene'))

	print(process(sentence, allwords, trigrams))
	t1 = time.time()
	print('time elapsed: ', t1 - t0)

def process(sentence, allwords, trigrams, accuracy=0.95):

	#work on this after college
	if len(sentence.split()) < 3:
		return sentence
	

	#make array of words
	sentence = sentence.split()
	length = len(sentence)
	potential = sentence[:2]
	#punctuation = dict()
	#signs = ',.:;'

	#loop thru sentence (starting at second word)
	for index in range(2, length):
		probabilities_med = defaultdict(list)
		word = sentence[index]
		print("word #", index + 2, ":", word)
		#word, p = format(word)

		#if p:
			#punctuation[index] = p

		possibles = getCandidateWords(word, allwords, upper_bound=3)

		print("got candidates")
		print(possibles)
		total_size_L = calcTotalSize(possibles) #this is a log 
		#now the keys are probability of each word appearing
		for key in possibles:
			if key != 0: 
				probabilities_med[np.log(1/key) - total_size_L] = possibles[key]

		
		#2-gram
		prev_two = (sentence[index - 2], sentence[index-1])
		guess = ''
		allGuesses = defaultdict(list)
		prevProb = float('-inf')

		#log of prob of the typed word
		if 0 in possibles.keys():
			#print("start calculating for the typed word")
			prior_of_typed = calcPrior(word, prev_two, trigrams)
			prevProb = np.log(accuracy) + prior_of_typed
			guess = word
			allGuesses[prevProb] = word
			#print("end calculating for the typed word")

		#pick the most likely word of the candidates
		for likelihood in probabilities_med:
			for candidate in probabilities_med[likelihood]:
				#print("start calc prob of candidate: ", candidate)
				prior = calcPrior(candidate, prev_two, trigrams)
				prob = likelihood + prior
				allGuesses[prob] = candidate #saving 
				#print("end calc")


				#decide
				if prob > prevProb:
					guess = candidate
					prevProb = prob

		#finish off and reset
		potential.append(guess)
		prevProb = float('-inf')
		print(allGuesses)

	return output(potential)


def calcPrior(word, prev_two, trigrams):
	#use counting
	#new dataframe
	df = trigrams[(trigrams['first'] == prev_two[0]) & (trigrams['second'] == prev_two[1])]
	#all 3-gram, starting w the first two words
	prev_two_count = int(df.sum(numeric_only=True))
	#count of our specific 3-gram
	three_gram_count = int(df[df['third'] == word].sum(numeric_only=True))
	
	#return log of the probability
	if three_gram_count != 0:
		return np.log(three_gram_count / prev_two_count)
	else:
		return np.log(0.0001)

#def getProbOfMED(key, total_size_L):
	#return np.log(1/key) - total_size_L

def calcTotalSize(possibles):
	total = 0
	for key in possibles:
		if key != 0:
			total += len(possibles[key])/key

	return np.log(total)



def getCandidateWords(word, df, upper_bound=4):
	#df_candidates = df.apply(calcMinEditDist, args = (word,))

	possibles = defaultdict(list)

	for row in df.itertuples():
		poss_w = str(row[1])
		dist = calcMinEditDist(word, poss_w)

		if dist != -1 and dist <= upper_bound:
			possibles[dist].append(poss_w)

	return possibles



def calcMinEditDist(w: str, c: str):
	if 0.5 <= len(w)/len(c) <= 2:
		return med.MED(w, c)
	else:
		#too short/long
		return -1

def weighAdjKeys(w: str):
	pass

#def formatWord(word):


def output(l):
	s = ''
	#keys = punctuation.keys()
	for word in l:
		s += word
		s += ' '
	return s


#run script
if __name__ == '__main__':
	main()

