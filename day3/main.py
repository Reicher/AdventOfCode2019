# Day 3
from shapely.geometry import LineString
from shapely.geometry import Point

print ('Day 3')

def convert2Vec(cmd):
    mag = int(cmd[1:])
    
    if cmd[0] == 'U':
        return [0, mag]
    elif cmd[0] == 'R':
        return [mag, 0]
    elif cmd[0] == 'D':
        return [0, -mag]
    elif cmd[0] == 'L':
        return [-mag, 0]
    else:
        print("Unknown command.")
        return [0, 0]
    
def convert2Line(vectors):
    start = [0, 0]
    lines = []
    for end in vectors:
        newend = [start[0] + end[0], start[1] + end[1]]    
        #lines.append([[start[0], start[1]], [newend[0], newend[1]]])        
        lines.append(LineString([(start[0], start[1]), (newend[0], newend[1])]))
        start[0] = newend[0]
        start[1] = newend[1]
    return lines

###############################################

with open('input.txt', 'r') as fp:
    strings1 = fp.readline().strip().split(',')
    strings2 = fp.readline().strip().split(',')

print("Got lines")

wire1 = [convert2Vec(cmd) for cmd in strings1]
wire2 = [convert2Vec(cmd) for cmd in strings2]

print("Converted to vec")

lines1 = convert2Line(wire1)
lines2 = convert2Line(wire2)

print("Converted to lines")

dist = []

line_1_len = 0
for ls1 in lines1:
    line_2_len = 0
    for ls2 in lines2:
        s = ls1.intersection(ls2)
        if s:
            dist1 = Point(ls1.coords[0]).distance(s)
            dist2 = Point(ls2.coords[0]).distance(s)
            dist.append(line_1_len + line_2_len + dist1 + dist2)
            
        line_2_len += ls2.length
    line_1_len += ls1.length
            
dist.sort()
print(dist)
print("Smalest: " + str(dist[1]))


