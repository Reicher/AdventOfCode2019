# Day 7
import computer

print('Day 9')

def readProgramFromFile(filename):
    with open(filename, 'r') as fp:
        line = fp.readline().strip().split(',')        
        return [int(x) for x in line]


program = readProgramFromFile('input.txt')
#program = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
#program = [1102,34915192,34915192,7,4,7,99, 0]
#program = [104,1125899906842624,99]

cpu = computer.ICC("day9", 10000, 0)
cpu.setMemory(program)
cpu.setInput(2)

output = []
while cpu.run():
    output.append(cpu.getOutput())

#cpu.getMemory()
print(output[-1])
