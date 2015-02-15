# WinnersData.py contains all the reg ex for finding winners for each category.
# It also contains the nominees for each category

import re

nomineesMovieDrama = ['Argo', 'Django Unchained', 'Life of Pi', 'Lincoln', 'Zero Dark Thirty']
nomineesMovieComedy = ['Les Miserables', 'The Best Exotic Marigold Hotel', 'Moonrise Kingdom', 'Salmon Fishing in the Yemen', 'Silver Linings Playbook']
nomineesBestActorDrama = ['Daniel DayLewis', 'Richard Gere', 'John Hawkes', 'Joaquin Phoenix', 'Denzel Washington']
nomineesBestActorMusicalComedy = ['Hugh Jackman', 'Jack Black', 'Bradley Cooper', 'Ewan McGregor', 'Bill Murray']
nomineesBestActressDrama = ['Jessica Chastain', 'Marion Cotillard', 'Helen Mirren', 'Naomi Watts', 'Rachel Weisz']
nomineesBestActressComedy = ['Jennifer Lawrence', 'Emily Blunt', 'Judi Dench', 'Maggie Smith', 'Meryl Streep']
nominessSupportingActor = ['Christopher Waltz', 'Alan Arkin', 'Leonardo DiCaprio', 'Philip Seymour Hoffman', 'Tommy Lee Jones']
nomineesSupportingActress = ['Anne Hathaway', 'Amy Adams', 'Sally Field', 'Helen Hunt', 'Nicole Kidman']
nomineesBestDirector = ['Ben Affleck', 'Kathryn Bigelow', 'Ang Lee', 'Steven Spielberg', 'Quentin Tarantino']
nomineesBestScreenplay = ['Quentin Tarantino', 'Chris Terrio', 'Tony Kushner', 'David O. Russel', 'Mark Boal']
nomineesForeignLanguageFilm = ['Amour', 'Kon-Tiki', 'The Intouchables', 'A Royal Affair', 'Rust and Bone']
nomineesBestAnimatedFilm = ['Brave', 'Frankenweenie', 'Hotel Transylvania', 'Rise of the Guardians', 'Wreck-It Ralph']
nomineesActorTVSeriesDrama = ['Damian Lewis', 'Steve Buscemi', 'Bryan Cranston', 'Jeff Daniels', 'Jon Hamm']
nomineesActorMiniSeries = ['Kevin Costner', 'Benedict Cumberbatch', 'Woody Harrelson', 'Toby Jones', 'Clive Owen']
nomineesActorTVSeriesComedy = ['Don Cheadle', 'Alec Baldwin', 'Louis C.K.', 'Matt LeBlanc', 'Jim Parsons']
nomineesActressTVSeriesDrama = ['Claire Danes', 'Connie Britton', 'Glenn Close', 'Michelle Dockery', 'Julianna Margulies']
nomineesActressMiniSeries = ['Julianne Moore', 'Nicole Kidman', 'Jessica Lange', 'Sienna Miller', 'Sigourney Weaver']
nomineesActressTVSeriesComedy = ['Lena Dunham', 'Zooey Deschanel', 'Tina Fey', 'Julia LouisDreyfus', 'Amy Poehler']
nomineesSupportingActorSeries = ['Ed Harris', 'Max Greenfield', 'Danny Huston', 'Mandy Patinkin', 'Eric Stonestreet']
nomineesSupportingActressSeries = ['Maggie Smith', 'Hayden Panettiere', 'Archie Panjabi', 'Sarah Paulson', 'Sofia Vergara']
nomineesTelevisionSeriesComedy = ['Girls', 'The Big Bang Theory', 'Episodes', 'Modern Family', 'Smash']
nomineesTelevisionSeriesDrama = ['Homeland', 'Downton Abbey', 'Boardwalk Empire', 'Breaking Bad', 'The Newsroom']
nomineesBestMiniSeries = ['Game Change', 'The Girl', 'Hatfields & McCoys', 'The Hour', 'Political Animals']

categories = ['Best Motion Picture Drama', 'Best Motion Picture Musical or Comedy', 'Best Actor Drama', 'Best Actor Musical or Comedy', 'Best Actress Drama',
'Best Actress Musical or Comedy', 'Best Actor in a Supporting Role', 'Best Actress in a Supporting Role', 'Best Director', 'Best Screenplay',
'Best Foreign Language Film', 'Best Animated Film', 'Best Actor TV Series Drama', 'Best Actor in a Mini-Series', 'Best Actor TV Series Musical or Comedy',
'Best Actress TV Series Drama', 'Best Actress in a Mini-Series', 'Best Actress TV Series Musical or Comedy', 'Best Performance by an Actor in a Supporting Role in a Series',
'Best Performance by an Actress in a Supporting Role in a Series', 'Best Television Series - Musical or Comedy', 'Best Television Series - Drama',
'Best Mini Series']

bestMovieDramaRegExPatterns = ['best picture.*drama', 'best motion picture.*drama', 'best movie.*drama']
bestMovieDramaPattern = '|'.join(bestMovieDramaRegExPatterns)
bestMovieDramaRegEx = re.compile(bestMovieDramaPattern, re.IGNORECASE)
bestMovieComedyRegExPatterns = ['best picture.*comedy', 'best motion picture.*comedy', 'best movie.*comedy']
bestMovieComedyPattern = '|'.join(bestMovieComedyRegExPatterns)
bestMovieComedyRegEx = re.compile(bestMovieComedyPattern, re.IGNORECASE)
bestActorDramaRegEx = re.compile('best actor.*drama', re.IGNORECASE)
bestActorComedyRegEx = re.compile('best actor.*comedy', re.IGNORECASE)
bestActressDramaRegEx = re.compile('best actress.*drama', re.IGNORECASE)
bestActressComedyRegEx = re.compile('best actress.*comedy', re.IGNORECASE)
bestSupportingActorRegExPatterns = ['best supporting actor', 'best actor.*supporting']
bestSupportingActorPattern = '|'.join(bestSupportingActorRegExPatterns)
bestSupportingActorRegEx = re.compile(bestSupportingActorPattern, re.IGNORECASE)
bestSupportingActressRegExPatterns = ['best supporting actress', 'best actress.*supporting']
bestSupportingActressPattern = '|'.join(bestSupportingActressRegExPatterns)
bestSupportingActressRegEx = re.compile(bestSupportingActressPattern, re.IGNORECASE)
bestDirectorRegEx = re.compile('best director', re.IGNORECASE)
bestScreenplayRegEx = re.compile('best screenplay', re.IGNORECASE)
bestForeignLanguageRegEx = re.compile('best foreign language', re.IGNORECASE)
bestAnimatedFilmRegExPatterns = ['best animated film', 'best animated movie']
bestAnimatedFilmPattern = '|'.join(bestAnimatedFilmRegExPatterns)
bestAnimatedFilmRegEX = re.compile(bestAnimatedFilmPattern, re.IGNORECASE)
bestActorTVSeriesDramaRegExPatterns = ['best actor.*television series.*drama', 'best actor.*tv.*series.*drama']
bestActorTVSeriesDramaPattern = '|'.join(bestActorTVSeriesDramaRegExPatterns)
bestActorTVSeriesDramaRegEX = re.compile(bestActorTVSeriesDramaPattern, re.IGNORECASE)
bestActorMiniSeriesRegEX = re.compile('best actor.*mini.*series', re.IGNORECASE)
bestActorTVSeriesComedyRegExPatterns = ['best actor.*television.*series.*comedy', 'best actor.*tv.*series.*comedy']
bestActorTVSeriesComedyPattern = '|'.join(bestActorTVSeriesComedyRegExPatterns)
bestActorTVSeriesComedyRegEX = re.compile(bestActorTVSeriesComedyPattern, re.IGNORECASE)
bestActressTVSeriesDramaRegExPatterns = ['best actress.*television series.*drama', 'best actress.*tv series.*drama']
bestActressTVSeriesDramaPattern = '|'.join(bestActressTVSeriesDramaRegExPatterns)
bestActressTVSeriesDramaRegEX = re.compile(bestActressTVSeriesDramaPattern, re.IGNORECASE)
bestActressMiniSeriesRegEX = re.compile('best actress.*mini.*series', re.IGNORECASE)
bestActressTVSeriesComedyRegExPatterns = ['best actress.*television.*series.*comedy', 'best actress.*tv.*series.*comedy']
bestActressTVSeriesComedyPattern = '|'.join(bestActressTVSeriesComedyRegExPatterns)
bestActressTVSeriesComedyRegEX = re.compile(bestActressTVSeriesComedyPattern, re.IGNORECASE)
bestSupportingActorTVSeriesRegExPatterns = ['best supporting actor.*[tv]*.*[series]*', 'best actor.*supporting.*[tv]*.*[series]*']
bestSupportingActorTVSeriesPattern = '|'.join(bestSupportingActorTVSeriesRegExPatterns)
bestSupportingActorTVSeriesRegEx = re.compile(bestSupportingActorTVSeriesPattern, re.IGNORECASE)
bestSupportingActressTVSeriesRegExPatterns = ['best supporting actress.*[tv]*.*[series]*', 'best actress.*supporting.*[tv]*.*[series]*']
bestSupportingActressTVSeriesPattern = '|'.join(bestSupportingActressTVSeriesRegExPatterns)
bestSupportingActressTVSeriesRegEx = re.compile(bestSupportingActressTVSeriesPattern, re.IGNORECASE)
bestTVSeriesComicalRegExPatterns = ['best [television]* series.*[musical or comedy]*']
bestTVSeriesComicalPattern = '|'.join(bestTVSeriesComicalRegExPatterns)
bestTVSeriesComicalRegEx = re.compile(bestTVSeriesComicalPattern, re.IGNORECASE)
bestTVSeriesDramaRegExPatterns = ['best [television]* series.*drama']
bestTVSeriesDramaPattern = '|'.join(bestTVSeriesDramaRegExPatterns)
bestTVSeriesDramaRegEx = re.compile(bestTVSeriesDramaPattern, re.IGNORECASE)
bestMiniSeriesRegEX = re.compile('best mini.*series', re.IGNORECASE)
bestDressedRegEx = ['best-dressed', 'dress']

winnerRegEx = [bestMovieDramaRegEx, bestMovieComedyRegEx, bestActorDramaRegEx, bestActorComedyRegEx,
bestActressDramaRegEx, bestActressComedyRegEx, bestSupportingActorRegEx, bestSupportingActressRegEx, bestDirectorRegEx,
bestScreenplayRegEx, bestForeignLanguageRegEx, bestAnimatedFilmRegEX, bestActorTVSeriesDramaRegEX, bestActorMiniSeriesRegEX,
bestActorTVSeriesComedyRegEX, bestActressTVSeriesDramaRegEX, bestActressMiniSeriesRegEX, bestActressTVSeriesComedyRegEX, bestSupportingActorTVSeriesRegEx,
bestSupportingActressTVSeriesRegEx, bestTVSeriesComicalRegEx, bestTVSeriesDramaRegEx, bestMiniSeriesRegEX]

nomineesByCategory = [nomineesMovieDrama, nomineesMovieComedy, nomineesBestActorDrama, nomineesBestActorMusicalComedy,
nomineesBestActressDrama, nomineesBestActressComedy, nominessSupportingActor, nomineesSupportingActress, nomineesBestDirector,
nomineesBestScreenplay, nomineesForeignLanguageFilm, nomineesBestAnimatedFilm, nomineesActorTVSeriesDrama, nomineesActorMiniSeries,
nomineesActorTVSeriesComedy, nomineesActressTVSeriesDrama, nomineesActressMiniSeries, nomineesActressTVSeriesComedy, nomineesSupportingActorSeries, nomineesSupportingActressSeries,
nomineesTelevisionSeriesComedy, nomineesTelevisionSeriesDrama, nomineesBestMiniSeries]
