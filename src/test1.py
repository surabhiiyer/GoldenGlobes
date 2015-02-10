import json

from pprint import pprint

json_2013 = 'gg2013.json'
json_data_2013 = open(json_2013)
data_13 = json.load(json_data_2013)
json_data_2013.close()

num_of_tweets = len(data_13)

print "num_of_tweets", num_of_tweets 

tweets = [] 
#extract all the text from tweets 
for i in range (0,num_of_tweets):
    tweets.append(data_13[i]["text"])

print tweets[100] 

json_data_2013.close()
#print json.dumps(data_13["text"], indent=4, sort_keys=True)


