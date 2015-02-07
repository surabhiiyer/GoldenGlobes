import json
import nltk
import re
from nltk.util import ngrams

#for debugging purposes only
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

from nltk.tokenize import TreebankWordTokenizer
wordTokenizer = TreebankWordTokenizer() 

# Method to process the sentences filtered by processTweets method
# Input: filtered sentence
# still working on this method
def porcessSentence(sentence):
    # toeknize the sentence and use ngrams to create a trigram
    token = wordTokenizer.tokenize(sentence)
    # creates trigrams
    trigrams = ngrams(token, '3')
    # assigns part of speech to each of the words in the trigram
    posTags = nltk.pos_tag(sentence)
    actorLabels = ['NNP', 'NNPS']
    actionLabels = ['VB', 'VBP', 'VBD', 'VBZ']
    possesionLabels = ['NN', 'NNS']
    expressiveLabels = ['NN', 'NNS']
    critcialVerbs = ["won", "win", "nominated", "got", "received", "bagged"]
    #for (word, tag) in posTags:



sentenceTokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# Create a list of regular expressions for award and compile the reg ex
awardPatternList = ['[a-z]* won best [a-z]*', '[a-z]* was nominated for [a-z]*']
awardPatterns = "|".join(awardPatternList)  
awardRegEx = re.compile(awardPatterns, re.IGNORECASE)

# Method to filter the tweets using the reg ex defined above
# Input: tweets stored as an array 
def  processTweets(tweet):
    sentences = sentenceTokenizer.tokenize(tweet)
    for sentenceIndex in range (0, len(sentences)):
        result = awardRegEx.search(sentences[sentenceIndex])
        if result:
            #prints all sentences that match the regular expression
            #for debugging purpose only. We need to call processSentence method
            #defined above to further process the sentences.
            pprint(sentences[sentenceIndex]) 



hostPatternList = ['[a-z]* hosting [a-z]*']
hostPattern = "|".join(hostPatternList)
hostRegEx = re.compile(hostPattern, re.IGNORECASE)

blacklistWords = ['Golden', 'Globes', 'GOLDEN', 'GLOBES']
import operator


hostName = []

# Method to find host name
def findHost(tweet):
    sentenceCount = 0;
    bigramsInfo = dict()
    for index in range (0, len(tweet)):
        sentence = sentenceTokenizer.tokenize(tweet[index])
        verifiedFlag = False;
        for sentenceIndex in range (0, len(sentence)):
            result = hostRegEx.search(sentence[sentenceIndex])
            if result:
                token = re.sub(r'[^a-zA-Z0-9 ]',r'',sentence[sentenceIndex])
                tokens = wordTokenizer.tokenize(token)
                for key in nltk.bigrams(tokens):
                    if key in bigramsInfo:
                        bigramsInfo[key] += 1
                    else:
                        bigramsInfo[key] = 1    
                sentenceCount += 1
            if sentenceCount > 10:
                break
        if sentenceCount > 10:
                break   
    
    bigFinal = dict()     
    
    for key in bigramsInfo:
        nounTags = 0
        posTags = nltk.pos_tag(key)
        for (data,tag) in posTags:
            if data not in blacklistWords:
                if(tag == 'NNP'):
                    nounTags += 1
        if nounTags ==2:
            bigFinal[key] = bigramsInfo[key]

    max = 0        
    for key in bigFinal:
        if(bigFinal[key] > max):
            max = bigFinal[key]

    for key in bigFinal:
        if(bigFinal[key] == max):
            hostName.append(key)

    pprint(hostName)


            


         
            




