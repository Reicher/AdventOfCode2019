import computer

class Painter(object):
    def __init__(self, name, program, debug):
        self.cpu = computer.ICC(name, 10000, debug)
        self.name = name
        self.cpu.setMemory(program)
        self.position = [0, 0]
        self.rotation = 0
        self.color = 0
        self.output = []
        self.tilesPainted = 0

    def setPosition(self, pos):
        self.position = pos

    def run(self, hullmap):
        paintmap = [[0 for x in range(len(hullmap[0]))] for y in range(len(hullmap))]
        
        while self.cpu.run():
            self.cpu.setInput(hullmap[self.position[0]][self.position[1]])

            self.output = []

            result = self.cpu.run()
            if result == 200:
                self.output.append(self.cpu.getOutput())
            else:
                return

            result = self.cpu.run()
            if result == 200:
                self.output.append(self.cpu.getOutput())
            else:
                return
                
            hullmap[self.position[0]][self.position[1]] = self.output[0]
            if paintmap[self.position[0]][self.position[1]] == 0:
                paintmap[self.position[0]][self.position[1]] = 1
                self.tilesPainted += 1
                    
            rotation_order = self.output[1]
            if rotation_order == 0:
                self.rotation -= 1
            elif rotation_order == 1:
                self.rotation += 1
            else:
                print("Something is wrong...with rotation")

            self.rotation %= 4

            if self.rotation == 0:
                self.position[1] += 1
            elif self.rotation == 1:
                self.position[0] += 1            
            elif self.rotation == 2:
                self.position[1] -= 1
            elif self.rotation == 3:
                self.position[0] -= 1
            else:
                print("Something is wrong...with movement")

            #print(self.position[0], self.position[1])
            #print("Painted " + str(self.tilesPainted) + " so far.")
