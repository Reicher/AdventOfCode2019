# Day 5
import computer

print('Day 5')

def readProgramFromFile(filename):
    with open(filename, 'r') as fp:
        line = fp.readline().strip().split(',')        
        return [int(x) for x in line]

cpu = computer.ICC(1)

program = readProgramFromFile('input.txt')
#program = []

cpu.setMemory(program)
cpu.setMemoryAsRom()

cpu.setInput(5)

cpu.run()

print("Program output: ", cpu.getOutput())
