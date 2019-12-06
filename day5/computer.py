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

    def __get(self, adress):        
        self.__debugText("Get memory at adress: [" + str(adress)
                         + " : " + str(self.memory[adress]) + "]")
        return self.memory[adress]

    def __set(self, adress, value):
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

    def __getValue(self, param, mode):
        if mode: # immediate
            self.__debugText("Get immediate value: " + str(param))
            return param            
        else: # position
            self.__debugText("Get position value: " + str(self.memory[param]))
            return self.memory[param]

    def run(self):
        pos = 0

        while pos <= len(self.memory):

            # Parse opCode, parameters and parameter modes
            code = str(self.memory[pos])            
            opcode = int(code[-2:])            
            mode = [int(m) for m in code[:-2][::-1]]
            while len(mode) < 3:
                mode.append(0)
            reversed(mode)
            
            print(code)
            self.__debugText("Program at position: " + str(pos) + ", Opcode: " + str(opcode) + ", Mode: " + str(mode))  

            if opcode == 99: # Program end
                self.__debugText("Program ran succesfull. (opcode 99)")            
                return 0
            if opcode == 1: # Addition
                self.__debugText("1: Addition")
                param = [self.__get(pos+1), self.__get(pos+2), self.__get(pos+3)]
                self.__set(param[2], self.__getValue(param[0], mode[0]) + self.__getValue(param[1], mode[1]))
                pos += 4
            elif opcode == 2: # Multiplication
                self.__debugText("2: Multiplication")
                param = [self.__get(pos+1), self.__get(pos+2), self.__get(pos+3)]
                self.__set(param[2], self.__getValue(param[0], mode[0]) * self.__getValue(param[1], mode[1]))
                pos += 4
            elif opcode == 3: # Input
                self.__debugText("3: Input")
                param = [self.__get(pos+1)]
                self.__set(param[0], self.input)
                pos += 2
            elif opcode == 4: # Output
                self.__debugText("4: Output")
                param = [self.__get(pos+1)]
                self.output = self.__getValue(param[0], mode[0])
                pos += 2
            elif opcode == 5: # Jump if true
                self.__debugText("5: Jump if true")
                param = [self.__get(pos+1), self.__get(pos+2)]
                if self.__getValue(param[0], mode[0]):
                    pos = self.__getValue(param[1], mode[1])
                else:
                    pos += 3
            elif opcode == 6: # Jump if false
                self.__debugText("6. Jump if false")
                param = [self.__get(pos+1), self.__get(pos+2)]
                if not self.__getValue(param[0], mode[0]):
                    pos = self.__getValue(param[1], mode[1])
                else:
                    pos += 3
            elif opcode == 7: # Less Than
                self.__debugText("7. Less Than")
                param = [self.__get(pos+1), self.__get(pos+2), self.__get(pos+3)]
                if self.__getValue(param[0], mode[0]) < self.__getValue(param[1], mode[1]):
                    self.__set(param[2], 1)
                else:
                    self.__set(param[2], 0)
                pos += 4
            elif opcode == 8: # Equals
                self.__debugText("8. Equals")
                param = [self.__get(pos+1), self.__get(pos+2), self.__get(pos+3)]
                if self.__getValue(param[0], mode[0]) == self.__getValue(param[1], mode[1]):
                    self.__set(param[2], 1)
                else:
                    self.__set(param[2], 0)
                pos += 4
            else:
                self.__debugText("Program encountered unknown opcode: " + str(opcode))                
                return 1
            
        self.__debugText("Program ended unexpected.")
        return 2
