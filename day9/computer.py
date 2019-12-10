''' IntCode-computer '''

class ICC(object):
    def __init__(self, name = "", mem_size = 10000, debug = 0):
        self.debug = debug
        self.name = name
        
        self.pos = 0 # Program position
        self.rbo = 0 # Relative base offset
        self.mem_size = mem_size
        self.memory = ([0] * mem_size)
        
        self.input = []
        self.output = 0

        self.cycles = 0
        self.max_cycles = 500
        
        self.__debugText("Created a empty ICC computer")
        
    def __debugText(self, text, error = 0):
        if self.debug or error:
            print("[ICC:" + self.name + "] " + text)
            
    def setMemory(self, memory):
        self.__debugText("Set internal memory to " + str(memory))
        self.__rom = memory[:]
        for i in range(len(memory)):
            self.memory[i] = memory[i]

    def setMemoryAsRom(self):
        self.__debugText("Setting current memory as ROM")
        self.__rom = self.memory[:]
        
    def getMemory(self):
        self.__debugText("Get memory: " + str(self.memory))
        return self.memory

    def __get(self, adress):
        if adress >= self.mem_size:
            self.__debugText("Out of memory", 1)
            return 1
        self.__debugText("Get memory at adress: [" + str(adress)
                         + " : " + str(self.memory[adress]) + "]")
        return self.memory[adress]

    def reset(self):
        self.__debugText("Reset memory to rom. Program position to 0 and empty input")
        self.setMemory(self.__rom[:])
        self.input = []
        self.pos = 0
        self.cycles = 0

    def setInput(self, val):
        self.__debugText("Added input (" + str(val) + ")")
        self.input.append(val)
        self.__debugText("Current input: " + str(self.input))

    def adjustRBO(self, val):
        self.__debugText("Adjusted relative base offset with " + str(val))
        self.rbo += val
        self.__debugText("Current relative base offset: " + str(self.rbo))

    def getOutput(self):
        self.__debugText("Got Output: " + str(self.output))
        return self.output

    def __getValue(self, param, mode):
        if mode == 0: # position
            self.__debugText("Get position value, pos: " + str(param))
            return self.__get(param)        
        if mode == 1: # immediate
            self.__debugText("Get immediate value: " + str(param))
            return param
        elif mode == 2: # relative
            self.__debugText("Get relative value, pos: " + str(param + self.rbo))
            return self.__get(param + self.rbo)
        else:
            self.__debugText("Unknown mode: " + str(mode), 1)
            return 1

    def __set(self, adress, mode, value):    
        if mode == 2: # relative
            self.__debugText("Get relative value, pos: " + str(adress + self.rbo))
            adress += self.rbo
        
        if adress >= self.mem_size:
            self.__debugText("Out of memory", 1)
            return 1        
        self.__debugText("Set memory at adress: [" + str(adress)
                         + " : from " + str(self.memory[adress])
                         + " to " + str(value) + "]")
        self.memory[adress] = value        

    def run(self):
        while self.pos <= len(self.memory):
            # Parse opCode, parameters and parameter modes
            code = str(self.memory[self.pos])            
            opcode = int(code[-2:])            
            mode = [int(m) for m in code[:-2][::-1]]
            while len(mode) < 3:
                mode.append(0)
            reversed(mode)

            self.__debugText(code)
            self.__debugText("Program at position: " + str(self.pos) + ", Opcode: " + str(opcode) + ", Mode: " + str(mode))  

            if opcode == 99: # Program end
                self.__debugText("Program ran succesfull. (opcode 99)")            
                return 0
            if opcode == 1: # Addition
                self.__debugText("1: Addition")
                param = [self.__get(self.pos+1), self.__get(self.pos+2), self.__get(self.pos+3)]
                self.__set(param[2], mode[2], self.__getValue(param[0], mode[0]) + self.__getValue(param[1], mode[1]))
                self.pos += 4
            elif opcode == 2: # Multiplication
                self.__debugText("2: Multiplication")
                param = [self.__get(self.pos+1), self.__get(self.pos+2), self.__get(self.pos+3)]
                self.__set(param[2], mode[2], self.__getValue(param[0], mode[0]) * self.__getValue(param[1], mode[1]))
                self.pos += 4
            elif opcode == 3: # Input
                self.__debugText("3: Input")
                param = [self.__get(self.pos+1)]
                if(len(self.input) < 1):
                    self.__debugText("Not enough input provided.")
                    self.__debugText("Paused at pos: " + str(self.pos))                   
                    return 100
                self.__set(param[0], mode[0], self.input.pop(0))
                self.pos += 2
            elif opcode == 4: # Output
                self.__debugText("4: Output")
                param = [self.__get(self.pos+1)]
                self.output = self.__getValue(param[0], mode[0])
                self.pos += 2
                return 200
            elif opcode == 5: # Jump if true
                self.__debugText("5: Jump if true")
                param = [self.__get(self.pos+1), self.__get(self.pos+2)]
                if self.__getValue(param[0], mode[0]):
                    self.pos = self.__getValue(param[1], mode[1])
                else:
                    self.pos += 3
            elif opcode == 6: # Jump if false
                self.__debugText("6. Jump if false")
                param = [self.__get(self.pos+1), self.__get(self.pos+2)]
                if not self.__getValue(param[0], mode[0]):
                    self.pos = self.__getValue(param[1], mode[1])
                else:
                    self.pos += 3
            elif opcode == 7: # Less Than
                self.__debugText("7. Less Than")
                param = [self.__get(self.pos+1), self.__get(self.pos+2), self.__get(self.pos+3)]
                if self.__getValue(param[0], mode[0]) < self.__getValue(param[1], mode[1]):
                    self.__set(param[2], mode[2], 1)
                else:
                    self.__set(param[2], mode[2], 0)
                self.pos += 4
            elif opcode == 8: # Equals
                self.__debugText("8. Equals")
                param = [self.__get(self.pos+1), self.__get(self.pos+2), self.__get(self.pos+3)]
                if self.__getValue(param[0], mode[0]) == self.__getValue(param[1], mode[1]):
                    self.__set(param[2], mode[2], 1)
                else:
                    self.__set(param[2], mode[2], 0)
                self.pos += 4
            elif opcode == 9: # Adjust Relative base offset
                self.__debugText("8. Adjust Relative base offset")
                param = [self.__get(self.pos+1)]
                self.adjustRBO(self.__getValue(param[0], mode[0]))
                self.pos += 2
            else:
                self.__debugText("Program encountered unknown opcode: " + str(opcode))                
                return 1

            if self.cycles > self.max_cycles:
                self.__debugText("Program reached max allowed cycles: " + str(self.max_cycles))
                return 1
            
            self.cycles += 1
            
        self.__debugText("Program ended unexpected.")
        return 2
