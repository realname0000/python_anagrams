test: out_1.sorted out_2.sorted out_3.sorted out_4.sorted
	@ cmp out_1.sorted out_2.sorted && echo No Difference || echo Files 1 and 2 Do Not Match
	@ cmp out_1.sorted out_3.sorted && echo No Difference || echo Files 1 and 3 Do Not Match
	@ cmp out_1.sorted out_4.sorted && echo No Difference || echo Files 1 and 4 Do Not Match

out_1.sorted: anagram_prog_1.py
	time ./anagram_prog_1.py some words here > out_1.native
	sort -o out_1.sorted out_1.native

out_2.sorted: anagram_prog_2.py
	time ./anagram_prog_2.py some words here > out_2.native
	sort -o out_2.sorted out_2.native

out_3.sorted: anagram_prog_3.py
	time ./anagram_prog_3.py some words here > out_3.native
	sort -o out_3.sorted out_3.native

out_4.sorted: anagram_prog_4.py
	time ./anagram_prog_4.py some words here > out_4.native
	sort -o out_4.sorted out_4.native

clean:
	rm -f out_* *.pyc
