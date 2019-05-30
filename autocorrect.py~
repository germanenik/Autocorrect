import minEditDist as med
import pandas as pd
from collections import defaultdict

def main():

	sentence = "Hellof how are you doin"
	#print(process(sentence))

	word = "thrgout"
	corpus = "corpus of english text"
	df = pd.read_csv("~/english-words/words.txt", sep='\n')
	possibles = getCandidateWords(word, df)

	print(possibles)

def process(sentence: str, df):
	output = str()
	for word in sentence:
		getCandidateWords(word, df)
	return output



def makeADecision(word):
	pass

def getCandidateWords(word: str, df):
	#df_candidates = df.apply(calcMinEditDist, args = (word,))

	possibles = defaultdict(list)

	for row in df.itertuples():
		poss_w = str(row[1])
		dist = calcMinEditDist(word, poss_w)

		if dist != -1 and dist <= 4:
			possibles[dist].append(poss_w)

	return possibles

#idea -- cut off the calculation once we know it's a no go
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

