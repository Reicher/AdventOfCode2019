# Day 16

import copy

print('Day 16')

def readSignalFromFile(filename):
    with open(filename, 'r') as fp:
        line = fp.readline().strip()
        return [int(x) for x in line]

###########################################################

def getP(pattern, output, part, size):
    newPattern = []
    while 1:
        for p in pattern:
            for i in range(output+1):
                newPattern.append(p)
                if len(newPattern) > part:
                    return newPattern[part]                         

#inSignal = [1, 2, 3, 4, 5, 6, 7, 8]
inSignal = readSignalFromFile('input.txt')
signal_size = len(inSignal)

pattern = [0, 1, 0, -1]

n_phases = 100
for phase in range(n_phases):
    print("Processing phase " + str(phase) + " of " + str(n_phases))
    outSignal = []
    pattern_i = 1
    
    for i in range(signal_size):
        output = 0
        
        for j in range(signal_size):
            p_val = getP(pattern, i, j+1, signal_size)
            output += (inSignal[j] * p_val)            
        
        output = int(str(output)[-1])
        outSignal.append(output)

    inSignal = copy.deepcopy(outSignal)

signal = ''.join([str(x) for x in inSignal])
print("After " + str(n_phases) + " phases: " + signal)
