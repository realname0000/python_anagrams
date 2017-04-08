This is a beginning python exercise.

The programs anagram_prog_*.py read the letters from
the command-line and combines them with the dictionary
file '/usr/share/dict/words' to generate a list of anagrams
where each word is at least 3 letters.

$ time ./anagram_prog_1.py president trump > presidential_anagrams

Maybe 20 minutes later you have ~250,000 anagrams including
['pint', 'rust', 'permed']

There are 4 variants using different ways to extract the word lists.
The iterative one with single recursion is faster than double
recursion.  The 4th one generates a single output per call to the
function (rather than returning eventually with all the results)
making that much the fastest way to get one output.
