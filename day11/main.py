# Day 11
import robot
from PIL import Image

print('Day 11')

def readProgramFromFile(filename):
    with open(filename, 'r') as fp:
        line = fp.readline().strip().split(',')        
        return [int(x) for x in line]


program = readProgramFromFile('input.txt')
paintBot = robot.Painter("Master Painter bot 9000", program, 0)

w, h = 100, 100;
hullmap = [[0 for x in range(w)] for y in range(h)]

hullmap[int(w/2)][int(h/2)] = 1
paintBot.setPosition([int(w/2), int(h/2)])

paintBot.run(hullmap)

print(paintBot.tilesPainted)

# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
img = Image.new( 'RGB', (250,250), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(w):    # for every col:
    for j in range(h):    # For every row
        if hullmap[j][i]:
            pixels[i,j] = (i, j, 100) # set the colour accordingly

img.show()
