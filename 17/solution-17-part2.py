WIDTH = 7
LEFT = -1
RIGHT = 1

def pushRock(direction, rock, chamber):
    offset = LEFT if direction == "<" else RIGHT
    pushedRock = []
    for (x, y) in rock:
        newX = x + offset
        if newX < 1 or newX > WIDTH:
            return rock
        if y in chamber[newX]:
            return rock
        pushedRock.append((newX, y))
    return pushedRock

def fallOneUnit(rock, chamber):
    newRockPos = []
    for (x,y) in rock:
        newY = y - 1
        # rock comes to rest
        if newY in chamber[x] or newY == 0:
            return (rock, True)
        newRockPos.append((x, newY))
    return (newRockPos, False)


def getHeight(chamber):
    height = 0
    for k, v in chamber.items():
        if len(v) > 0:
            height = max(height, v[len(v) - 1])
    return height

def getRock(idx, height):
    idx = idx % 5
    if idx == 0:
        # rock -
        return [(3,height), (4,height), (5,height), (6,height)]
    if idx == 1:
        # rock +
        return [(4,height), (3,height + 1),(4,height + 1),(5, height + 1), (4,height + 2)]
    if idx == 2:
        # rock _|
        return [(3,height), (4,height),(5,height), (5,height + 1), (5,height + 2)]
    if idx == 3:
        # rock |
        return [(3,height), (3,height + 1), (3,height + 2 ), (3,height + 3)]
    if idx == 4:
        # rock []
        return [(3,height), (4,height), (3,height + 1), (4,height + 1)]


def simulateRockFalling(jetPattern):
    chamber = {i: [] for i in range(1, WIDTH + 1)}
    height = 0
    idx = 0
    for i in range(20000):
        rock = getRock(i, height + 4)
        while True:
            direction = jetPattern[idx]
            # Push rock
            rock = pushRock(direction, rock, chamber)
            
            # Fall one unit
            (rock, rest)= fallOneUnit(rock,chamber)
            idx = (idx + 1) % len(jetPattern)

            # come to rest
            if rest:
                for (x, y) in rock:
                    chamber[x].append(y)
                    chamber[x].sort()
                    # set new height
                height = getHeight(chamber)
                break
                    
    return height

f = open("17/input-simple.txt", "r")
jetPattern = f.readline().strip()
h = simulateRockFalling(jetPattern)
print("height", h)
# answer 3200
30288 