# Day 2
import computer

print ('Day 2')

def findOutput(cpu, target):
        
    for noun in range(99):
        for verb in range(99):
            cpu.reset()
            cpu.setMemoryAt(1, noun)
            cpu.setMemoryAt(2, verb)

            cpu.run()
            output = cpu.getMemoryAt(0)

            if output == target :
                print("Noun: " + str(noun) + "\nVerb: " + str(verb))
                return 0
            
cpu = computer.ICC(0)

with open('input.txt', 'r') as fp:
    line = fp.readline().strip().split(',')
    program = [int(x) for x in line]
    
    cpu.setMemory(program)
    cpu.setMemoryAsRom()

findOutput(cpu, 19690720)
            
