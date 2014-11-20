import random as rn

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    reds = [1, 2, 3]
    greens = [4, 5, 6]
    allballs = reds + greens
    balls = 0
    for i in range(numTrials):
        if rn.choice(allballs) in reds:
            balls += 1
    return balls
    
print noReplacementSimulation(3)
