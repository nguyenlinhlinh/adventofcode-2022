RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
NBR_OF_DIRECTIONS = 4

def rotateRight(m):
    n = []
    for c in range(0, len(m[0])):
        temp = []
        for r in range(len(m) - 1, -1, -1):
            temp.append(m[r][c])
        n.append(temp)
    return n

def rotateLeft(m):
    n = []
    for c in range(len(m) - 1, -1, -1):
        temp = []
        for r in range(0, len(m[0])):
            temp.append(m[r][c])
        n.append(temp)
    return n


CUBE_SIDES_VERTICAL =   [[2,1,2],
                        [3,3,3],
                        [4,5,4], 
                        [6,6,6]]

# follow the order of CUBE_SIDES_VERTICAL
ROTATE_FUNCTIONS_VERTICAL=   [[None,  None,             None],
                              [(rotateLeft,1),    None,             (rotateLeft,1)],
                              [None,              None,             None], 
                              [None,              (rotateLeft, 1), None]]

                            #   2                    3                      4                    6
ROTATE_FACINGS_VERTICAL = [[{UP: UP, DOWN: DOWN}, {UP:  RIGHT, DOWN: LEFT}, {UP:UP, DOWN: DOWN}, {UP: UP, DOWN: DOWN}],
                            #   1                    3                      5                    6 
                            [{UP: UP, DOWN:DOWN}, {UP: UP, DOWN: DOWN}, {UP: UP, DOWN:DOWN}, {DOWN:LEFT, UP: RIGHT}],
                            #   2                 3                     4                  6           
                            [{DOWN: DOWN, UP: UP},{DOWN: LEFT, UP: RIGHT},{DOWN:DOWN, UP: UP},{DOWN: DOWN, UP:UP}]]


CUBE_SIDES_HORIZONTAL = [[4,1,2,5],
                        [4,3, 2,6],
                        [4,5,2,1],
                        [6,5,3,1]]
                            #4                              1                           2,                          5
ROTATE_FACINGS_HORIZONTAL = [[{LEFT: RIGHT, RIGHT: LEFT}, {LEFT:  LEFT, RIGHT: RIGHT}, {LEFT:LEFT, RIGHT:RIGHT}, {LEFT: RIGHT, RIGHT: LEFT}],
                            #4                       3                            2                         6
                            [{LEFT: DOWN, RIGHT:UP}, {RIGHT: RIGHT, LEFT: LEFT}, {RIGHT: UP, LEFT:DOWN}, {RIGHT:UP, LEFT: DOWN}],
                            #4                          5                       2                          1
                            [{LEFT: LEFT, RIGHT: RIGHT},{LEFT: LEFT , RIGHT: RIGHT},{RIGHT:LEFT, LEFT: RIGHT},{RIGHT: LEFT, LEFT:RIGHT}],
                            #6                          5                           3                          1
                            [{LEFT: LEFT, RIGHT: RIGHT},{LEFT: DOWN , RIGHT: UP},{RIGHT:UP, LEFT: DOWN},{RIGHT: UP, LEFT:DOWN}]]

ROTATE_FUNCTIONS_HORIZONTAL= [[(rotateRight, 2), None, None, (rotateLeft, 2)],
                              [(rotateRight, 1), None, (rotateRight,1),(rotateRight, 1)],
                              [None, None, (rotateRight,2), (rotateRight, 2)],
                              [None, (rotateRight, 1), (rotateRight,1), (rotateRight,1)]]
                              




f = open("22/input.txt", "r")
def parseSimple(side_length):
    map = []
    maxCols = 0
    # Parse tiles
    for line in f:
        if line == "\n":
            break
        map.append([])
        cols = len(line)
        maxCols = max(maxCols, cols)
        for c in range(cols):
            char = line[c]
            if char != "\n":
                map[len(map) - 1].append(char)
    for row in map:
        row.extend([" " for i in range(maxCols - len(row))])

    # Parse instructions
    instructionStr = f.readline().strip()
    nbrStr = ""
    instructions = []
    for char in instructionStr:
        if char.isnumeric():
            nbrStr += char
            continue
      
        if nbrStr:
            instructions.append(int(nbrStr))
            nbrStr = ""
        instructions.append(char)
    if nbrStr:
        instructions.append(int(nbrStr))
    sides = {}
    sideIdx = 1
    for row in range(0,len(map), side_length):
        for col in range(0,len(map[0]), side_length):
            if map[row][col] != " ":
                sides[sideIdx] = []
                for r in range(row, row + side_length):
                    temp = []
                    for c in range(col, col + side_length):
                        temp.append((r,c, map[r][c]))
                    sides[sideIdx].append(temp)
                sideIdx += 1
    for k, v in sides.items():
        print(k)
        print(v)
    horizontal = [[0 for j in range(len(CUBE_SIDES_HORIZONTAL[0] * side_length))] for r in range(len(CUBE_SIDES_HORIZONTAL) * side_length)]
    vertical = [[0 for j in range(len(CUBE_SIDES_VERTICAL)* side_length)] for c in range(len(CUBE_SIDES_VERTICAL[0])* side_length)]
    
    rotated = [[0 for j in range(len(map[0]))] for i in range(len(map))]
    # Populate horizontal
    for row in range(0,len(map), side_length):
        for col in range(0, len(map[0]), side_length):
            sideIdx = CUBE_SIDES_HORIZONTAL[row // side_length][col // side_length]
            side = sides[sideIdx]
            rotateFunc = ROTATE_FUNCTIONS_HORIZONTAL[row // side_length][col // side_length]
            rotated = side
            if rotateFunc:
                (func, times) = rotateFunc
                for i in range(times):
                    rotated = func(rotated)
            for r in range(0, len(rotated)):
                    for c in range(0, len(rotated[0])):
                        horizontal[row + r][col + c] = rotated[r][c]
    # Rotate arcodingly
    temp = [[0 for j in range(0, len(CUBE_SIDES_VERTICAL[0]) * side_length)] for i in range(len(CUBE_SIDES_VERTICAL)* side_length)]
    for row in range(0,len(CUBE_SIDES_VERTICAL)):
        for col in range(0, len(CUBE_SIDES_VERTICAL[0])):
            sideIdx = CUBE_SIDES_VERTICAL[row][col]
            side = sides[sideIdx]
            rotateFunc = ROTATE_FUNCTIONS_VERTICAL[row][col]
            rotated = side
            if rotateFunc:
                (func, times) = rotateFunc
                for i in range(times):
                    rotated = func(rotated)
            for r in range(0, len(rotated)):
                for c in range(0, len(rotated[0])):
                    temp[row * side_length + r][col * side_length + c] = rotated[r][c]

    for col in range(len(temp[0])):
        for row in range(len(temp)):
            vertical[col][row] = temp[row][col]

    return map, horizontal, vertical, instructions


def turn(currentDirection, direction):
    if direction == "R":
        return(currentDirection + 1) % NBR_OF_DIRECTIONS
    if direction == "L":
        return (currentDirection - 1) % NBR_OF_DIRECTIONS

def move(position, facing, steps, horizontal, vertical, sideLength):
    currentIdx = 0
    map = []
    mapFacing = []
    isHorizontal = facing == LEFT or facing == RIGHT
    isVertical = facing == UP or facing == DOWN
    step = - 1 if (facing == LEFT or facing == UP) else 1

    # Horizontal move
    if isHorizontal:
        row = position[0]
        map = horizontal[row]
        mapFacing = ROTATE_FACINGS_HORIZONTAL[row // sideLength]
        for i in range(len(map)):
            if map[i][1] == position[1]:
                currentIdx = i
                break
            
    if isVertical:
        col = position[1]
        map = vertical[col]
        mapFacing = ROTATE_FACINGS_VERTICAL[col // sideLength]
        for i in range(len(map)):
            if map[i][0] == position[0]:
                currentIdx = i
                break

    while steps > 0:
        prevIdx = currentIdx
        currentIdx = (currentIdx + step) % len(map)
        if map[currentIdx][2] == "#":
            currentIdx = prevIdx
            break
        steps -= 1

    newFacing = mapFacing[currentIdx // sideLength][facing]
    return map[currentIdx], newFacing

def followInstructions(start, facing, instructions, horizontal, vertical, sideLength):
    currentPos = start
    currentFacing = facing
    for instruction in instructions:
        print("instruction", instruction)
        if isinstance(instruction, str):
            currentFacing = turn(currentFacing, instruction)
        else:
            print("before", currentPos, currentFacing, instruction)
            currentPos, currentFacing = move(currentPos, currentFacing, instruction, horizontal, vertical, sideLength)
            print("after", currentPos, currentFacing)
            print("\n")

    return currentPos, currentFacing


sideLength = 50
map, horizontal, vertical, instructions = parseSimple(sideLength)


print("HORIZONTAL")
counter = 0
for row in horizontal:
    print(row)
    counter +=1
    if counter % sideLength == 0:
        print("\n")
counter = 0
print("VERTICAL")
for row in vertical:
    print(row)
    counter +=1
    if counter % sideLength == 0:
        print("\n")

# print(instructions)
# (x, y, char) = horizontal[0][0]
# print("First Position:", (x,y,char))
(pos, facing) = followInstructions((0,50), RIGHT, instructions, horizontal, vertical, sideLength)
print(pos, facing)

print("result:", 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + facing )



# answer
# 162096