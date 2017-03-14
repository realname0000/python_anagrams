import copy

def char_remove(d, word):
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

class Anagram():
    def __init__(self, inwords):
        self.abc_used={}   # letters used
        self.store = []    # answers
        self.already = 0
        for i in range(0,len(inwords)):
            self.add(inwords[i])
        self.words=self.read_wordlist(len(inwords)) # from a file

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
            after=char_remove(used, w)
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
        print "%d words to work with" % (len(words))
        return words

    # return list of wordlists (or None)
    def get_list(self, used, words, sofar):
        remain=0 # remaining letters to work with
        for f in used.keys():
            if used[f] and f != ' ':
                remain += used[f]
        if not remain:
            return [sofar]
        lol=[]
        for pick in range(0,len(words)):
            if remain < len(words[pick]):
                break # words too long for this search
            after=char_remove(used, words[pick])
            if (after):
                story=sofar[:]
                # pick the first word possible
                story.append(words[pick])
                take=self.get_list(after, words[pick+1:], story)
                for qq in range(0,len(take)):
                    lol.append(take[qq])
        return lol
