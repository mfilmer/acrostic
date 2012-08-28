import Markov as M
import sys

def main():
    for word in sys.argv[1:]:
        list = M.markov('AStudyInScarlet.txt')
        
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