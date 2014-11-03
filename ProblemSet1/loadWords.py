import string

path1 = 'C:/Users/florin_gheorghe/Documents/GitHub/6.00.2x/ProblemSet1/words1.txt'
# word list 1 has space separated words

path2 = 'C:/Users/florin_gheorghe/Documents/GitHub/6.00.2x/ProblemSet1/words2.txt'
# word list 2 has comma separated words

def loadWords():
    try:
        inFile  = open(path2, 'r', 0)
    except IOError:
        print "The wordlist doesn't exist; using some fruits for now"
        return ['apple', 'orange', 'pear', 'lime', 'lemon', 'grape']
    inFile = open(path2, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line,',')
    print "  ", len(wordlist), "words loaded."
    return wordlist

loadWords()

# Uncomment the following function if you want to try the code template
# def loadWords2():
# 	try:
# 		inFile = open(PATH_TO_FILE, 'r', 0)
# 	#line of code to be added here#
# 		print "The wordlist doesn't exist; using some fruits for now"
# 		return ['apple', 'orange', 'pear', 'lime', 'lemon', 'grape', 'pineapple']
# 	line = inFile.readline()
# 	wordlist = string.split(line)
# 	print "  ", len(wordlist), "words loaded."
# 	return wordlist
# PATH_TO_FILE = 'words2.txt'
# loadWords2()
# PATH_TO_FILE = 'doesntExist.txt'
# loadWords2()
