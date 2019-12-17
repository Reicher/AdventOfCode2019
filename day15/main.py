# Day 15
import robot
import copy
print('Day 15')

def readProgramFromFile(filename):
    with open(filename, 'r') as fp:
        line = fp.readline().strip().split(',')        
        return [int(x) for x in line]

def readMapFromFile(filename):
    aMap = []
    with open(filename, 'r') as fp:
        lines = [x.strip() for x in fp.readlines()]        
        for line in lines:
            row = []
            for c in line:
                row.append(c)
            aMap.append(row)
    return aMap

def printMap(aMap):
    for row in aMap:
        print(''.join(row))

###########################################################

program = readProgramFromFile('input.txt')

repairBot = robot.Repair("Repair-droid 6000", program, 0)
aMap = repairBot.run()
#repairBot.showMap()

# aMap = readMapFromFile('testmap.txt')

#Fill loop
minute = 0
aMap[9][39] = "o"
printMap(aMap)
print("minute: " + str(minute) + "\n")

newFill = True
while newFill:
    newFill = False
    minute += 1
    newMap = copy.deepcopy(aMap)
    for x in range(len(aMap)):
        for y in range(len(aMap[0])):
            if aMap[x][y] == 'o':
                if aMap[x+1][y] != '#' and aMap[x+1][y] != 'o':
                    newMap[x+1][y] = 'o'
                    newFill = True
                if aMap[x-1][y] != '#' and aMap[x-1][y] != 'o':
                    newMap[x-1][y] = 'o'
                    newFill = True
                if aMap[x][y+1] != '#' and aMap[x][y+1] != 'o':
                    newMap[x][y+1] = 'o'
                    newFill = True
                if aMap[x][y-1] != '#' and aMap[x][y-1] != 'o':
                    newMap[x][y-1] = 'o'
                    newFill = True
                    
    aMap = copy.deepcopy(newMap)
printMap(aMap)
print("Min: " + str(minute))

