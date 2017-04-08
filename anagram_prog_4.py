#!/usr/bin/python

from sys import argv
import extract_module_4

# read arguments into one string
letters=""
for a_word in argv[1:]:
    letters += a_word

# new anagram object
answer = extract_module_4.Answer(letters)
# returns one phrase at a time
while 1:
    phrase = answer.generate()
    if not phrase:
        break
    print phrase
