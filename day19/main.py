# Day 15
import computer
print('Day 19')

def readProgramFromFile(filename):
    with open(filename, 'r') as fp:
        line = fp.readline().strip().split(',')        
        return [int(x) for x in line]

def printMap(aMap):
    for row in aMap:
        print(''.join(row))

def findMinDistancefor(tractorMap, size):
    return (0, 0)

###########################################################

program = readProgramFromFile('input.txt')
cpu = computer.ICC('Droid-system', 1000)
cpu.setMemory(program)

w = 100
h = 100
tractorMap = [[' ' for x in range(w)] for y in range(h)]
x = 5
y = 5

for x in range(w):
    for y in range(h):
        cpu.reset()
        cpu.setInput(x)
        cpu.setInput(y)
        cpu.run()
        if cpu.getOutput():
            tractorMap[x][y] = '#'
        else:
            tractorMap[x][y] = '.'

printMap(tractorMap)
                     
