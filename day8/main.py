# Day 8
from copy import copy, deepcopy

print('Day 8')

class Image(object):
    def __init__(self, raw_data, width, height):
        self.raw_data = raw_data
        self.width = width
        self.height = height
        self.layer = []
        i = 0
        for layer in range(int(len(raw_img) / (width*height))):
            tmp = [[0] * width for i in range(height)]
            for row in range(height):
                for col in range(width):
                    tmp[row][col] = int(raw_img[i])                    
                    i += 1            
            self.layer.append(deepcopy(tmp))
            
    def findLayerWithLeast(self, num):
        lowscore = -1
        withLeast = -1
        for lay in range(len(self.layer)):
            count = self.countInLayer(self.layer[lay], num)
            if lowscore == -1 or count < lowscore:
                lowscore = count
                withLeast = lay
        return withLeast

    def countInLayer(self, layer, num):
        count = 0
        for row in range(self.height):
            for col in range(self.width):
                if layer[row][col] == num:
                    count += 1
        return count

    # 0 is black, 1 is white, and 2 is transparent.
    def decode(self):
        self.image = [[0] * self.width for i in range(self.height)]

        for row in range(self.height):
            for col in range(self.width):
                for lay in range(len(self.layer)):
                    if self.layer[lay][row][col] == 0: #BLACK
                        self.image[row][col] = 0
                        break;
                    if self.layer[lay][row][col] == 1: #White
                        self.image[row][col] = 1
                        break;

    def render(self):
        for row in self.image:
            tmp_row = [str(i) for i in row]
            print("".join(tmp_row))
                

def readProgramFromFile(filename):
    with open(filename, 'r') as fp:
        return fp.readline()  

raw_img = readProgramFromFile('input.txt')
#raw_img = "0222112222120000"

password = Image(raw_img, 25, 6)
password.decode()
password.render()




    
