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
    #file = open("presenters.txt", "w")
    filteredTweets = []
    count = 0
    for tweet in tweets:
        if(filterRegEx.search(tweet) and not filterRetweetRegEx.search(tweet)):
            count += 1
            tweetCleaned = re.sub(r'[^a-zA-Z0-9 ]',r'',tweet)
            #file.write(tweetCleaned)
            #file.write("\n")
            filteredTweets.append(tweetCleaned)
    #pprint(count)            
    return filteredTweets
#function filterTweets end

# a list of tokens to be removed from the tweets/sentences under analysis
blacklistWords = ['golden', 'globes', 'goldenglobes', '#goldenglobes', '#golden']

# list to store all the winners by category
presenters = []

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
    #list of hosts
    hosts = []
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
    return hosts


import WinnersData
winnerRegEx = WinnersData.winnerRegEx
nomineesByCategory = WinnersData.nomineesByCategory
categories = WinnersData.categories

def findWinners(tweets, nominees_categorized):
    winners = []
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
                        for nominee in nominees_categorized[categoryIndex]:
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
    return winners      


specialAwards = WinnersData.specialCategories
specialAwardsRegEx = WinnersData.specialAwardsRegExReordered

specialAwardWinner = dict()

def findWinnersSpecialAward(tweets):
    specialAwardWinners = []
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
    return specialAwardWinners    


presentersRegexPatternList = ['[A-Z][a-z]+ [A-Z][a-z]+ presented', '[A-Z][a-z]+ [A-Z][a-z]+ presenting']
presentersRegexPattern = "|".join(presentersRegexPatternList)
presentersRegEx = re.compile(presentersRegexPattern)
#properNountRegEx = re.compile('[A-Z][a-z]+ [A-Z][a-z]+ presented')

unigramRegExPatternList = ['[A-Z][a-z]+', 'and', 'amp']
unigramRegExPattern = '|'.join(unigramRegExPatternList)
unigramRegEx = re.compile('[A-Z][a-z]+')


def manipulateDictionary(dictionary):
    for key in dictionary:
        token = wordTokenizer.tokenize(key)
        if dictionary[key] > 1:
            presenters.append(key)       
        elif len(token) ==2:
            presenters.append(key) 

best = ["best"]
presentersAward = dict()

def linkPresenters(tweets):
     found = 0
     for presenter in presenters:
        for tweet in tweets:
            if presentersRegEx.search(tweet):
                if presenter in tweet:
                    for regexIndex in range(0, len(winnerRegEx)):
                        if winnerRegEx[regexIndex].search(tweet):
                            presentersAward[presenter] = categories[regexIndex]
                    for regexIndex in range(0, len(specialAwardsRegEx)):
                        if specialAwardsRegEx[regexIndex].search(tweet):
                            presentersAward[presenter] = specialAwards[regexIndex]            


def findPresenters(tweets):
    file = open("presenters.txt", "w")
    presentersList = dict()
    for tweet in tweets:
        if presentersRegEx.search(tweet):
            Tweet = re.sub(r'and',r'conjunction', tweet)
            subTweet = re.sub(r'amp',r'conjunction', Tweet)
            filteredSentences = ' '.join(word for word in subTweet.split() if word.lower() not in stop and word.lower() not in blacklistWords)
            file.write(filteredSentences)
            file.write("\n")
            unigrams = wordTokenizer.tokenize(filteredSentences)
            name = ''
            for unigram in unigrams:
                if unigram == "presented" or unigram == "presenting":
                    if name != '':
                        if name in presentersList:
                            presentersList[name] += 1
                        else:
                            presentersList[name] = 1 
                    break
                elif  unigramRegEx.search(unigram):
                    name += unigram
                    name += ' '
                elif unigram == "conjunction":
                    if name in presentersList:
                        presentersList[name] += 1
                    else:
                        presentersList[name] = 1 
                    name = ''                             
    manipulateDictionary(presentersList)
    linkPresenters(tweets)
    return presentersList
    #pdb.set_trace()    

                                      

def printResults():
    print('Hosted by:')
    for name in hosts:
        print(name)
    print('Winners by category')
    for index in range(0, len(categories)):
        print(categories[index], winners[index])
    # for index in range(0, len(specialAwards)):
    #     print(specialAwards[index], specialAwardWinners[index])                                          


def createJSON():
    data = { 
    "metadata": {
        "year": "",
        "hosts": {
            "method": "detected",
            "method_description": ""
            },
        "nominees": {
            "method": "scraped",
            "method_description": ""
            },
        "awards": {
            "method": "detected",
            "method_description": ""
            }
        },
    "data": {
        "unstructured": {
            "hosts": [],
            "winners": [],
            "awards": [],
            "presenters": [],
            "nominees": []
        },
        "structured": {
            "award1": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award2": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award2": {
                "nominees": [],
                "winner": "",
                "presenters": []
            }
        }
    }}
    data['metadata']['year'] = "2013"
    data['data']['unstructured']['hosts'] = hosts
    json_data = json.dumps(data)
    print json_data

            


         
            




