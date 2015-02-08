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

awardCategories = ["best actor", "best actress", "best picture", "best movie", "best director", "best original song",
"best foreign film", "best original score","best animated", "tv series", "best supporting" , "best screenplay",
"mini series","Cecil B. DeMille Award"]

#winnerPattern = ['won best']
winnerRegEx = re.compile('won best', re.IGNORECASE);


def findWinners(tweets):
    winnerTrigramsList = dict()
    for index in range(0, len(tweets)):
        # extract all the sentences in a tweet
        sentence = sentenceTokenizer.tokenize(tweets[index])
        for sentenceIndex in range (0, len(sentence)):
            # filter the sentences based on the reg ex for host
            result = winnerRegEx.search(sentence[sentenceIndex])
            if result:
                tokens = wordTokenizer.tokenize(sentence[sentenceIndex])
                #triGrams = nltk.trigrams(tokens)
                for key in nltk.bigrams(tokens):
                    if key in winnerTrigramsList:
                        winnerTrigramsList[key] += 1
                    else:
                        winnerTrigramsList[key] = 1

    winnerTrigramsProperNouns = dict()     
    
    for key in winnerTrigramsList:
        nounTags = 0
        posTags = nltk.pos_tag(key)
        for (data,tag) in posTags:
            if data not in blacklistWords:
                if(tag == 'NNP'):
                    nounTags += 1
        if nounTags ==2:
            winnerTrigramsProperNouns[key] = winnerTrigramsList[key]
    pprint(winnerTrigramsProperNouns)
    #             nounTags = 0
    #             for key in triGrams:
    #                 posTags = nltk.pos_tag(key)
    #                 for(data, tag) in posTags:
    #                     if data not in blacklistWords:
    #                         if(tag == 'NNP'):
    #                             nounTags += 1
    #                 if nounTags == 3:
    #                     if key in winnerTrigramsList:
    #                         winnerTrigramsList[key] += 1
    #                     else:
    #                         winnerTrigramsList[key] = 1
    # pprint(winnerTrigramsList)                     
                # else:
                #     nounTags = 0
                #     biGrams = nltk.bigrams(tokens)
                #     for (data, tag) in triGrams:
                #         if data not in blacklistWords:
                #             if(tag == 'NNP'):
                #                 nounTags += 1
                #     if nounTags == 2                            


webCrawlerPattern = ['[a-z]* nominees [a-z]*']
#hostPattern = "|".join(hostPatternList)
#hostRegEx = re.compile(hostPattern, re.IGNORECASE)

urlText = []
class parseText(HTMLParser.HTMLParser):
    def handle_data(self, data):
        if data != '\n':
            urlText.append(data)
lParser = parseText()

#from urllib2 import urlopen
#from bs4 import BeautifulSoup

#def webCrawler(url):
    # thisurl = "http://www.imdb.com/event/ev0000292/2013"
    # handle = urllib.urlopen(thisurl)
    # lParser.feed(handle.read())
    # lParser.close()
    # for item in urlText:
    #     print item
    #soup = BeautifulSoup(urlopen('http://www.imdb.com/event/ev0000292/2013'))
    #for article in soup.select('div.view-content article'):
    #    print article.text





            


         
            




