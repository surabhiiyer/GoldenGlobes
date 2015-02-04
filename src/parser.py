import json
from nltk.corpus import stopwords
from pprint import pprint

def jsonparser(path):
    json_data = open(path)
    data = json.load(json_data)
    numOfTweets = len(data)
    tweets = []
    for tweetIndex in range (0,numOfTweets):
        tweets.append(data[tweetIndex]["text"])
    json_data.close()
    return tweets

tweets = jsonparser("/Users/Harsh/Desktop/Winter 2015/EECS 337 NLP/Project1/gg2013.json")

import nltk.data
sentenceTokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sentences = sentenceTokenizer.tokenize(tweets[0])

listOfWords = ["won", "winner"];

# import nltk.tokenize import TreebankWordTokenizer
# wordTokenizer = TreebankWordTokenizer()

#for sentenceIndex in range (0, len(sentences)):
#	tokens = wordTokenizer.tokenize(sentences[sentenceIndex])
#	for tokenIndex in range (0, len(tokens)):

tokens = nltk.word_tokenize(tweets[2])
stop = stopwords.words('english')
for index in range (len(tokens)):
	if tokens[index] not in stop:
		pprint(tokens[index])
