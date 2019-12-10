# Day 10
import numpy as np
import math

print('Day 10')

def readProgramFromFile(filename):
    map_array = []
    with open(filename, 'r') as fp:
        for line in fp:
            map_array.append([x for x in line.strip()])
    return map_array

def loadExample(num):
    return readProgramFromFile('example' + str(num) + '.txt')

def isInSight(eye, obj, aList):
    line = LineString([(eye['x'], eye['y']), (obj['x'], obj['y'])])
    for asteroid in aList:
        if (eye['x'] == asteroid['x'] and eye['y'] == asteroid['y']) \
           or (obj['x'] == asteroid['x'] and obj['y'] == asteroid['y']):
            continue
        else:
            point = Point(asteroid['x'], asteroid['y'])
            if point.within(line):
                return 0
    return 1

def getVisibles(station, aList):
    inSight = 0
    for asteroid in aList:
        if station['x'] == asteroid['x'] and station['y'] == asteroid['y']:
            continue
        inSight += isInSight(station, asteroid, aList)
            
    return inSight

def findBestSpot(aList):
    i = 0
    num = len(aList)
    for asteroid in aList:
        asteroid["score"] = getVisibles(asteroid, aList)
        print(str(int((i/num)*100)) + " % done.")
        i += 1

    return max(aList, key=lambda s:s['score'])

def createAstroidList(spacemap):    
    alist = []
    width = len(spacemap[0])
    height = len(spacemap)
    for row in range(height):
        for col in range(width):
            if spacemap[row][col] == "#":
                asteroid = {
                  "x": col,
                  "y": row,
                  "score": 0
                }
                alist.append(asteroid)
    return alist

#####################################################################

# {'x': 11, 'y': 11, 'score': 221}

example = 5
#spacemap = loadExample(example)
spacemap = readProgramFromFile("input.txt")
asteroidList = createAstroidList(spacemap)

laser = {
    "x": 11,
    "y": 11,
    "deg": 0}

for i in range(1, 201):
    min_angle = 360
    min_dist = 1000000
    target = 0
    for asteroid in asteroidList:
        if laser['x'] == asteroid['x'] and laser['y'] == asteroid['y']:
            continue

        angle = (np.rad2deg(np.arctan2(asteroid['y'] - laser['y'], asteroid['x'] - laser['x'])) + 90) 
        #angle -= laser['deg']
        angle %= 360
        angle = round(angle, 5)
        
        dist = math.sqrt(math.pow(asteroid['x'] - laser['x'], 2) + math.pow(asteroid['y'] - laser['y'], 2))
        
        if angle >= laser['deg'] and angle <= min_angle:
            if angle < min_angle or (angle == min_angle and dist < min_dist):
                min_angle = angle
                min_dist = dist
                #print(str(asteroid) + " angle: " + str(angle))
                #print("Laser angle: " + str(laser['deg']))
                target = asteroid

    print(str(i) + ". Zapping asteroid " + str(target))
    laser['deg'] = min_angle + 0.00000000001 # uuugly
    #print("Laser angle: " + str(laser['deg']))
    asteroidList.remove(target)
        

#print(asteroidList)


    
