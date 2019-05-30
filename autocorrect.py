import minEditDist as med
import pandas as pd
from collections import defaultdict
import numpy as np

def main():
	ACCURACY = 0.95
	personal words = list()

	sentence = "Hellof how are you doin"
	#print(process(sentence, df, ACCURACY))

	word = "only"
	df = pd.read_csv("~/english-words/words.txt", sep='\n')
	possibles = getCandidateWords(word, df)

	print(possibles)

def process(sentence: str, df):

	#work on this after college
	if len(sentence.split()) < 3:
		return sentence


	output = str()
	potential = sentence[:2]
	for word in sentence[2:]:
		possibles = getCandidateWords(word, df, upper_bound=3)

	return output



def makeADecision(word):
	pass

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

def performBayes(ngram: str):
	pass

def weighAdjKeys(w: str):
	pass


#run script
if __name__ == '__main__':
	main()

