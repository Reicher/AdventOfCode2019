class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.f = 0
        self.g = 0
        self.h = 0

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self, other):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def getChildren(self, room):
        children= [ Node(self.x, self.y-1),
                    Node(self.x, self.y+1),
                    Node(self.x-1, self.y),
                    Node(self.x+1, self.y)]
        
        good_children = []
        for child in children:
            if room[child.x][child.y] != "#":
                good_children.append(child)
        return good_children

    def distance2(self, other):
        return abs(self.x - other.x) + abs(self.y + other.y)
        

def getLeastFNode(aList):
    minf = -1

    for n in aList:
        if n.f < minf or minf == -1:
            minf = n.f
            best = n
    return best

def printWay(way):
    for n in way:
        print(n.x, n.y)

# S = Start
# # = Block
# . = Visited
# D = Goal
def Astar(start, end, room):
    openList = [Node(start[0], start[1])]
    end = Node(end[0], end[1])
    closedList = []
    while openList:

        # FIND NEXT
        current = getLeastFNode(openList)
        openList.remove(current)
        closedList.append(current)        

        # FOUND END
        if current == end:
            printWay(closedList)
            return closedList

        children = current.getChildren(room)
        for child in children:
            if child in closedList:
                continue
            
            child.g = current.g + child.distance2(current)
            child.h = child.distance2(end)
            child.f = child.g + child.h

            if child in openList:
                other = next((x for x in openList if x == child), None)
                if child.g > other.g:
                    continue

            openList.append(child)
