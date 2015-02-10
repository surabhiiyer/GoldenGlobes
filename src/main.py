import json
#import crawler
import functionDefinitions
parseJson = functionDefinitions.jsonParser


if __name__ == "__main__":
    tweets = parseJson("gg2013.json")
    print("Welcome To Golden Globes Award Wizard")
    filteredTweets = functionDefinitions.filterTweets(tweets)
    functionDefinitions.findHost(filteredTweets)
    functionDefinitions.findWinners(filteredTweets)
    #functionDefinitions.findSpecialAwards(filteredTweets)
    functionDefinitions.printResults()