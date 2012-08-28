import random
import sys
import re

class Markov(object):
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
        p = re.compile(pattern,re.IGNORECASE)
        return filter(p.match,chainWords)
    
    def getRandWord(self,seedWord=None,pattern=r'^.*$'):
        wordList = self.getWordList(seedWord,pattern)
        if len(wordList) == 0:
            return None
        return random.choice(self.getWordList(seedWord,pattern))

def main():
    list = Markov('AStudyInScarlet.txt')
    for word in sys.argv[1:]:
        poem = []
        for letter in word:
            if len(poem) == 0:
                poem.append(list.getRandWord(pattern=r'^[{0}.*$]'.format(letter)))
            else:
                nextWord = list.getRandWord(poem[-1],r'^{0}.*$'.format(letter))
                if nextWord is None:
                    nextWord = list.getRandWord(pattern=r'^{0}.*$'.format(letter))
                poem.append(nextWord)
        
        print word
        print '='*len(word)
        for line in poem:
            print line
        print ''

if __name__ == '__main__':
    main()