import json
import categoriesCrawler
import functionDefinitions
import WinnersData
parseJson = functionDefinitions.jsonParser


if __name__ == "__main__":
    tweets = parseJson("gg15mini.json")
    print("Welcome To Golden Globes Award Wizard")
    print()
    categoriesCrawler.scrapeCategories("http://www.imdb.com/event/ev0000292/2015")
    WinnersData.createCategoryNomineeDict()
    filteredTweets = functionDefinitions.filterTweets(tweets)
    functionDefinitions.findHost(filteredTweets)
    functionDefinitions.findWinners(filteredTweets)
    #functionDefinitions.findWinnersSpecialAward(filteredTweets)
    functionDefinitions.printResults()