# Day 6

print('Day 6')
import copy 

class OrbitalObject(object):
    def __debugText(self, text):
        if self.debug:
            print("[" + self.name +"]: " + text)
            
    def __init__(self, name, checksum = 0, debug = 0):
        self.debug = debug
        self.name = name
        self.checksum = checksum
        self.satelites = []
        self.fucked = False
        self.__debugText("Created")  

class OrbitalTree(object):
    def __debugText(self, text):
        if self.debug:
            print("[Orbital Tree]: " + text)
            
    def __init__(self, debug = 0):
        self.debug = debug
        self.root  = OrbitalObject("COM", 0)

    def findObject(self, orbitalName, orbits):
        for o in orbits:                    
            if o.name == orbitalName:
                return o
            else:
                self.__debugText("Checking " + o.name + " orbits")
                found = self.findObject(orbitalName, o.satelites)
                if found:
                    return found
       
        return False

    def addDirectOrbitTo(self, parentName, childName):
        self.__debugText("Parent " + parentName + ", Child " + childName)
        parent = self.findObject(parentName, [self.root])
        if parent:
            child = OrbitalObject(childName, parent.checksum+1)
            parent.satelites.append(child)
            child.dad = parent
            self.__debugText("Added " + child.name + " to " + parent.name + ", now have " + str(len(parent.satelites)) + " Satelites")
            return True
        else:
            #self.__debugText("Could not find " + parentName)
            return False

    def getChecksum(self, unchecked):
        sum = 0
        for orbit in unchecked:
            sum += orbit.checksum
            sum += self.getChecksum(orbit.satelites)

        return sum

    def findSAN(self, position, cost = 0):
        print("at pos: " + position.name + " with cost " + str(cost))
        if position.name == "SAN":
            return cost
        elif not position.fucked:
            position.fucked = True
            for sat in position.satelites:
                cost += self.findSAN(sat, cost)
        else:
            self.findSAN(position.dad, cost)
            
        return cost
            
            
def readProgramFromFile(filename):
    with open(filename, 'r') as fp:
        return [x.strip().split(')') for x in fp.readlines()]

##############################################################################

orbitMap= readProgramFromFile('sample.txt')
tree = OrbitalTree(0);

while orbitMap:
    orbitsLeft = []
    for pair in orbitMap:
        if not tree.addDirectOrbitTo(pair[0], pair[1]):
            orbitsLeft.append(pair)
    orbitMap = orbitsLeft

you = tree.findObject('YOU', [tree.root])
print(tree.findSAN(you))

#print("checksum: " + str())
