import prepare_module_1

class Answer():
    def __init__(self, letters):
        self.ana = prepare_module_1.Anagram(letters)
    
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
            after=self.ana.char_remove(used, words[pick])
            if after:
                story=sofar[:]
                # pick the first word possible
                story.append(words[pick])
                take=self.get_list(after, words[pick+1:], story)
                lol += take
        return lol

