# Day 12

import re
import math

print('Day 12')

def readProgramFromFile(filename):
    moon_array = []
    with open(filename, 'r') as fp:
        for line in fp:
            coords = [ int(x) for x in  re.findall(r'-?\d+', line)]            
            moon_array.append(Moon(coords[0], coords[1], coords[2]))
    return moon_array

class Moon(object):
    counter = 0
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.vx = 0
        self.vy = 0
        self.vz = 0

        self.ix = x
        self.iy = y
        self.iz = z
        
        self.id = Moon.counter
        Moon.counter += 1

    def __str__(self):
        return "Moon " + str(self.id) + ". Pos (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ") " + \
               "Vel (" + str(self.vx) + ", " + str(self.vy) + ", " + str(self.vz) + ")"
    
    def __eq__(self, other): 
        if not isinstance(other, Moon):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.id == other.id

    def moveOnStep(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def getPotentialEnergy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def getKineticEnergy(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

    def getTotalEnergy(self):
        return self.getPotentialEnergy() * self.getKineticEnergy()

def applyGravity(moon, other):
    if moon.x > other.x:
        moon.vx -= 1
    elif moon.x < other.x:
        moon.vx += 1

    if moon.y > other.y:
        moon.vy -= 1
    elif moon.y < other.y:
        moon.vy += 1

    if moon.z > other.z:
        moon.vz -= 1
    elif moon.z < other.z:
        moon.vz += 1

def doStep(moons):
    #Gravity
    for moon in moons:
        for other in moons:
            if moon == other:
                continue
            applyGravity(moon, other)
    
    for moon in moons:
        moon.moveOnStep()

def gotxPeriods(moons):
    for moon in moons:
        if moon.x != moon.ix:
            return False

    return True

def gotyPeriods(moons):
    for moon in moons:
        if moon.y != moon.iy:
            return False

    return True

def gotzPeriods(moons):
    for moon in moons:
        if moon.z != moon.iz:
            return False

    return True

def compute_lcm(x, y):
   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm

#####################################################################

moons = readProgramFromFile("input.txt")

step = 1
x_period = 0
y_period = 0
z_period = 0

while not x_period or not y_period or not z_period:
    doStep(moons)
    step += 1

    if not x_period and gotxPeriods(moons):
        x_period = step

    if not y_period and gotyPeriods(moons):
        y_period = step

    if not z_period and gotzPeriods(moons):
        z_period = step             

period = [x_period, y_period, z_period]
print(period)

if min(min(period[0], period[1]), period[2]) == period[0]:
    minsta_i = 0
elif min(min(period[0], period[1]), period[2]) == period[1]:
    minsta_i = 1
elif min(min(period[0], period[1]), period[2]) == period[2]:
    minsta_i = 2

minsta = period[minsta_i]
while minsta % period[0] != 0 or \
      minsta % period[1] != 0 or \
      minsta % period[2] != 0:
    minsta += period[minsta_i]

print(minsta)

