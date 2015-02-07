import json
import nltk
import re
from nltk.util import ngrams

#for debugging purposes only
from pprint import pprint


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
    # for (word, tag) in posTags:



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


         
            




