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

# reg ex for filtering the tweets.
filterRegExPatterns = ['hosting', 'won best', 'winner'] 
filterRegExPatternJoin = "|".join(filterRegExPatterns)
filterRegEx = re.compile(filterRegExPatternJoin, re.IGNORECASE)

filterRetweetRegEx = re.compile('^RT', re.IGNORECASE)

# Method to filter the tweets, removing tweets that do not make sense
# Input: unfiltered tweets
# Output: filtered tweets 
def filterTweets(tweets):
    filteredTweets = []
    count = 0
    #file = open("newfile.txt", "w")
    for index in range(0, len(tweets)):
        sentence = sentenceTokenizer.tokenize(tweets[index])
        if not(filterRetweetRegEx.search(sentence[0])):
            for sentenceIndex in range (0, len(sentence)):
                # filter the sentences based on the reg ex defined above
                result = filterRegEx.search(sentence[sentenceIndex])
                if result:
                    # if tweet is meaningful, push into the list of filtered tweets
                    # first remove any speacial characters
                    tweetCleaned = re.sub(r'[^a-zA-Z0-9 ]',r'',tweets[index])
                    filteredTweets.append(tweetCleaned)
                    #file.write(tweetCleaned)
                    #file.write("\n")
                    count += 1
                    break
    pprint(count)            
    return filteredTweets
#function filterTweets end

# a list of tokens to be removed from the tweets/sentences under analysis
blacklistWords = ['Golden', 'Globes', 'GOLDEN', 'GLOBES']

#reg ex pattern for filtering tweets with information about the host(s)
hostRegEx = re.compile('hosting', re.IGNORECASE)
# a list to store the host name. TODO: to be replaced by some meaningful structure
hostName = []

# Method to find the host name from all the tweets
# INPUT: tweets in array/list format
# OUPUT: none
def findHost(tweet):
    # dictionary object to store the bigrams
    bigramsList = dict()
    # variable to check the number of sentences that satisfy the regex for extracting host name
    sentenceCount = 0;
    for index in range (0, len(tweet)):
        # extract all the sentences in a tweet
        sentence = sentenceTokenizer.tokenize(tweet[index])
        for sentenceIndex in range (0, len(sentence)):
            # filter the sentences based on the reg ex for host
            result = hostRegEx.search(sentence[sentenceIndex])
            if result:
                # remove all the special characters from the sentence
                token = re.sub(r'[^a-zA-Z0-9 ]',r'',sentence[sentenceIndex])
                tokens = wordTokenizer.tokenize(token)
                # calculate the frequency of bigrams
                for key in nltk.bigrams(tokens):
                    if key in bigramsList:
                        bigramsList[key] += 1
                    else:
                        bigramsList[key] = 1    
                sentenceCount += 1
            # if we have 10 sentences that give information about the hosts, stop this process    
            if sentenceCount > 10:
                break
        if sentenceCount > 10:
                break   
    # List that stores bigrams pairs that are Proper Nouns
    bigramProperNouns = dict()     
    
    for key in bigramsList:
        nounTags = 0
        posTags = nltk.pos_tag(key)
        for (data,tag) in posTags:
            if data not in blacklistWords:
                if(tag == 'NNP'):
                    nounTags += 1
        if nounTags ==2:
            bigramProperNouns[key] = bigramsList[key]

    max = 0        
    for key in bigramProperNouns:
        if(bigramProperNouns[key] > max):
            max = bigramProperNouns[key]

    for key in bigramProperNouns:
        if(bigramProperNouns[key] == max):
            hostName.append(key)
    pprint(hostName)        
# function findHost end


from nltk.corpus import stopwords
stop = stopwords.words('english')

# list to store all the winners by category
winners = []

import WinnersData
winnerRegEx = WinnersData.winnerRegEx
nomineesByCategory = WinnersData.nomineesByCategory 

def findWinners(tweets):
    #file = open("newfile.txt", "w")
    winnerBigramList = dict()
    for categoryIndex in range(0, len(winnerRegEx)):
        for index in range(0, len(tweets)):
            winnerFoundFlag = 0
            result = winnerRegEx[categoryIndex].search(tweets[index])
            if result:
                sentence = sentenceTokenizer.tokenize(tweets[index])
                for sentenceIndex in range(0, len(sentence)):
                    text = ' '.join(word for word in sentence[sentenceIndex].split() if word not in stop and word not in blacklistWords)
                    tokens = wordTokenizer.tokenize(text)
                    for key in nltk.bigrams(tokens):
                        winner = "%s %s" % key               
                        if winner in nomineesByCategory[categoryIndex]:
                            winners.append(winner)
                            winnerFoundFlag = 1
                            break
                    if winnerFoundFlag == 1:
                        break
                    for key in nltk.trigrams(tokens):
                        winner = "%s %s %s" % key 
                        if winner in nomineesByCategory[categoryIndex]:
                            winners.append(winner)
                            winnerFoundFlag = 1
                            break
                    if winnerFoundFlag == 1:
                        break
                    for unigram in tokens:
                        if unigram in nomineesByCategory[categoryIndex]:
                            winners.append(unigram)
                            winnerFoundFlag = 1 
                            break          
            if winnerFoundFlag == 1:
                break
    pprint(winners)                            




            


         
            




