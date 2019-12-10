class  Memory(object):
    def __init__(self, size, mode, debug):
        self.size = size
        self.ram = ([0] * self.size)
        

    def __debugText(self, text, error = 0):
        if self.debug or error:
            print("[ICC:" + self.name + "] " + text)

    def __set(self, adress, val):
        if adress >= self.size:
            self.__debugText("ERROR: Out of memory", 1)
        self.ram[adress] = val

    def __get(self, adress):
        if adress >= self.size:
            self.__debugText("ERROR: Out of memory", 1)
        return self.ram[adress]

    def setMemory(self, memory):
        self.__debugText("Set internal memory to " + str(memory))
        for i in range(len(memory)):
            self.ram[i] = memory[i]    
