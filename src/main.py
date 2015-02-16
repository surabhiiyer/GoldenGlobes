import json
import categoriesCrawler
import crawler2
import functionDefinitions
import WinnersData
from pprint import pprint
parseJson = functionDefinitions.jsonParser


if __name__ == "__main__":
    print("\n\t\tHi my name is Abu, your personal guide to Golden Globes Award ceremonies\n")
    year = input("Which edition(year) of the awards are you interested in: ")
    jsonPath = input("What trail do I follow to get the tweets: ")
    print("Please wait while I read the tweets and figure out which ones are useful...\n")
    tweets = parseJson(jsonPath)
    # Method to filter the tweets, and remove irrelevant tweets
    filteredTweets = functionDefinitions.filterTweets(tweets)
    print("Done filtering tweets. Shelob, the spider, will search the web for additional resources.\n")
    url = "http://www.imdb.com/event/ev0000292/%s" % year 
    categoriesCrawler.scrapeCategories(url)
    nominees_categorized = []
    nominees_categorized = crawler2.crawl(url)
    print("Populating Nominees and Categories...\n")
    WinnersData.createCategoryNomineeDict(nominees_categorized)
    print("Identifying the Hosts...\n")
    hosts = functionDefinitions.findHost(filteredTweets)
    print("Extracting Winners...\n")
    winners = functionDefinitions.findWinners(filteredTweets, nominees_categorized)
    specialAwardWinners = functionDefinitions.findWinnersSpecialAward(filteredTweets)
    print("Waiting for Presenters...\n")
    presentersList = functionDefinitions.findPresenters(filteredTweets)
    #functionDefinitions.createJSON()
    print("Ready to explore!!!\n")
    concString = "\t\tGolden Globes, %s" % year
    print(concString)
    print("\n")
    hostString = ''
    for host in hosts:
        hostString += host + ', '
    concString = "Hosted by: " + hostString    
    print(concString)
    print("\n")
    print("Select one of the award categories to learn more about them.\n")
    categories = categoriesCrawler.categories
    for index in range(0, len(categories)):
        concString = ("%s" % (index+1)) + "." + categories[index]
        print(concString)
    specialCategories = categoriesCrawler.specialCategories    
    for index in range(0, len(specialCategories)):
        concString = ("%s" % (len(categories)+index+1)) + "." + specialCategories[index]
        print(concString)
    wantToContinue = 1
    presentersFound = 0
    presentersString = ''
    presentersAward = functionDefinitions.presentersAward    
    while wantToContinue == 1:        
        choice = input("Enter your choice: ")
        if choice < len(categories):
            concString = categories[choice-1] + ": The winner for this award was " + winners[choice - 1] + ". The nominees were: "
            for nominee in nominees_categorized[choice-1]:
                if nominee != winners[choice-1]:
                    concString += nominee + ", "
            concString += ". "
            for key in presentersAward:
                if presentersAward[key] == categories[choice-1]:
                    presentersString += " " + key
                    presentersFound = 1
            if presentersFound == 1:
                concString += "The award was presented by" + presentersString +"."
                presentersFound = 0
                presentersString = ''       
            print(concString)
        else:
            concString = specialCategories[choice-len(categories)-1] + ": The winner for this award was " + specialAwardWinners[choice-len(categories)-1] + ". "
            for key in presentersAward:
                if presentersAward[key] == specialCategories[choice-len(categories)-1]:
                    presentersString += " " + key
                    presentersFound = 1
            if presentersFound == 1:
                concString += "The award was presented by" + presentersString +"."
                presentersFound = 0
                presentersString = ''   
            print(concString)    
        wantToContinue = input("Explore more categories? (Yes->1 , No->0): ")
                
