import computer
import algo

import random
import copy
import numpy as np

class Repair(object):
    def __init__(self, name, program, debug):
        self.cpu = computer.ICC(name, 10000, debug)
        self.name = name
        self.cpu.setMemory(program)

        self.map = [[' ' for x in range(50)] for y in range(50)] 
        
        self.position = [25, 25]
        self.start = [25, 25]
        self.ox = []
        self.cmd = 0

    def showMap(self):
        printMap = self.map.copy()
        printMap[self.position[0]][self.position[1]] = "X"
        printMap[self.start[0]][self.start[1]] = "S"

        for row in printMap:
            print(''.join(row))

    def getPos(self):
        newPos = self.position.copy()
        if self.cmd == 1: # North
            newPos[1] -= 1
        elif self.cmd == 2: # South
            newPos[1] += 1
        elif self.cmd == 3: # West
            newPos[0] -= 1
        elif self.cmd == 4: # East
            newPos[0] += 1
        return newPos

    def updateMap(self, pos, state):
        self.map[pos[0]][pos[1]] = state

    def run(self):
        while self.cpu.run() != 1:
            # INPUT
            if self.cpu.state == computer.STATE.WAITING:
                dire = []
                if self.map[self.position[0]][self.position[1]-1] != "#":
                    dire.append(1)
                if self.map[self.position[0]][self.position[1]+1] != "#":
                    dire.append(2)
                if self.map[self.position[0]-1][self.position[1]] != "#":
                    dire.append(3)
                if self.map[self.position[0]+1][self.position[1]] != "#":
                    dire.append(4)
                self.cmd = random.choice(dire)
                self.cpu.setInput(self.cmd)

            # OUTPUT    
            elif self.cpu.state == computer.STATE.OUTPUT:
                output = self.cpu.getOutput()                
                if output == 0:
                    self.updateMap(self.getPos(), '#')
                    continue
                
                self.position = self.getPos()
                
                if output == 2:
                    self.ox = self.position.copy()
                    print("Found oxygene unit at " + str(self.position))
                    #directions = algo.Astar(self.start, self.position, self.map)
                    #print(directions)
                    #print("length: " + str(len(directions)))
                    #self.showMap()
                    #return
                    
        return self.map
