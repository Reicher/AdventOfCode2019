import algo

def readMapFromFile(filename):
    aMap = []
    with open(filename, 'r') as fp:
        lines = [x.strip() for x in fp.readlines()]
        [aMap.append(x) for x in lines]
    return aMap

def printMap(aMap):
    for row in aMap:
        print(''.join(row))

aMap = readMapFromFile('testmap.txt')
path = algo.Astar([1, 1], [2, 9], aMap)
print(path)



