import json
import functionDefinitions
parseJson = functionDefinitions.jsonParser


if __name__ == "__main__":
    # change the path mentioned below when testing
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
    tweets = parseJson("/Users/Harsh/Desktop/Winter 2015/EECS 337 NLP/Project1/gg2013.json")
=======
>>>>>>> Stashed changes
    tweets = parseJson("gg2013.json")
    #for index in range (0, len(tweets)):
        # processTweets id defined in the file functionDefinitions.py
        #functionDefinitions.findHost(tweets[index])
>>>>>>> FETCH_HEAD
    filteredTweets = functionDefinitions.filterTweets(tweets)
    functionDefinitions.findHost(filteredTweets)
    functionDefinitions.findWinners(filteredTweets)
<<<<<<< Updated upstream
    #functionDefinitions.webCrawler("url")
=======
<<<<<<< HEAD
=======
    #functionDefinitions.webCrawler("url")
>>>>>>> FETCH_HEAD
>>>>>>> Stashed changes
