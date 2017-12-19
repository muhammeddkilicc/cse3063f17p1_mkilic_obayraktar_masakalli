#!/usr/bin/env python3
#20-12-2017 02:34:47 

import os
import sys
import re
import time
import PyPDF2
import string
import operator
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def getPageCount(pdf_file):

	pdfFileObj = open(pdf_file, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	pages = pdfReader.numPages
	return pages

def extractData(pdf_file, page):

	pdfFileObj = open(pdf_file, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	pageObj = pdfReader.getPage(page)
	data = pageObj.extractText()
	return data

def getWordCount(data):

	data=data.split()
	return len(data)

# color function
def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = int(360.0 * float(random_state.randint(60, 250)) / 255.0)
    s = int(100.0 * float(random_state.randint(60, 250)) / 255.0)
    l = int(100.0 * float(random_state.randint(60, 250)) / 255.0)
    return "hsl({}, {}%, {}%)".format(h, s, l)

def main():
	if len(sys.argv)!=2:
		print('command usage: python word_count.py FileName')
		exit(1)
	else:
		pdfFile = sys.argv[1]
	
		# check if the specified file exists or not
		try:
			if os.path.exists(pdfFile):
				print("file found!")
		except OSError as err:
			print(err.reason)
			exit(1)


		# get the word count in the pdf file
		totalWords = 0
		numPages = getPageCount(pdfFile)
		print("num of pages ",numPages)
		for i in range(numPages):
			wordstring = extractData(pdfFile, i)
			
			# Generate text to count
			frequency = {}
			#document_text = open('test.txt', 'r')
			#wordstring = document_text.read().lower()
			wordlist = re.findall(r'\b[a-z]{3,15}\b', wordstring)
			#wordlist= re.sub(r'\W+', ' ', wordlist)

			wordfreq = [wordlist.count(w) for w in wordlist]

			"""
			print("String\n" + wordstring +"\n")
			print("List\n" + str(wordlist) + "\n")
			print("Frequencies\n" + str(wordfreq) + "\n")
			print("Pairs\n" + str(zip(wordlist, wordfreq)))
			"""
			wordlist.sort()
			wordlist.reverse()
			wordfreq.sort()
			wordfreq.reverse()

			kelimeSayisi=0

			for a in wordlist:
				kelimeSayisi = kelimeSayisi+1
				if (kelimeSayisi <50):
						print((kelimeSayisi+1),a, sep=" : ")



			#print("String\n" + wordstring +"\n")
			print("List\n" + str(wordlist) + "\n")
			print("Frequencies\n" + str(wordfreq) + "\n")
			print("Pairs\n" + str(zip(wordlist, wordfreq)))
			print(type(wordstring))
			print(type(str(wordlist)))
			print(type(wordfreq))
			print(type(str(wordfreq)))
			print(type(str(zip(wordlist, wordfreq))))
			print(type(zip(wordlist, wordfreq)))
			time.sleep(1)
			




# Display the generated image:
# the matplotlib way:

#plt.imshow(wordcloud, interpolation='bilinear')
#plt.axis("off")

# lower max_font_size
			wordcloud = WordCloud(background_color = 'white',width = 1200,height = 1000,color_func = random_color_func).generate(wordstring)
			plt.figure()
			plt.imshow(wordcloud, interpolation="bilinear")
			plt.axis("off")
			plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()
	


if __name__ == '__main__':
	main()
