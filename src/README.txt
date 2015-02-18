{\rtf1\ansi\ansicpg1252\cocoartf1344\cocoasubrtf720
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;\red0\green68\blue254;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural

\f0\fs24 \cf0 GOLDEN GLOBES PROJECT\
\
Libraries used:\
NLTK - for extracting grams and parts of speech tags\
RegEx - for using regular expressions\
BeautifulSoup - for web scraping\
\
Notes:\
This system is adaptable to any edition(year) of the Golden Globes Awards. This is because all the information is either scraped from the internet or extracted from tweets for a particular year. To be more specific, all nominees and award categories are scraped from the website: \
\cf2 http://www.imdb.com/event/ev0000292\cf0  , which is the IMDB page for Golden Globe Awards. The hosts, award winners and presenters are extracted from the tweets.\
\
A few changes need to be made to ensure that this system adapts to all award ceremonies.\
- Change the url mentioned above, if IMDB does not provide information about the other award ceremonies.\
- If the url is changed, alter the scraping technique.\
- Change the list of black listed words. These are the most commonly occurring words besides the stop words. For example, in our case it is Golden Globes, #goldenglobes, etc. For an award show like Oscars, the words oscars, #oscar, academy awards, will be added to this list.\
\
The entry point to this system is from main.py\
The results for the 2013 data is stored in results2013.json\
The results for the 2015 data is stored in results2015.json\
}