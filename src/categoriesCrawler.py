import urllib2
import re
from bs4 import BeautifulSoup

# to be used to tokenize words in a sentence
from nltk.tokenize import TreebankWordTokenizer
wordTokenizer = TreebankWordTokenizer()

categoryRegEx = re.compile('^Best', re.IGNORECASE)

categories = []
specialCategories = []

specialCategoryRegEx = re.compile('^golden globe', re.IGNORECASE)

def specialCategory(url):
	html_page = urllib2.urlopen(url)
 	soup = BeautifulSoup(html_page)
	for header in soup.find_all('h1'):
		headerText = header.text
		if specialCategoryRegEx.search(headerText):
			continue
		else:
			specialCategories.append(headerText)	


def scrapeCategories(url):
	html_page = urllib2.urlopen(url)
 	soup = BeautifulSoup(html_page)
	for header in soup.find_all('h2'):
		headerText = header.text
		if categoryRegEx.search(headerText):
			categories.append(headerText)
	specialCategory(url)		