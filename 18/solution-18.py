import sys
f = open("18/input.txt", "r")
CUBES = set()
minX, minY, minZ = sys.maxsize, sys.maxsize, sys.maxsize
maxX, maxY, maxZ = 0, 0, 0

for line in f:
    line = line.strip()
    [x, y, z] = [int(i) for i in line.split(",")]
    minX = min(minX, x)
    minY = min(minY, y)
    minZ = min(minZ, z)
    maxX = max(maxX, x)
    maxY = max(maxY, y)
    maxZ = max(maxZ, z)
    CUBES.add((x,y,z))

def checkSides(x, y, z, cubes): 
    s = 6
    if (x + 1, y,z) in cubes:
        s -= 1
    if (x -1 , y, z) in cubes:
        s -= 1
    if (x, y +1 , z) in cubes:
        s -= 1
    if (x, y -1, z) in cubes:
        s -=1
    if (x, y, z -1 ) in cubes:
        s -= 1
    if (x, y, z + 1) in cubes:
        s -= 1
    return s

def getSurfaceArea(cubes):
    sides = 0
    for (x,y,z) in cubes:
        sides += checkSides(x,y,z, cubes)
    return sides

def getUncoveredSides(x,y,z, cubes):
    sides = []
    adjacents = [(x + 1, y,z), (x -1 , y, z), (x, y +1 , z),(x, y -1, z), (x, y, z -1 ),  (x, y, z + 1)]
    for adj in adjacents:
        if adj not in cubes:
            sides.append(adj)
    return sides

def isAirBubble(sides, cubes):
    for s in sides:
        if s not in cubes:
            return False
    return True

def getNeighbors(x,y ,z, cubes, neighbors):
    neighbors.add((x,y,z))
    adjacents = [(x + 1, y,z), (x -1 , y, z), (x, y +1 , z),(x, y -1, z), (x, y, z -1 ),  (x, y, z + 1)]
    for adj in adjacents:
        if adj in cubes:
            neighbors.add(adj)
            cubes.remove(adj)
            getNeighbors(adj[0], adj[1], adj[2], cubes, neighbors)

def getAirCube(cubes):
    airSides = 0
    # get the air cubes
    aircubes = set()
    
    for (x,y,z) in cubes:
        adjacents = [(x + 1, y,z), (x -1 , y, z), (x, y +1 , z),(x, y -1, z), (x, y, z -1 ),  (x, y, z + 1)]
        for adj in adjacents:
            if adj not in cubes:
                aircubes.add((adj[0], adj[1], adj[2]))
    # put air cubes next to each other in group       
    groups = []
    while(len(aircubes)):
        neighbors = set()
        (x,y,z) = aircubes.pop()
        getNeighbors(x,y,z, aircubes, neighbors)
        groups.append(neighbors)
    # for g in groups:
    #     print(g)
    # get sides that is not coverered by other air cubes in the group:
    sidesGroups = []
    for group in groups:
        sidesToCheck = set()
        for (x,y,z) in group:
            sides = getUncoveredSides(x,y,z, group)
            sidesToCheck.update(sides)
        sidesGroups.append(sidesToCheck)
    rest = []
    for sideGroup in sidesGroups:
        result = isAirBubble(sideGroup, cubes)
        
        if result:
            airSides += len(sideGroup)
        else:
            rest.append(sideGroup)
    for r in rest:
        print(r)
    return airSides

def bfs(X,Y,Z, visited_all, cubes, aircubes):
    q = [(X,Y,Z)]
    visited_all.add(q[0])
    visited = set()
    visited.add(q[0]);
    isAirCube = True

    while(len(q)):
        (x,y,z) = q.pop(0)
        adjacents = [(x + 1, y,z), (x -1 , y, z), (x, y +1 , z),(x, y -1, z), (x, y, z - 1 ),  (x, y, z + 1)]
        if isAirCube:
            for adj in adjacents:
                if adj[0] < minX or adj[0] > maxX or adj[1] < minY or adj[1] > maxY or adj[2] < minZ or adj[2] > maxZ:
                    isAirCube = False
                    break
        for adj in adjacents:
            if adj not in cubes and adj not in visited_all and adj[0] >= minX and adj[0] <= maxX and adj[1] >= minY and adj[1] <= maxY and adj[2] >= minZ and adj[2] <= maxZ:
                visited_all.add(adj)
                visited.add(adj)
                q.append(adj)

    if isAirCube:
        for xyz in visited:
            aircubes.add(xyz)

def checkSides2(x, y, z, cubes, airCubes): 
    s = 6
    if (x + 1, y,z) in cubes or  (x + 1, y,z) in airCubes:
        s -= 1
    if (x -1 , y, z) in cubes or (x -1 , y, z) in airCubes:
        s -= 1
    if (x, y +1 , z) in cubes or (x, y +1 , z) in airCubes:
        s -= 1
    if (x, y -1, z) in cubes or  (x, y -1, z) in airCubes:
        s -=1
    if (x, y, z -1 ) in cubes or (x, y, z -1 ) in airCubes:
        s -= 1
    if (x, y, z + 1) in cubes or (x, y, z + 1) in airCubes:
        s -= 1
    return s

def getSurfaceArea2(cubes, airCubes):
    sides = 0
    for (x,y,z) in cubes:
        sides += checkSides2(x,y,z, cubes, airCubes)
    return sides

def getAirCubes(cubes):
    visited = set()
    aircubes = set()
    for x in range(minX, maxX + 1):
        for y in range(minY, maxY + 1):
            for z in range(minZ, maxZ + 1):
                if (x,y,z) not in visited and (x,y,z) not in cubes: 
                    bfs(x,y,z, visited, cubes, aircubes)
    print(getSurfaceArea2(cubes, aircubes))

#airSides = getAirCube(CUBES)
#surfaceSide = getSurfaceArea(CUBES)
#print(surfaceSide, airSides)
#print( surfaceSide - airSides)

getAirCubes(CUBES)