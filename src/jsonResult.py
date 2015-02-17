import json

def prepareJson(year, hosts, allWinners, allCategories, allPresenters, allNominees, winners, categories, specialCategories, nominees_categorized, presentersAward):
    data = { 
    "metadata": {
        "year": "",
        "hosts": {
            "method": "detected",
            "method_description": "Filter the tweets based on keywords like 'hosts', 'hosting', 'host', using regular expressions. Further filter by removing all stop words from each tweet. Find all the proper nouns in these tweets and add them to a dictionary. Naturally, the most frequently occuring Proper Nouns would be the names of the host."
            },
        "nominees": {
            "method": "scraped",
            "method_description": "Using Beautiful Soup, the nominees were scraped from the website http://www.imdb.com/event/ev0000292/(year)."
            },
        "awards": {
            "method": "detected",
            "method_description": "Create a regular expression for each of the award categories. For evaluating winner of each category, use its dedicated RegEx to filter tweets that talking about it. Remove all stop words from these filtered tweets. Extract unigrams from these tweets, "
            }
        },
    "data": {
        "unstructured": {
            "hosts": [],
            "winners": [],
            "awards": [],
            "presenters": [],
            "nominees": []
        },
        "structured": {
            "award1": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award2": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award3": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award4": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award5": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award6": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award7": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award8": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award9": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award10": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award11": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award12": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award13": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award14": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award15": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award16": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award17": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award18": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award19": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award20": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award21": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award22": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award23": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award24": {
                "nominees": [],
                "winner": "",
                "presenters": []
            },
            "award25": {
                "nominees": [],
                "winner": "",
                "presenters": []
            }
        }
    }}
    data['metadata']['year'] = year
    data['data']['unstructured']['hosts'] = hosts
    data['data']['unstructured']['winners'] = allWinners
    data['data']['unstructured']['awards'] = allCategories
    data['data']['unstructured']['presenters'] = allPresenters
    data['data']['unstructured']['nominees'] = allNominees
    unknown = ["unknown"]
    for awardIndex in range(1, 25):
    	presentersList = []
    	awardStr = "award%s" % awardIndex
    	data['data']['structured'][awardStr]["nominees"] = nominees_categorized[awardIndex-1]
    	data['data']['structured'][awardStr]["winner"] = winners[awardIndex-1]
    	for key in presentersAward:
    		if(presentersAward[key] == categories[awardIndex-1]):
    			presentersList.append(key)
    	if (len(presentersList) == 0):		
    		data['data']['structured'][awardStr]["presenters"] = unknown
    	else:
    		data['data']['structured'][awardStr]["presenters"] = presentersList	
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)