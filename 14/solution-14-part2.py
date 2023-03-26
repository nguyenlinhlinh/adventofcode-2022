import heapq
f =  open("14/input.txt", "r")
def parse():
    points = {}
    maxY = 0
    for line in f:
        line = line.strip().split("->")
        for i in range(1, len(line)):
            [x1, y1] = [ int(char.strip()) for char in line[i - 1].split(",")]
            x2, y2 = [ int(char.strip()) for char in line[i].split(",")]
            X = sorted([x1,x2])
            Y = sorted([y1,y2])
            for x in range(X[0], X[1] + 1):
                for y in range(Y[0], Y[1]+ 1):
                    if x in points:
                        if y not in points[x]:
                            maxY = max(y, maxY)
                            points[x].append(y)
                    else:
                        points[x] = [y]
    floor = maxY + 2
    for k, v in points.items():
        v.append(floor)
        v.sort()
    return points, floor

def isBlocked(pos, floor, blockers):
    x, y = pos
    if x not in blockers and y == floor:
        return True
    if x in blockers and y in blockers[x]:
        return True
        
    return False

def simulateSandFallDown(pos, floor, blockers):    
    (x,y) = pos
    while True:
        # fall forever
        if x not in blockers:
            y = floor - 1
        else:
            for n in blockers[x]:
                if n >= y:
                    y = n - 1
                    break
        down = (x, y + 1)
        left = (x - 1, y + 1)
        right = (x+1, y + 1)
        # fall down
        if not isBlocked(down, floor, blockers):
            (x, y) = down
        # fall left
        elif not isBlocked(left, floor, blockers):
            (x, y) = left
        # fall right
        elif not isBlocked(right, floor, blockers):
            (x,y) = right
        # rest
        else:
            return (x,y)

def pouringSand(blockers, floor):
    i = 1
    while True:
        print("pouringSand", i)
        x = 500
        y = blockers[500][0] - 1
        rest = simulateSandFallDown((x,y), floor, blockers)
        print(i, rest)
        if rest == (500, 0):
            print("Blocked", i)
            return i
        (x,y) = rest
        if x in blockers:
            blockers[x].append(y)
            blockers[x].sort()
        else:
            blockers[x] = [y, floor]
        i += 1



p, floor = parse()
pouringSand(p, floor)
# for x in p:
#     for y in p[x]:
#         print(x, y)
# print(p)

#answer 25434