#!/usr/local/bin/python
# coding: utf-8

"""
Script capable of renaming all files in folder following the layout -> S#E#.ext

Example:
Gotham.S01.E10.720p.HDTV.lexus.mp4 -> S1E10.mp4
--------------------------------------------------------------------------------------------
SYSTEM REQUIREMENTS:

-UNIX based OS or Windows
--------------------------------------------------------------------------------------------
EXECUTION METHOD:
./NameChanger.py path season startEpisode

Example:
./NameChanger.py /Users/hugocurado/Desktop/G2 2 1
"""

__author__ = "Hugo Filipe Curado"
__copyright__ = """
				This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike
				4.0 International License.
				https://creativecommons.org/licenses/by-nc-sa/4.0/
				"""
__version__ = "1.0"
__maintainer__ = "Hugo Filipe Curado"
__email__ = "hfsvbc@hugocurado.info"


from os import listdir, rename
from os.path import isfile, join

def getFiles(path):
	"""
	returns every file in a folder

	requires: the path to the folder as str
	ensures: a list with the names of every file as str
	"""
	return  [join(path, f) for f in listdir(path) if isfile(join(path, f)) if f != '.DS_Store']

def nameChanger(Season, EpisodeStart, path):
	"""
	changes the names of the files in the folder according with following layout: S#E#.ext

	requires: The Season as an int, the number of the season. The EpisodeStart as an int, the
	number of the first episode. The path as an str, the path to the folder containing the files
	ensures:  every file in the folder renamed according to the layout mentioned above.
	"""
	episodes = sorted(getFiles(path))
	for ep in episodes:
		ext = ep.split('.')[-1]
		rename(ep, join(path, 'S'+str(Season)+'E'+str(EpisodeStart)+'.'+ext))
		EpisodeStart += 1


#----------------Var retrival and options check----------------
if __name__ == '__main__':
    import argparse, os
    parser = argparse.ArgumentParser(description = "TV Shows name changer. Simply\
    	indicate path to folder Season Number and First Episode")
    #INPUT
    parser.add_argument('Path', metavar = 'location',
                        help = 'the folder containing the episodes')
    
    parser.add_argument('Season', metavar = 'season', type = int, 
                        help = 'the number of the season')
    
    parser.add_argument('startEpisode', metavar = 'episode', type = int,
                        help = 'the number of the first episode')

    arguments = parser.parse_args()
    nameChanger(arguments.Season, arguments.startEpisode, arguments.Path)
