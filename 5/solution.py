f = open("5/input.txt", "r")
lines = []
# Parse stacks
for line in f:
    lines.append(line)
    if line == "\n":
        lines.pop() # remove new line
        idxLine = lines.pop()
        indexes = []
        for i in range(len(idxLine)):
            if idxLine[i].isnumeric():
                indexes.append(i)
        nbrOfStacks = len(indexes)
        stacks = [[] for i in range(nbrOfStacks)]
        while len(lines) > 0:
            l = lines.pop()
            for i in range(nbrOfStacks):
                if l[indexes[i]].isalpha():
                    stacks[i].append(l[indexes[i]])
        break 
# Parse moves part 1
moveIdx = 1
fromIdx = 3
toIdx = 5
# for line in f:
#     line = line.strip().split(" ")
#     for i in range(int(line[moveIdx])):
#         crate = stacks[int(line[fromIdx]) - 1].pop()
#         stacks[int(line[toIdx]) - 1].append(crate)
# result = "".join([i.pop() for i in stacks])
# print(result)

# def printStacks(stacks):
#     for i in range(len(stacks)):
#         print(i+1, stacks[i])
# Parse moves part 2
# printStacks(stacks)
for line in f:
    line = line.strip().split(" ")
    nbrOfCrates = - int(line[moveIdx])
    crates = stacks[int(line[fromIdx]) - 1][nbrOfCrates:]
    del stacks[int(line[fromIdx]) - 1][nbrOfCrates:]
    stacks[int(line[toIdx]) - 1] += crates
result = "".join([i.pop() for i in stacks])
print(result)