import minEditDist as med
import pandas as pd
from collections import defaultdict
import numpy as np

def main():
	ACCURACY = 0.95

	sentence = "Hellof how are you doin"
	#print(process(sentence, df, ACCURACY))

	word = "he"

	#datasets
	personal_words = list()
	trigrams = pd.read_csv("~/w3_.txt", encoding="ISO-8859-1", sep='\t', names=["count", "first", "second", "third"])

	#print(trigrams.shape)

	allwords = pd.read_csv("~/english-words/words.txt", sep='\n')
	possibles = getCandidateWords(word, allwords)
	total_size_L = calcTotalSize(possibles)

	


	print(probabilites_med)

	#print(possibles)

def process(sentence: str, allwords, trigrams):

	#work on this after college
	if len(sentence.split()) < 3:
		return sentence


	output = str()
	potential = sentence[:2]
	probabilites_med = defaultdict(list)
	for word in sentence[2:]:


		possibles = getCandidateWords(word, allwords, upper_bound=3)
		total_size_L = calcTotalSize(possibles)
		#now the keys are probability of each word appearing
		for key in possibles:
			probabilites_med[np.log(1/key) - total_size_L] = possibles[key]

		prob_ngram = performBayes()


	return output



def makeADecision(word):
	pass

def getProbOfMED(key, total_size_L):
	return np.log(1/key) - total_size_L

def calcTotalSize(possibles):
	total = 0
	for key in possibles:
		total += len(possibles[key])/key

	return np.log(total)



def getCandidateWords(word, df, upper_bound=4):
	#df_candidates = df.apply(calcMinEditDist, args = (word,))

	possibles = defaultdict(list)

	for row in df.itertuples():
		poss_w = str(row[1])
		dist = calcMinEditDist(word, poss_w)

		if dist != -1 and dist != 0 and dist <= upper_bound:
			possibles[dist].append(poss_w)

	return possibles




def calcMinEditDist(w: str, c: str):
	if 0.5 <= len(w)/len(c) <= 2:
		return med.MED(w, c)
	else:
		#too short/long
		return -1

def performBayes(ngram: str):
	
	return np.log(1)

def weighAdjKeys(w: str):
	pass


#run script
if __name__ == '__main__':
	main()

