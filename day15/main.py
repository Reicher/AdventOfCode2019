# Day 15
import robot

print('Day 15')

def readProgramFromFile(filename):
    with open(filename, 'r') as fp:
        line = fp.readline().strip().split(',')        
        return [int(x) for x in line]

###########################################################

program = readProgramFromFile('input.txt')

repairBot = robot.Repair("Repair-droid 6000", program, 0)
repairBot.run()

