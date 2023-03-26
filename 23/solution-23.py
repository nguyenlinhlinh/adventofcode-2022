import sys

NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3

f = open("23/input-simple.txt")
def parse():
    elfPositions = []
    row = 0
    for line in f:
        line = line.strip()
        for c in range(len(line)):
            if line[c] == "#":
                elfPositions.append((row, c)) 
        row += 1
    return elfPositions

def getConsiderationOrder(pos, direction):   
    (r, c) = pos
                        #       N           NE              NW                      S               SE              SW                      W           NW              SW                      E           NE              SE          
    directions = [(NORTH, [(r - 1, c), (r - 1, c + 1), (r - 1, c- 1)]), (SOUTH, [(r + 1, c), (r + 1, c + 1),(r + 1, c - 1)]), (WEST, [(r, c - 1),  (r - 1, c - 1),(r + 1, c - 1)]), (EAST, [(r, c + 1), (r - 1, c + 1),(r + 1, c + 1)])]
    length = len(directions)
    order = []
    p = direction
    for i in range(length):
        if p >= length:
            p = p % length
        order.append(directions[p])
        p += 1
    return order

def getNewPostion(currentPos, direction):
    (r, c) = currentPos
    if direction == NORTH:
        return (r - 1, c)
    if direction == SOUTH:
        return (r + 1, c)
    if direction == WEST:
        return (r, c - 1)
    if direction == EAST:
        return (r, c + 1)
def isEmptyPositions(directions, elfPositions):
    for dir in directions:
        (r, c) = dir
        if (r, c) in elfPositions:
            return False
    return True

def proposeNewPosition(pos, elfPositions, priority):
    (r, c) = pos    
    #                   N           NE              E           SE              S               SW          W           NW
    directions = [(r - 1, c), (r - 1, c + 1), (r, c + 1), (r + 1, c + 1),   (r + 1, c), (r + 1, c - 1), (r, c - 1), (r - 1, c- 1)]
    if isEmptyPositions(directions, elfPositions):
        # priorities[elvesIdx] = priorities[elvesIdx] + 1
        return (r, c)
        
    considerationOrder = getConsiderationOrder((r, c), priority)
    for (dir, consideration) in considerationOrder:
        if isEmptyPositions(consideration, elfPositions):
            # priorities[elvesIdx] = dir + 1
            return getNewPostion(pos, dir)

def findMinMax(elfPositions):
    minR = sys.maxsize
    maxR = - sys.maxsize
    minC = sys.maxsize
    maxC = - sys.maxsize
    for (r, c) in elfPositions:
        minR = min(r, minR)
        maxR = max(r, maxR)
        minC = min(c, minC)
        maxC = max(c, maxC)
    return(minR, maxR, minC, maxC)

def findEmptyGroundTiles(elfPositions):
    (minR, maxR, minC, maxC) = findMinMax(elfPositions)
    tiles = 0
    for r in range(minR, maxR+1):
        for c in range(minC, maxC+1):
            if (r,c) not in elfPositions:
                tiles += 1
    return tiles

def draw(elfPositions):
    (minR, maxR, minC, maxC) = findMinMax(elfPositions)
    result = ""
    for r in range(minR, maxR + 1):
        for c in range(minC, maxC + 1):
            if (r,c) not in elfPositions:
                result += "."
            else:
                result += "#"
        result += "\n"
    return result

def simulateRounds(elfPositions):
    # priorities = [NORTH for i in range(len(elfPositions))]
    priority = NORTH
    # print ("Round", 0)
    # print(draw(elfPositions))
    for round in range(0, 10):
        print("round", round, elfPositions)
        newPostions = {}
        for i in range(len(elfPositions)):
            (r, c) = elfPositions[i]
            newPos = proposeNewPosition((r,c), elfPositions, priority)
            if newPos == elfPositions[i]:
                continue
            if newPos in newPostions:
                newPostions[newPos].append((r,c))
            else:
                newPostions[newPos] = [(r,c)]
        moved = []
        for newPos, elves in newPostions.items():
            if len(elves) < 2:
                idx = elfPositions.index(elves[0])
                elfPositions[idx] = newPos
                moved.append(newPos)
        if len(moved) == 0:
            print("no move round", round)
            return
        priority += 1
        # print ("Round", round + 1)
        # print(draw(elfPositions))
        # print("priorities", priority)


elfPositions  = parse()
print("nbr of elves", len(elfPositions))

simulateRounds(elfPositions)
tiles = findEmptyGroundTiles(elfPositions)
pic = draw(elfPositions)
print("nbr of tiles", tiles)
print(pic)    

