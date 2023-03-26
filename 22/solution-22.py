RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
NBR_OF_DIRECTIONS = 4

f = open("22/input.txt", "r")
def parse():
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

    horizontal = [[] for r in range(len(map))]
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] != " ":
                horizontal[row].append((row, col, map[row][col]))

    vertical = [[] for c in range(len(map[0]))]
    for col in range(len(map[0])):
        for row in range(len(map)):
            if map[row][col] != " ":
                vertical[col].append((row, col, map[row][col]))
                 
    return map, horizontal, vertical, instructions

def turn(currentDirection, direction):
    if direction == "R":
        return(currentDirection + 1) % NBR_OF_DIRECTIONS
    if direction == "L":
        return (currentDirection - 1) % NBR_OF_DIRECTIONS

def move(position, facing, steps, horizontal, vertical):
    currentIdx = 0
    map = []
    isHorizontal = facing == LEFT or facing == RIGHT
    isVertical = facing == UP or facing == DOWN
    step = - 1 if (facing == LEFT or facing == UP) else 1
    # Horizontal move
    if isHorizontal:
        row = position[0]
        map = horizontal[row]
        for i in range(len(map)):
            if map[i][1] == position[1]:
                currentIdx = i
    if isVertical:
        col = position[1]
        map = vertical[col]
        for i in range(len(map)):
            if map[i][0] == position[0]:
                currentIdx = i

    while steps > 0:
        prevIdx = currentIdx
        currentIdx = (currentIdx + step) % len(map)
        if map[currentIdx][2] == "#":
            currentIdx = prevIdx
            break
        steps -= 1
    return map[currentIdx]

def followInstructions(start, facing, instructions, horizontal, vertical):
    currentPos = start
    currentFacing = facing
    for instruction in instructions:
        if isinstance(instruction, str):
            currentFacing = turn(currentFacing, instruction)
        else:
            currentPos = move(currentPos, currentFacing, instruction, horizontal, vertical)

    return currentPos, currentFacing

map, horizontal, vertical, instructions = parse()



# print("HORIZONTAL")
# for row in horizontal:
#     print(row)

# print("VERTICAL")
# for row in vertical:
#     print(row)

print(instructions)
(x, y, char) = horizontal[0][0]
print("First Position:", (x,y,char))
(pos, facing) = followInstructions((x,y), RIGHT, instructions, horizontal, vertical)
print(pos, facing)

print("result:", 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + facing )



# answer input
# 117054