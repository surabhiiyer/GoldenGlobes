import json
import categoriesCrawler
import crawler2
import functionDefinitions
import WinnersData
import jsonResult
import Sentiments
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
    functionDefinitions.findPresenters(filteredTweets)
    presentersList = functionDefinitions.presenters
    print("Walking down the Red Carpet...\n")
    functionDefinitions.getRedCarpetInfo(filteredTweets)
    bestDressed = functionDefinitions.bestDressedList
    worstDressed = functionDefinitions.worstDressedList
    mostTalkedAboutPeople = functionDefinitions.mostTalkedAboutList
    rivalries = functionDefinitions.rivalriesList
    print("Ready to explore!!!\n")
    concString = "\t\tGolden Globes, %s" % year
    print(concString)
    print("\n")
    hostString = ''
    for host in hosts:
        hostString += host + ', '
    concString = "Hosted by: " + hostString    
    print(concString)
    mainMenuLoop = 1
    categories = categoriesCrawler.categories
    specialCategories = categoriesCrawler.specialCategories
    presentersAward = functionDefinitions.presentersAward
    while mainMenuLoop == 1:
        print("\n")
        option = input("Press 1. To go to Red Carpet, 2. To go to the Award Ceremony, 3. To learn what others said about the ceremony, 4. To view all the award presenters, 5. To free me from my duties : \n")
        if option == 1: 
            print("The Red Carpet: ")
            if(len(rivalries) > 1):
                rivalryString = "The most talked about rivalry on the Red Carpet was that between " + rivalries[0] + " and " + rivalries[1] + ". "
                print(rivalryString)
            bestWorstDressedString = bestDressed[0] + " was voted the best dressed, while " + worstDressed[0] + " was voted the worst dressed."
            print(bestWorstDressedString)
            otherBestDressedString = "Other people appreciated for their dress sense were "
            for index in range(1, len(bestDressed)):
                otherBestDressedString += bestDressed[index] + ", "         
            otherBestDressedString += "."    
            print(otherBestDressedString)    
        elif option == 2:
            print("Select one of the award categories to learn more about them.\n")
            for index in range(0, len(categories)):
                concString = ("%s" % (index+1)) + "." + categories[index]
                print(concString)    
            for index in range(0, len(specialCategories)):
                concString = ("%s" % (len(categories)+index+1)) + "." + specialCategories[index]
                print(concString)
            wantToContinue = 1
            presentersFound = 0
            presentersString = ''    
            while wantToContinue == 1:        
                choice = input("Enter your choice: ")
                if choice <= len(categories):
                    concString = categories[choice-1] + ": The winner of this award was " + winners[choice - 1] + ". The nominees were: "
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
                    concString = specialCategories[choice-len(categories)-1] + ": The winner of this award was " + specialAwardWinners[choice-len(categories)-1] + ". "
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
        elif option == 3:
                Sentiments.sentimentEntryPoint(filteredTweets)  
        elif option == 4:
            print("The presenters were as follows: \n")
            presenterString = ''
            for presenter in presentersList:
                presenterString += presenter + ', '
            print(presenterString)            
        elif option == 5:
            mainMenuLoop = 0
            print("See you later!!!!\n")        
    allWinners = []
    for winner in winners:
        allWinners.append(winner)
    for winner in specialAwardWinners:
        allWinners.append(winner)
    allCategories = []
    for category in categories:
        allCategories.append(category)
    for category in specialCategories:
        allCategories.append(category)
    allNominees = []
    for nominees in nominees_categorized:
        for nominee in nominees:
            allNominees.append(nominee)
    allPresenters = []
    for presenter in presentersList:
        allPresenters.append(presenter)            
    jsonResult.prepareJson(year, hosts, allWinners, allCategories, allPresenters, allNominees, winners, categories, specialCategories, nominees_categorized, presentersAward)                    
                
