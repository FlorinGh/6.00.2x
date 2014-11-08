# Week2, Lecture 3, Sequence 2

def strToInt(s):
    """ (str) -> (int)
    Transforms a string in an integer
    """
    number = ''
    for c in s:
        number = number + str(ord(c))
    index = int(number)
    return index

def hashStr(s, tableSize = 101):
    """ (str, int) -> (int)
    Improves the last function by shorten it
    """
    number = ''
    for c in s:
        number = number + str(ord(c))
    index = int(number)%tableSize
    return index

#print 'Index = ', strToInt('a')
#print 'Index = ', strToInt('John is a way cool dude')
print 'Index = ', hashStr('a')
print 'Index = ', hashStr('John is a way cool dude')

print hashStr('Eric', 7)
print hashStr('Chris', 7)
print hashStr('Sarina', 7)
print hashStr('Jill', 7)
