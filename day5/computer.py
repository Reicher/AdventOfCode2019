''' IntCode-computer '''

class ICC(object):
    def __init__(self, debug = 0):
        self.debug = debug
        self.input = 0
        self.output = 0
        
        self.__debugText("Created a empty ICC computer")

    def __debugText(self, text):
        if self.debug:
            print("[ICC] " + text)
            
    def setMemory(self, memory):
        self.__debugText("Set internal memory to " + str(memory))
        self.__rom = memory[:]
        self.memory = memory[:]

    def setMemoryAsRom(self):
        self.__debugText("Setting current memory as ROM")
        self.__rom = self.memory[:]
        
    def getMemory(self):
        self.__debugText("Get memory: " + str(self.memory))
        return self.memory

    def getMemoryAt(self, adress):
        self.__debugText("Get memory at adress: [" + str(adress)
                         + " : " + str(self.memory[adress]) + "]")
        return self.memory[adress]

    def setMemoryAt(self, adress, value):
        self.__debugText("Set memory at adress: [" + str(adress)
                         + " : from " + str(self.memory[adress])
                         + " to " + str(value) + "]")
        self.memory[adress] = value

    def reset(self):
        self.__debugText("Reset memory to rom.")
        self.memory = self.__rom[:]

    def setInput(self, val):
        self.__debugText("Set Input to: " + str(val))
        self.input = val

    def getOutput(self):
        self.__debugText("Got Output: " + str(self.output))
        return self.output
                    
    def run(self):
        pos = 0

        while pos <= len(self.memory):

            # Parse opCode and parameter modes
            code = str(self.memory[pos])            
            opcode = int(code[-2:])            
            paramMode = [int(m) for m in code[:-2][::-1]]
            while len(paramMode) < 3:
                paramMode.append(0)
            reversed(paramMode)

            self.__debugText("Opcode: " + str(opcode) + ", Mode: " + str(paramMode))  

            if opcode == 99: # Program end
                self.__debugText("Program ran succesfull. (opcode 99)")            
                return 0
            if int(opcode) == 1: # Addition
                param = [self.memory[pos+1], self.memory[pos+2], self.memory[pos+3]]
                self.memory[param[2]] = param[0] + param[1]
                pos += 4
            elif opcode == 2: # Multiplication
                param = [self.memory[pos+1], self.memory[pos+2], self.memory[pos+3]]
                self.memory[param[2]] = param[0] * param[1]
                pos += 4
            elif opcode == 3: # Input
                param = [self.memory[pos+1]]
                self.memory[param[0]] = self.input
                pos += 2
            elif opcode == 4: # Output
                param = [self.memory[pos+1]]
                self.output = self.memory[param[0]]
                pos += 2
            else:
                self.__debugText("Program encountered unknown opcode: " + str(opcode))                
                return 1
            
        self.__debugText("Program ended unexpected.")
        return 2
