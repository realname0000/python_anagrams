#!/usr/bin/python

from sys import argv
import anagram_module_1

# read arguments into one string
letters=""
argv=argv[1:]
for a_word in argv:
    letters += a_word

# new anagram object
ana = anagram_module_1.Anagram(letters)
# returns list of lists
lol = ana.get_list(ana.abc_used, ana.words, []);
for phrase in lol:
    print phrase
