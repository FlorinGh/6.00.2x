# Week2, Lecture 3, Sequence 1

import random

def rollDie():
    """ (None) -> (int)
    Rolling a dice problem:
    this function returns a random integer between 1 and 6
    every call should return a different value    
    """
    return random.choice([1,2,3,4,5,6])

def rollN(n):
    """ (int) -> (str)
    This function uses the rolling one dice problem to say what sequence
    will be return if rolling a dice n times
    it starts with an empty string and ads up the result
    """
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    return result

#print rollN(5)

def getTarget(goal):
    """ (str) -> (int)
    Returns number of tries in which a a dies should be rolled to get the goal sequence
    """
    numTries = 0
    numRolls = len(goal)
    while True:
        numTries += 1
        result = rollN(numRolls)
        if result == goal:
            return numTries

def runSim(goal, numTrials):
    """ (str,int) -> (float)
    Returns the probability of getting a certain sequence of dices
    Basicaly runs getTarget many times and divides the number of trials at the total
    number of tries
    Number of trials is the number of tests
    Number of tries is the number of dice roll for every test
    """
    total = 0
    for i in range(numTrials):
        total += getTarget(goal)
    aveNumTries = total/float(numTrials)
    print 'Expected answer is ', 1.0/6.0**len(goal)
    print 'Probability is ', 1.0/aveNumTries

runSim('64', 100)