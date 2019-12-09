# Day 7
import computer
import itertools

print('Day 7')

def readProgramFromFile(filename):
    with open(filename, 'r') as fp:
        line = fp.readline().strip().split(',')        
        return [int(x) for x in line]


program = readProgramFromFile('input.txt')
phasePermutaions = list(itertools.permutations([5, 6, 7, 8, 9]))
names = ["A", "B", "C", "D", "E"]

highscore = 0
for phase in phasePermutaions:
    amplifier = []
    for i in range(5):
        cpu = computer.ICC(names[i], 0)
        cpu.setMemory(program)
        cpu.setInput(phase[i])
        amplifier.append(cpu)

    active = 0
    amplifier[active].setInput(0)
    while amplifier[active].run():        
        signal = amplifier[active].getOutput()
        active = (active + 1) % 5
        amplifier[active].setInput(signal)


    finalSignal = amplifier[4].getOutput()
    if finalSignal > highscore:
        print("New highscore! (" + str(finalSignal) + ")")
        highscore = finalSignal

print("Program output: ", highscore)
