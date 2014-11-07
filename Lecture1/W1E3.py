# W1E3, W1E4
import pylab as pl
import numpy as np

# Initializing the vectors:
def loadFile():
    high = []
    low = []
    path = 'C:/Users/Adina/Desktop/600.2x/julyTemps.txt'
    inFile = open(path)
    for line in inFile:
        fields = line.split()
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low,high)

def producePlot(lowTemps, highTemps):
    diffTemps = np.array(highTemps) - np.array(lowTemps)
    pl.plot(range(1,32), diffTemps)
    pl.title('Day by Day Ranges in Temperature in Boston in July 2012',fontsize=14)
    pl.xlabel('Days', fontsize = 12)
    pl.ylabel('Temperature Ranges', fontsize = 12)
    pl.show()
    
(low, high) = loadFile()    
producePlot(low, high)
    
    
    