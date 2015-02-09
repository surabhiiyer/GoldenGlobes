# WinnersData.py contains all the reg ex for finding winners for each category.
# It also contains the nominees for each category

import re

nomineesMovieDrama = ['Argo', 'Django Unchained', 'Life of Pi', 'Lincoln', 'Zero Dark Thirty']
nomineesMovieComedy = ['Les Miserables', 'The Best Exotic Marigold Hotel', 'Moonrise Kingdom', 'Salmon Fishing in the Yemen', 'Silver Linings Playbook']
nomineesBestActorDrama = ['Daniel DayLewis', 'Richard Gere', 'John Hawkes', 'Joaquin Phoenix', 'Denzel Washington']
nomineesBestActorMusicalComedy = ['Hugh Jackman', 'Jack Black', 'Bradley Cooper', 'Ewan McGregor', 'Bill Murray']

bestMovieDramaRegExPatterns = ['best picture.*drama', 'best motion picture.*drama', 'best movie.*drama']
bestMovieDramaPattern = '|'.join(bestMovieDramaRegExPatterns)
bestMovieDramaRegEx = re.compile(bestMovieDramaPattern, re.IGNORECASE)
bestMovieComedyRegExPatterns = ['best picture.*comedy', 'best motion picture.*comedy', 'best movie.*comedy']
bestMovieComedyPattern = '|'.join(bestMovieComedyRegExPatterns)
bestMovieComedyRegEx = re.compile(bestMovieComedyPattern, re.IGNORECASE)
bestActorDramaRegEx = re.compile('best actor.*drama', re.IGNORECASE)
bestActorComedyRegEx = re.compile('best actor.*comedy', re.IGNORECASE)
#bestActorComedyRegEx = re.compile('best actor.*comedy', re.IGNORECASE)


winnerRegEx = [bestMovieDramaRegEx, bestMovieComedyRegEx, bestActorDramaRegEx, bestActorComedyRegEx]
nomineesByCategory = [nomineesMovieDrama, nomineesMovieComedy, nomineesBestActorDrama, nomineesBestActorMusicalComedy]