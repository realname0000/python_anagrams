import copy

class Anagram():
    def __init__(self, inwords):
        self.abc_used={}   # letters used
        self.store = []    # answers
        self.already = 0
        for i in range(0,len(inwords)):
            self.add(inwords[i])
        self.words=self.read_wordlist(len(inwords)) # from a file

    def char_remove(self, d, word):
        after=copy.copy(d)
        for i in range(0,len(word)):
            ch = word[i]
            if ch in after.keys():
                if not after[ch]:
                    return None
                after[ch] -= 1
            else:
                return None
        return after

    def show_count(self):
        for a in self.abc_used.keys():
            print "Counted %d of %s" % (self.abc_used[a],a)

    def add(self,a):
        a=a.lower()
        if ((a < 'a') or (a > 'z')):
            return
        # TODO lowercase
        if a in self.abc_used.keys():
            self.abc_used[a] += 1
        else:
            self.abc_used[a] = 1

    # read a file of one-word-per-line and store ordered by length
    def read_wordlist(self, maxletters):
        words_by_length={}
        words=[]
        f=open('/usr/share/dict/words')
     #  f=open('WORDS')
        for line in f:
            w=line.lower()
            for newline in ('r', 'n'):
                if (w[-1] <'a' and w[-1] <'z' ):
                    w=w[:-1]
            lll=len(w)
            if lll<3:
                continue
            used=copy.copy(self.abc_used)
            after=self.char_remove(used, w)
            if not after:
                continue
            try:
                if not words_by_length[lll]:
                    words_by_length[lll]=[]
            except:
                words_by_length[lll]=[]
            words_by_length[lll].append(w)
        for lll in words_by_length.keys():
            if lll > maxletters:
                break
            words += words_by_length[lll]
        return words
