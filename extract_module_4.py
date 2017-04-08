import prepare_module_1

class Answer():
    def __init__(self, letters):
        self.ana = prepare_module_1.Anagram(letters)
        self.stack = []
    
    def advance(self, wordnumber, count_letters, letters):
        self.stack.append([wordnumber, self.ana.words[wordnumber], count_letters, letters])

    def backtrack(self):
        if not len(self.stack):
            return None # means we have finished
        return self.stack.pop()

    # return one wordlist (or None)
    def generate(self):
        # set up from previous state (if any)
        lastset = self.backtrack()
        if lastset:
            start = lastset[0] + 1
            count_letters = lastset[2]
            letters = lastset[3]
        else:
            start = 0
            letters = self.ana.abc_used
            count_letters = 0 # remaining letters to work with
            for f in letters.keys():
                if letters[f] and f != ' ':
                    count_letters += letters[f]
        #
        while 1:
            for pick in range(start,len(self.ana.words)):
                after=self.ana.char_remove(letters, self.ana.words[pick])
                if after:
                    self.advance(pick, count_letters, letters)
                    count_letters -= len(self.ana.words[pick])
                    letters = after
                    # if all letters used prepare to return a solution
                    if not count_letters:
                        phrase = []
                        for qq in self.stack:
                            phrase.append(qq[1])
                        return phrase
                #
                # if word is too long for letters or pick exceeds range then backtrack
                if count_letters < len(self.ana.words[pick]):
                    break # from for loop
            # after end of for loop have to backtrack
            lastset = self.backtrack()
            if not lastset:
                return None
            start = lastset[0] + 1
            count_letters = lastset[2]
            letters = lastset[3]
