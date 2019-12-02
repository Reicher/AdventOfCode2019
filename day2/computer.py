''' IntCode-computer '''

class ICC(object):
    def __init__(self, debug = 0):
        self.debug = debug
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

    def run(self):
        pos = 0
    
        while pos+3 < len(self.memory):
            opcode = self.memory[pos]

            if opcode == 99: # Program end
                self.__debugText("Program ran succesfull. (opcode 99)")            
                return 0

            param1 = self.memory[pos+1]
            param2 = self.memory[pos+2]
            param3 = self.memory[pos+3]
            self.__debugText("Instruction: " + str(self.memory[pos:pos+4]))

            if opcode == 1: # Addition
                self.memory[param3] = self.memory[param1] + self.memory[param2]
            elif opcode == 2: # Multiplication  
                self.memory[param3] = self.memory[param1] * self.memory[param2]
            else:
                self.__debugText("Program encountered unknown opcode.")
                print(self.memory)
                return 1

            pos += 4

        self.__debugText("Program ended unexpected.")
        return 2
