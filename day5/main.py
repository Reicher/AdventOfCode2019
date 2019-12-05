# Day 5
import computer

print('Day 5')

def readProgramFromFile(filename):
    with open(filename, 'r') as fp:
        line = fp.readline().strip().split(',')        
        return [int(x) for x in line]

cpu = computer.ICC(1)

#program = readProgramFromFile('input.txt')
program = [1002,4,3,4,33]

cpu.setMemory(program)
cpu.setMemoryAsRom()

cpu.setInput(15)

cpu.run()

print("Program output: ", cpu.getOutput())
