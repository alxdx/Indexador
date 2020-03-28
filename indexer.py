import os
import nltk
import pandas as pd
from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('spanish'))
stop_words.add("i")
stop_words.add("ii")
stop_words.add("iii")
stop_words.add("iv")

def getCSVs():
	data=[]
	for root,directories,files in os.walk('filesCSV/'):
		for f in files:
			data.append(f)
	return data

if __name__ == '__main__':
	files=getCSVs()
	print(files)
