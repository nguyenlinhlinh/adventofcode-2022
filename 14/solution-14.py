import heapq
f =  open("14/input.txt", "r")
def parse():
    points = {}
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
                            points[x].append(y)
                    else:
                        points[x] = [y]
    for k, v in points.items():
        v.sort()
    return points

def isBlocked(pos, blockers):
    x, y = pos
    if x in blockers and y in blockers[x]:
        return True
        
    return False

def simulateSandFallDown(pos, blockers):
    
    (x,y) = pos
    print("Start", x,y)
    while True:
        print("HERE", x,y)
        # fall forever
        if x == 502:
            print("502", blockers[x])
        if x not in blockers:
            return None
        foundBlocker = False
        for n in blockers[x]:
            if n >= y:
                y = n - 1
                foundBlocker = True
                break
        if not foundBlocker:
            return None
        down = (x, y + 1)
        left = (x - 1, y + 1)
        right = (x+1, y + 1)
        # fall down
        if not isBlocked(down, blockers):
            (x, y) = down
        # fall left
        elif not isBlocked(left, blockers):
            (x, y) = left
        # fall right
        elif not isBlocked(right, blockers):
            (x,y) = right
        # rest
        else:
            return (x,y)

def pouringSand(blockers):
    i = 0
    while True:
        print("pouringSand", i)
        x = 500
        y = blockers[500][0] - 1
        rest = simulateSandFallDown((x,y), blockers)
        print(i, rest)
        if rest:
            (x,y) = rest
            if x in blockers:
                blockers[x].append(y)
                blockers[x].sort()
            else:
                blockers[x] = [y]
        else:
            print ("falling endless", i)
            return i
        i += 1



p = parse()
pouringSand(p)
# for x in p:
#     for y in p[x]:
#         print(x, y)
# print(p)

# answer 665