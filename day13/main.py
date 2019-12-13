# Day 13
from PIL import Image
import computer

print('Day 13')

class Game(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0 for x in range(width)] for y in range(height)]

        program = readProgramFromFile('input.txt')
        self.cpu = computer.ICC("day13", 10000, 0)
        self.cpu.setMemory(program)

        self.cpu.memory[0] = 2

        self.score = 0

    def setOnBoard(self, x, y, tile_id):
        self.board[x][y] = tile_id

    def getNumOf(self, tile_id):
        i = 0
        for x in range(self.width):    
            for y in range(self.height):
                if self.board[x][y] == tile_id:
                    i += 1
        return i

    def getPosOfFirst(self, tile_id):
        for x in range(self.width):    
            for y in range(self.height):
                if self.board[x][y] == tile_id:
                    return [x, y]

    def run(self):
        output = []
        gameover = False
        while not gameover:
            
            result = self.cpu.run()
            if result == 100: #Input
                paddle = self.getPosOfFirst(3)
                ball = self.getPosOfFirst(4)
                if paddle and ball and paddle[0] > ball[0]:
                    self.cpu.setInput(-1)
                elif paddle and ball and paddle[0] < ball[0]:
                    self.cpu.setInput(1)
                elif paddle and ball:
                    self.cpu.setInput(0)
            elif result == 200: #Output
                output.append(self.cpu.getOutput())
                if len(output) == 3:
                    if output[0] == -1: #score
                        self.score = output[2]
                        print(self.score)
                    else:
                        arcadegame.setOnBoard(output[0], output[1], output[2])
                    output = []                                        
            elif result == 0 or self.getNumOf(2) == 0: #Done
                gameover = True
            
            
    def show(self):
        img = Image.new( 'RGB', (self.width, self.height), "black")

        pixels = img.load()

        for i in range(self.width):    
            for j in range(self.height):  
                if self.board[j][i]:
                    pixels[j,i] = (i, j, 255) 

        img.show()         
        

def readProgramFromFile(filename):
    with open(filename, 'r') as fp:
        line = fp.readline().strip().split(',')        
        return [int(x) for x in line]

arcadegame = Game(40, 40)
arcadegame.run()
        
#arcadegame.show()
