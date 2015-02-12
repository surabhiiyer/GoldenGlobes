import json
import categoriesCrawler
import functionDefinitions
parseJson = functionDefinitions.jsonParser


if __name__ == "__main__":
    tweets = parseJson("gg2013.json")
    print("Welcome To Golden Globes Award Wizard")
    categoriesCrawler.scrapeCategories("http://www.imdb.com/event/ev0000292/2013")
    #filteredTweets = functionDefinitions.filterTweets(tweets)
    #functionDefinitions.findHost(filteredTweets)
    #functionDefinitions.findWinners(filteredTweets)
    #functionDefinitions.findWinnersSpecialAward(filteredTweets)
    #functionDefinitions.printResults()