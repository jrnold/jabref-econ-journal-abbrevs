#!/usr/bin/python2.6
""" AEA_Abbrev.py
Author: Jeffrey Arnold <jeffrey.arnold@gmail.com>
Description: Creates a Jabref journal abbreviation file using the
American Economic Association Abbreviations, available at
http://www.aeaweb.org/journal/abbrev.html.

Note: Some of the journal names include unicode characters such
as accented vowels. Currently the script handles these by
outputting to a utf-8 encoded output file. It does not
convert accents into LaTeX accents.

Copyright (C) 2009  Jeffrey Arnold
License GPLv3 see <http://www.gnu.org/licenses/>
"""
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup
from os.path import *
import urllib

URL="http://www.aeaweb.org/journal/abbrev.html"
code='utf-8'

soup = BeautifulSoup(urllib.urlopen(URL).read())

def cleanEntries(x):
    x = ''.join(x.findAll(text=True)).strip()
    x = BeautifulStoneSoup(x, convertEntities=BeautifulStoneSoup.HTML_ENTITIES).contents[0]
    x = x.split(r'/')
    return x

journalList = []
for row in soup.findAll('table')[3].findAll('tr')[1:]:
    journal, abb = row.findAll('td')
    journalList += zip(cleanEntries(journal), cleanEntries(abb))
        
for j,a in journalList:
    txt = '='.join([j, a])
    print( txt.encode(code) )

