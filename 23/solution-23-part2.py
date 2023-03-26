import sys

NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3

f = open("23/input.txt")
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
def getOrder(priority, nbrOfDirections):
    p = priority
    order = []
    for i in range(nbrOfDirections):
        if p >= nbrOfDirections:
            p = p % nbrOfDirections
        order.append(p)
        p += 1
    return order

def getConsiderations(pos, order):   
    (r, c) = pos
                        #       N           NE              NW                      S               SE              SW                      W           NW              SW                      E           NE              SE          
    directions = [(NORTH, [(r - 1, c), (r - 1, c + 1), (r - 1, c- 1)]), (SOUTH, [(r + 1, c), (r + 1, c + 1),(r + 1, c - 1)]), (WEST, [(r, c - 1),  (r - 1, c - 1),(r + 1, c - 1)]), (EAST, [(r, c + 1), (r - 1, c + 1),(r + 1, c + 1)])]
    result = []
    for idx in order:
        result.append(directions[idx])
    return result


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
def getAdjcentElves(pos, elfPositions):
    (r, c) = pos 
    #                   N           NE              E           SE              S               SW          W           NW
    directions = [(r - 1, c), (r - 1, c + 1), (r, c + 1), (r + 1, c + 1),   (r + 1, c), (r + 1, c - 1), (r, c - 1), (r - 1, c- 1)]
    elfPos = set()
    for dir in directions:
        if dir in elfPositions:
            elfPos.add(dir)
    return elfPos

def getAdjcentElvesIdx(pos, elfPositions):
    (r, c) = pos 
    #                   N           NE              E           SE              S               SW          W           NW
    directions = [(r - 1, c), (r - 1, c + 1), (r, c + 1), (r + 1, c + 1),   (r + 1, c), (r + 1, c - 1), (r, c - 1), (r - 1, c- 1)]
    elfPos = set()
    for dir in directions:
        try:
            idx = elfPositions.index(dir)
            elfPos.add(idx)
        except ValueError:
            continue
    return elfPos

def hasAdjcentElf(pos, elfPositions):
    (r, c) = pos 
    #                   N           NE              E           SE              S               SW          W           NW
    directions = [(r - 1, c), (r - 1, c + 1), (r, c + 1), (r + 1, c + 1),   (r + 1, c), (r + 1, c - 1), (r, c - 1), (r - 1, c- 1)]
    for dir in directions:
        if dir in elfPositions:
            return True
    return False

def proposeNewPosition(pos, elfPositions, order):
    elfPos = getAdjcentElves(pos, elfPositions)
    if len(elfPos) ==  0:
        return pos
        
    considerationOrder = getConsiderations(pos, order)
    for (dir, consideration) in considerationOrder:
        if isEmptyPositions(consideration, elfPos):
            return getNewPostion(pos, dir)
    return pos

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
    priority = NORTH
    round = 1
    checkList = set([i for i in range(len(elfPositions))])
    while True:
        # print("round", round - 1)
        # pic = draw(elfPositions)
        # print(pic)    
        # print("checkList", len(checkList))
        # print(checkList)
        newPostions = {}
        order = getOrder(priority, 4)
        for idx in checkList :
            pos = elfPositions[idx]
            newPos = proposeNewPosition(pos, elfPositions, order)
            if newPos == pos:
                continue
            if newPos in newPostions:
                newPostions[newPos].append(idx)
            else:
                newPostions[newPos] = [idx]
        moved = 0
        for newPos, elves in newPostions.items():
            if len(elves) < 2:
                moved += 1
                idx = elves.pop()
                elfPositions[idx] = newPos
        if moved == 0:
            return round
        
        priority += 1        
        round += 1
        if round == 10:
            print(round)
            break

elfPositions  = parse()
print("nbr of elves", len(elfPositions))
round = simulateRounds(elfPositions)
tiles = findEmptyGroundTiles(elfPositions)
print("nbr Of round", round)
pic = draw(elfPositions)
print("nbr of tiles", tiles)
print(pic)    
# how to optimze this?
#result 992