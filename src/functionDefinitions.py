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
filterRegExPatterns = ['hosting', 'won best', 'winner', 'wins', 'presented', 'presenting'] 
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
            host = "%s %s" % key
            hostName.append(host)        
# function findHost end



from nltk.corpus import stopwords
stop = stopwords.words('english')

# list to store all the winners by category
winners = []

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

specialAwardWinners = []

specialAwards = WinnersData.specialAwards
specialAwardsRegEx = WinnersData.specialAwardsRegEx

def findSpecialAwards(tweets):
    winnerList = dict()
    for specialAwardIndex in range(0, len(specialAwards)):
        for index in range(0, len(tweets)):
            result = specialAwardsRegEx[specialAwardIndex].search(tweets[index])
            if result:
                sentence = sentenceTokenizer.tokenize(tweets[index])    
                for sentenceIndex in range(0, len(sentence)):
                    text = ' '.join(word for word in sentence[sentenceIndex].split() if word.lower() not in stop and word not in blacklistWords)
                    tokens = wordTokenizer.tokenize(text)
                    posTags = nltk.pos_tag(tokens)
                    for (data,tag) in posTags:
                        if(tag == 'NNP'):
                            if data in winnerList:
                                winnerList[data] +=1
                            else:
                                winnerList[data] = 1 
        max = 0 
        pdb.set_trace()       
        for key in winnerList:
            if(winnerList[key] > max):
                max = winnerList[key]
        if max == 0:
            specialAwardWinners.append("Data not found")        
        for key in winnerList:
            if(winnerList[key] == max):
                specialAwardWinners.append(key)   
        winnerList.clear()                        

presentersPatternList = ['presented', 'presenter', 'presenting', 'gave away']
presentersPattern = '|'.join(presentersPatternList)
presentersPatternRegEx = re.compile(presentersPattern, re.IGNORECASE)
                    


def printResults():
    print('Hosted by:')
    for name in hostName:
        print(name)
    print('Winners by category')
    for index in range(0, len(categories)):
        print(categories[index], winners[index])
    # for index in range(0, len(specialAwards)):
    #     print(specialAwards[index], specialAwardWinners[index])                                          





            


         
            




