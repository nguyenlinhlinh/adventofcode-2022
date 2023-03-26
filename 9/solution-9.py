import math
f = open("9/input.txt", "r")
H = (0,0)
T = (0,0)
knots = [(0,0) for i in range(10)]
positions = set()
def goRight(H):
    [x, y] = H
    return(x+1, y)

def goLeft(H):
    [x, y] = H
    return(x-1, y)
def goUp(H):
    [x, y] = H
    return(x, y + 1)
def goDown(H):
    [x, y] = H
    return(x, y - 1)
    
def distance(H, T):
    return pow(H[0] - T[0], 2) + pow(H[1] - T[1], 2)

def move(direction, H):
    if direction == "R":
        return goRight(H)
    if direction == "L":
        return goLeft(H)
    if direction == "D":
        return goDown(H)
    if direction == "U":
        return goUp(H)
    if direction == "RU":
        N = goRight(H)
        return goUp(N)
    if direction == "RD":
        N = goRight(H)
        return goDown(N)
    if direction == "LU":
        N = goLeft(H)
        return goUp(N)
    if direction == "LD":
        N = goLeft(H)
        return goDown(N)
    return H
def getDirection(H, T):
    if H[0] == T[0] and H[1] > T[1]:
        return "U"
    if H[0] == T[0] and H[1] < T[1]:
        return "D"
    if H[0] > T[0] and H[1] == T[1]:
        return "R"
    if H[0] < T[0] and H[1] == T[1]:
        return "L"
    if H[0] > T[0] and H[1] > T[1]:
        return "RU"
    if H[0] < T[0] and H[1] > T[1]:
        return "LU"
    if H[0] < T[0] and H[1] < T[1]:
        return "LD"
    if H[0] > T[0] and H[1] < T[1]:
        return "RD"

for line in f:
    [direction, steps]= line.split(" ")
    steps = int(steps)
    for s in range(steps):
        knots[0] = move(direction, knots[0])
        for i in range(1, len(knots)):
            first = knots[i - 1]
            second = knots[i]
            if distance(first, second) > 2:
                d = getDirection(first, second)
                knots[i] = move(d, second)
        positions.add(knots[-1])
print(len(positions))
