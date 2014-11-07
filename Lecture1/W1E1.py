# Introduction to Computational Thinking and Data Science

# Week 1
#import pylab as pl
#pl.figure(1)
#pl.plot([1,2,3,4],[1,7,3,5])
#pl.show()

def isAlphabeticalWord(word, wordList=None):
    '''
    isAlphabeticalWord('abcd') should return True
    isAlphabeticalWord('zoo') should return False
    '''
    if (len(word) > 0):
        curr = word[0]
    for letter in word:
        if (curr > letter):
            return False
        else:
            curr = letter
    if wordList is None:
        return True
    return word in wordList
    