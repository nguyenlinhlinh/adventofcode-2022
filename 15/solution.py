f = open("15/input.txt", "r")
maxX = 0
maxY = 0
minX = 0
minY = 0
sensors = []
beacons = []
for line in f:
    line = line.strip().split(" ")
    sX = int(line[2].replace(",","").split("=")[1])
    sY = int(line[3].replace(":","").split("=")[1])
    bX = int(line[8].replace(",","").split("=")[1])
    bY = int(line[9].replace(",","").split("=")[1])
    distance = abs(bX - sX) + abs(bY - sY)
    sensors.append((sX,sY, distance))
    if (bX,bY) not in beacons:
        beacons.append((bX,bY))
    maxX = max([maxX, sX, bX])
    maxY = max([maxY, sY, bY])
    minX = min([minX, sX, bX])
    minY = min([minY, sY, bY])


print("sensors", len(sensors))

def getInRow(Y):
    inRow = []
    for b in beacons:
        (x, y) = b
        if y == Y:
            inRow.append((x,y))
    return inRow

def getCheckSensors(Y):
    checkSensors = []
    for s in sensors:
        (x,y,d) = s
        distance = abs(y - Y)
        if distance <= d:
            checkSensors.append(s)
    return checkSensors

# part 1
def countImpossiblePositions(Y):
    inRow = getInRow()
    checkSensors = getCheckSensors()
    positions = 0
    for s in checkSensors:
        (x,y,d) = s
        minX = min(minX,x - d)
        maxX = max(maxX,x + d)

    for X in range(minX, maxX + 1):
        if (X,Y) in inRow:
            continue
        for sensor in checkSensors:
            (x,y,d) = sensor
            distance = abs(X - x) + abs(Y - y)
            if distance <= d:
                positions +=1
                break
    return positions

# part2
searchRange = 4000000
def limitSearchRange():
    minX = searchRange
    minY = searchRange
    maxX = 0
    maxY = 0
    for s in sensors:
        (x, y, d) = s
        maxX = max(maxX, x)
        maxY = max(maxY, y)
        minX = min(minX, x)
        minY = min(minY, y)
    #return (minX, minY, maxX, maxY)
    return (0, 0, 4000000, 4000000)

def findBeacon():
    (minX, minY, maxX, maxY) = limitSearchRange()
    print("range", minX, maxX,minY, maxY)
    for Y in range(minY, maxY + 1):
        checkSensors = getCheckSensors(Y)
        inRow = getInRow(Y)
        # print("checkSensors", len(checkSensors))
        # print("inRow", len(inRow))
        X = minX

        if Y % 100000 == 0:
            print(Y)

        while X < maxX + 1:
            if (X,Y) in inRow:
                continue
            detected = False
            for sensor in checkSensors:
                (x,y,d) = sensor
                distance = abs(X - x) + abs(Y - y)
                if distance <= d:
                    detected = True
                    #print(X, Y, sensor, distance)
                    #print((x - X))
                    #print("before", abs(x - X) * 2, d - distance)
                    X = X + abs(x - X) * 2 + abs(d - distance)
                    #print("after", X)
                    break
            if detected == False:
                return (X, Y)
            X = X + 1
    return None
detectedBeacon = findBeacon()

print("detected", detectedBeacon)
print(detectedBeacon[0]* 4000000 + detectedBeacon[1] )

# 4399906