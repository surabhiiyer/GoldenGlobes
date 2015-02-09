import json
import nltk.data
import functionDefinitions
parseJson = functionDefinitions.jsonParser

from nltk.corpus import stopwords
from pprint import pprint

if __name__ == "__main__":
    # change the path mentioned below when testing
    tweets = parseJson("gg2013.json")
    #for index in range (0, len(tweets)):
        # processTweets id defined in the file functionDefinitions.py
        #functionDefinitions.findHost(tweets[index])
    filteredTweets = functionDefinitions.filterTweets(tweets)
    functionDefinitions.findWinners(filteredTweets)
    #functionDefinitions.webCrawler("url")
