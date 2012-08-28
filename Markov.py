import random
import re

class markov(object):
    def __init__(self,filename):
        with open(filename,'r') as f:
            self._words = f.read().split()
            self._wordCount = len(self._words)

    def getWordList(self,seedWord=None,pattern=r'^.*$'):
        if seedWord is not None:
            chainWords = [self._words[i+1] for i in range(self._wordCount-1)\
                if seedWord == self._words[i].lower()]
        else:
            chainWords = self._words
        p = re.compile(pattern)
        return filter(p.match,chainWords)
    
    def getRandWord(self,seedWord=None,pattern=r'^.*$'):
        return random.choice(self.getWordList(seedWord,pattern))