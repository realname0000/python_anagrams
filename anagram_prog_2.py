#!/usr/bin/python

from sys import argv
import anagram_module_2b

# read arguments into one string
letters=""
for a_word in argv[1:]:
    letters += a_word

# new anagram object
answer = anagram_module_2b.Answer(letters)
# returns list of lists
lol = answer.get_list(answer.ana.abc_used, answer.ana.words, []);
for phrase in lol:
    print phrase
