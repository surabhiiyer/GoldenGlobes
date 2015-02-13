import json
import nltk
import re
from nltk.util import ngrams
import urllib
import HTMLParser

#for debugging purposes only, to be removed
from pprint import pprint
import pdb

# Method to parse the JSON file
# Input: path to json file
# Returns: the parsed data in an array 
def jsonParser(path):
    json_data = open(path)
    data = json.load(json_data)
    numOfTweets = len(data)
    tweets = []
    for tweetIndex in range (0,numOfTweets):
        tweets.append(data[tweetIndex]["text"])
    json_data.close()
    return tweets
#function jsonParser end

# to be used to tokenize words in a sentence
from nltk.tokenize import TreebankWordTokenizer
wordTokenizer = TreebankWordTokenizer() 

# to be used to tokenize sentences in a tweet
sentenceTokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

from nltk.corpus import stopwords
stop = stopwords.words('english')

# reg ex for filtering the tweets.
filterRegExPatterns = ['host?[s]', 'hosting', 'hosted', 'won best', 'winner', 'wins', 'presented', 'presenting'] 
filterRegExPatternJoin = "|".join(filterRegExPatterns)
filterRegEx = re.compile(filterRegExPatternJoin, re.IGNORECASE)

filterRetweetRegEx = re.compile('^RT', re.IGNORECASE)

# Method to filter the tweets, removing tweets that do not make sense
# Input: unfiltered tweets
# Output: filtered tweets 
def filterTweets(tweets):
    filteredTweets = []
    count = 0
    for tweet in tweets:
        if(filterRegEx.search(tweet) and not filterRetweetRegEx.search(tweet)):
            count += 1
            tweetCleaned = re.sub(r'[^a-zA-Z0-9 ]',r'',tweet)
            filteredTweets.append(tweetCleaned)
    pprint(count)            
    return filteredTweets
#function filterTweets end

# a list of tokens to be removed from the tweets/sentences under analysis
blacklistWords = ['golden', 'globes', 'goldenglobes', '#goldenglobes', '#golden']
#list of hosts
hosts = []
# list to store all the winners by category
winners = []
specialAwardWinners = []

#reg ex pattern for filtering tweets with information about the host(s)
hostRegExPatterns = ['host?[s]', 'hosting', 'hosted']
hostRegExPatternJoint = '|'.join(hostRegExPatterns)
hostRegEx = re.compile(hostRegExPatternJoint, re.IGNORECASE)
# a list to store the host name. TODO: to be replaced by some meaningful structure
hostName = dict()

def addToDictionary(key, dictionaryObject):
    if key in dictionaryObject:
        dictionaryObject[key] += 1
    else:
        dictionaryObject[key] = 1    

def findMaxInDictionary(dictionaryObject, resultList):
    max = 0
    for key in dictionaryObject:
        if max < dictionaryObject[key]:
            max = dictionaryObject[key]
    for key in dictionaryObject:
        if max == dictionaryObject[key]:
            resultList.append(key)        


def findHost(tweets):
    name = ''
    tweetsScanned = 0
    for tweet in tweets:
        if hostRegEx.search(tweet):
            tweetsScanned += 1
            filterText = ' '.join(word for word in tweet.split() if word.lower() not in stop and word.lower() not in blacklistWords)
            unigram = wordTokenizer.tokenize(filterText)
            for bigram in nltk.bigrams(unigram):
                noun = 0
                posTag = nltk.pos_tag(bigram)
                for(data, tag) in posTag:
                    if tag == 'NNP':
                        noun += 1
                if noun == 2:
                    name = "%s %s" % bigram
                    addToDictionary(name, hostName)
        if tweetsScanned > 10:
            break                    
    findMaxInDictionary(hostName, hosts)

import WinnersData
winnerRegEx = WinnersData.winnerRegEx
nomineesByCategory = WinnersData.nomineesByCategory
categories = WinnersData.categories 

def findWinners(tweets):
    winnerngramList = dict()
    for categoryIndex in range(0, len(winnerRegEx)):
        for index in range(0, len(tweets)):
            result = winnerRegEx[categoryIndex].search(tweets[index])
            if result:
                sentence = sentenceTokenizer.tokenize(tweets[index])    
                for sentenceIndex in range(0, len(sentence)):
                    text = ' '.join(word for word in sentence[sentenceIndex].split() if word not in stop and word not in blacklistWords)
                    tokens = wordTokenizer.tokenize(text)
                    for unigram in tokens:
                        for nominee in nomineesByCategory[categoryIndex]:
                            tokenNominee = wordTokenizer.tokenize(nominee) 
                            if unigram in tokenNominee:
                                if nominee in winnerngramList:
                                    winnerngramList[nominee] +=1
                                else:
                                    winnerngramList[nominee] = 1 
        max = 0        
        for key in winnerngramList:
            if(winnerngramList[key] > max):
                max = winnerngramList[key]
        if max == 0:
            winners.append("Data not found")        
        for key in winnerngramList:
            if(winnerngramList[key] == max):
                winners.append(key)   
        winnerngramList.clear()    


specialAwards = WinnersData.specialAwards
specialAwardsRegEx = WinnersData.specialAwardsRegEx

specialAwardWinner = dict()

def findWinnersSpecialAward(tweets):
    for index in range(0, len(specialAwards)):
        specialAwardStopWords = wordTokenizer.tokenize(specialAwards[index])
        for tweet in tweets:
            if specialAwardsRegEx[index].search(tweet):
                filteredSentences = ' '.join(word for word in tweet.split() if word.lower() not in stop and word.lower() not in blacklistWords 
                    and word not in specialAwardStopWords)
                unigrams = wordTokenizer.tokenize(filteredSentences)
                for bigram in nltk.bigrams(unigrams):
                    posTags = nltk.pos_tag(bigram)
                    noun = 0
                    for (data, tag) in posTags:
                        if tag == 'NNP':
                            noun += 1
                    if noun == 2:
                        name = "%s %s" % bigram
                        addToDictionary(name, specialAwardWinner)                   
        findMaxInDictionary(specialAwardWinner, specialAwardWinners)
        specialAwardWinner.clear()
                                      

def printResults():
    print('Hosted by:')
    for name in hosts:
        print(name)
    print('Winners by category')
    for index in range(0, len(categories)):
        print(categories[index], winners[index])
    for key in range(0, len(specialAwards)):
        print(specialAwards[index], specialAwardWinners[index])                                          





            


         
            




