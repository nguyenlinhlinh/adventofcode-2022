import sys
import heapq
f = open("24/input-simple2.txt", "r")
def parse():
    start = (0,1)
    blizzards = {}
    row = 1
    col = len(f.readline().strip())
    for line in f:
        for c in range(col):
            char = line[c]
            if char != "#" and char != ".":
                blizzards[(row, c)] = [char]
        row += 1
    end = (row - 1, col - 2)
    return start, end, blizzards, row, col

def move(blizzard, row, col):
    (r, c, direction) = blizzard 
    if direction == ">":
        c += 1
        if c >= col - 1:
            c = 1
    elif direction == "<":
        c -= 1
        if c <= 0:
            c = col - 2
    elif direction == "^":
        r -= 1
        if r <= 0:
            r = row - 2
    else:
        r += 1
        if r >= row - 1:
            r = 1
    return (r,c)

def simulateBlizzardMovement(blizzards, row, col):
    newPositions = {}
    for position, directions in blizzards.items():
        (r, c) = position
        for dir in directions:
            (newR, newC)= move((r,c,dir), row, col)
            if (newR, newC) in newPositions:
                newPositions[(newR, newC)].append(dir)
            else:
                newPositions[(newR, newC)] = [dir]
    return newPositions

def getAvailablePositions(position, row, col, blizzards, start, end):
    positions = []
    (r,c) = position
    directions = [(r - 1, c),(r + 1, c), (r, c - 1), (r, c + 1)]
    for pos in directions:
        if pos == start or pos == end:
            if pos == end:
                print("here")
            positions.append(pos)
            continue
        if (pos[0] <= 0 or pos[0] >= row - 1 or pos[1] <= 0 or pos[1] >= col - 1):
            continue
        if pos in blizzards:
            continue
        positions.append(pos)
    return positions

def isSameState(initialState, currentState):
    for pos, blizzards in initialState.items():
        if pos not in currentState:
            return False
        b = currentState[pos]
        for i in range(len(blizzards)):
            if blizzards[i] != b[i]:
                return False
    return True

def printState(row, col, state, pos, start, end):
    result = ""
    for r in range(row):
        for c in range(col):
            if (r,c) == pos:
                result += "E"
                continue
            if (r,c) == start or (r,c) == end:
                result += "."
                continue
            if r == 0 or c == 0 or r == row - 1 or c == col - 1:
                result += "#"
                continue
            if (r, c) in state:
                b = state[(r,c)]
                if len(b) > 1:
                    result += str(len(b))
                else:
                    result += b[0]
                continue
            result += "."
        result += "\n"
    return result


def getStates(initialState, row, col):
    states = [initialState]
    # print("state 0", printState(row, col,  initialState))
    currentState = simulateBlizzardMovement(initialState, row, col)
    while not isSameState(initialState, currentState):
        # print("state", counter, printState(row, col,  currentState))
        states.append(currentState)
        currentState = simulateBlizzardMovement(currentState, row, col)
    return states



def bfs(start, end, blizzards, row, col):
    states = getStates(blizzards, row, col)
    nbrOfStates = len(states)
    prev = {(start[0], start[1], 0): None} 
    q = [(start[0], start[1], 0)]
    # visited when position and state is same
    visited = set()
    while len(q):
        (r,c, minutes) = q.pop(0)
        visited.add((r,c, minutes%nbrOfStates))
        if (r,c) == end:
            return minutes, states[minutes%len(states)]
        stateIdx = (minutes + 1) % nbrOfStates
        state = states[stateIdx]
        positions = getAvailablePositions((r,c), row, col, state , start, end)
        for pos in positions:
            if not (pos[0], pos[1], stateIdx) in visited:
                q.append((pos[0], pos[1], minutes + 1))
                prev[(pos[0], pos[1], minutes + 1)] = (r,c, minutes)
                visited.add((pos[0], pos[1], stateIdx))

        if (r,c) not in state:
            if not ((r,c),stateIdx) in visited:
                q.append((r,c, minutes + 1))
                prev[(r,c, minutes + 1)] = (r,c, minutes)
                visited.add((r,c, stateIdx))

start, end, blizzards, row, col = parse()
minutes1, state1 = bfs(start, end, blizzards, row, col )
print(minutes1)
print(printState(row, col, state1, end, start, end))
minutes2, state2 = bfs(end, start, state1, row, col )
# print(minutes2)
# minutes3, state3 = bfs(start, end, state2, row, col)
# print(minutes1 + minutes2 + minutes3)
# states = getStates(blizzards, row, col)
# print("States", len(states))
# for i in range(len(states)):
#     print("state", i)
#     print(printState(row, col, states[i], start, start, end))
# print("*****")
# curr = (end[0], end[1], minutes)
# stack = [curr]
# while curr:
#     stack.append(prev[curr])
#     curr = prev[curr]
# counter = 0
# while len(stack):
#     p = stack.pop(len(stack) - 1)
#     print("p",p)
#     if p:
#         (r, c, m) = p
#         print("minute", m)
#         print(printState(row, col, states[m% len(states)],(r,c),start, end))
#     counter += 1
