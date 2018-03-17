import prepare_module_1

class Answer():
    def __init__(self, letters):
        self.ana = prepare_module_1.Anagram(letters)
    
    # return list of wordlists (or None)
    def get_list(self, used, words, sofar):
        finished = 1
        for f in used.keys():
            if used[f] and f != ' ':
                finished = 0
        if finished:
            return [sofar]
        # find the first word that is possible
        for pick in range(0,len(words)):
            after=self.ana.char_remove(used, words[pick])
            if after:
                story=sofar[:]
                lol=[]
                # one option is do not pick this word
                notake=self.get_list(used, words[pick+1:], story)
                lol += notake
                # one option is do pick this word
                story.append(words[pick])
                take=self.get_list(after, words[pick+1:], story)
                lol += take
                return lol
        return []
