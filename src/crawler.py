""" There are 5 nominees. The last value in each list is the winner """ 

from bs4 import BeautifulSoup
import urllib2
import re
import pprint

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


def crawl(page_url): 
	#page_url = "http://www.imdb.com/event/ev0000292/2013"
	html_page = urllib2.urlopen(page_url)
	soup = BeautifulSoup(html_page)

	winners = [] 
	for a in soup.findAll('h3'):
		if a.text == 'WINNER': 
			next_tag = a.findNext('div')
			for b in next_tag.findAll('strong'): 
				for c in b.findAll('a', attrs={'href': re.compile("^/title")}):
					#print a.string
					#print c.string  
					winners.append(c.string)	

	#print '#####WINNERS#####', len(winners)

	#pprint.pprint(winners)

	big_list = [] 
	nominees = [] 
	for i in soup.findAll('h3'):
		if i.text == 'NOMINEES': 
			nextNode = i.findNext('div',attrs={'class':'alt'})
			for j in nextNode.findAll('strong'): 
				for k in j.findAll('a', attrs={'href': re.compile("^/title")}):
					#print k.string  
					nominees.append(k.string)	

			nextNode2 = nextNode.findNext('div', attrs={'class':'alt2'})
			for j in nextNode2.findAll('strong'): 
				for k in j.findAll('a', attrs={'href': re.compile("^/title")}):
					#print k.string  
					nominees.append(k.string)

			nextNode3 = nextNode2.findNext('div',attrs={'class':'alt'})
			for j in nextNode3.findAll('strong'): 
				for k in j.findAll('a', attrs={'href': re.compile("^/title")}):
					#print k.string  
					nominees.append(k.string)	

			nextNode4 = nextNode3.findNext('div', attrs={'class':'alt2'})
			for j in nextNode4.findAll('strong'): 
				for k in j.findAll('a', attrs={'href': re.compile("^/title")}):
					#print k.string  
					#num_evens.setdefault(even_counter,[]).append(k.string)
					nominees.append(k.string)	

		#print "#####NOMINEES#######"
		#pprint.pprint(nominees)

		#creating lists 
		#print "#### NOMINIEES CATEGORIZED ####"
		nominees_categorized = []
		nominees_categorized = list(chunks(nominees, 4))
		#pprint.pprint(nominees_categorized)
		#print "#### NOMINIEES CATEGORIZED ####", len(nominees_categorized)

		for i in range(len(nominees_categorized)): 
			nominees_categorized[i].append(winners[i])

		#print "#### NOMINIEES CATEGORIZED WITH WINNERS ####"
		#pprint.pprint(nominees_categorized)
		#print "#### NOMINIEES CATEGORIZED ####", len(nominees_categorized)

	return nominees_categorized 

nominees_categorized = []
nominees_categorized = crawl("http://www.imdb.com/event/ev0000292/2013")

pprint.pprint(nominees_categorized)

# Best Motion Picture - Drama

# Best Motion Picture - Comedy or Musical

# Best Performance by an Actor in a Motion Picture - Drama

# Best Performance by an Actor in a Motion Picture - Comedy or Musical

# Best Performance by an Actress in a Motion Picture - Drama

# Best Performance by an Actress in a Motion Picture - Comedy or Musical

# Best Performance by an Actor in a Supporting Role in a Motion Picture

# Best Performance by an Actress in a Supporting Role in a Motion Picture

# Best Director - Motion Picture

# Best Screenplay - Motion Picture

# Best Original Song - Motion Picture

# Best Original Score - Motion Picture

# Best Foreign Language Film

# Best Animated Film

# Best Performance by an Actor in a Television Series - Drama

# Best Performance by an Actor in a Mini-Series or a Motion Picture Made for Television

# Best Performance by an Actor in a Television Series - Musical or Comedy

# Best Performance by an Actress in a Television Series - Drama

# Best Performance by an Actress in a Mini-Series or a Motion Picture Made for Television
# Best Performance by an Actor in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television

# Best Performance by an Actress in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television

# Best Television Series - Musical or Comedy

# Best Television Series - Drama
# Best Mini-Series or Motion Picture Made for Television
