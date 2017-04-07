#!/usr/bin/python

from sys import argv
import extract_module_3

# read arguments into one string
letters=""
for a_word in argv[1:]:
    letters += a_word

# new anagram object
answer = extract_module_3.Answer(letters)
# returns list of lists
lol = answer.get_list(answer.ana.abc_used, answer.ana.words, [])
for phrase in lol:
    print phrase
