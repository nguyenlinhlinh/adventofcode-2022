# X = 1
# addx = 2 #cycle
# noop = 1 # cycle
# f = open("10/input.txt")
# cycle = 0
# register = 1
# checkCycle = 20
# sum = 0
# for line in f:
#     line = line.strip()
#     if "addx" in line:
#         [op, val] = line.split(" ")
#         endCycle = cycle + 3
#         for c in range(cycle, endCycle):
#             if cycle == checkCycle:
#                 sum += register * cycle
#                 checkCycle += 40
#                 print(cycle, register, sum)
#             if c == endCycle - 1:
#                 register += int(val)
#                 break
#             cycle += 1
#     else:
#         if cycle == checkCycle:
#             sum += register * cycle
#             checkCycle += 40
#         cycle +=1

# print(cycle, sum)

# part 2

f = open("10/input.txt")
register = 1
sprite = 1
CTR = 0
array = [[0 for i in range(40)] for i in range(6)]
finishCycle = 0
value = 0
currentRow = -1
def getPendingAdd():
    line = f.readline().strip()
    if "addx" in line:
        [op, val] = line.split(" ")
        return int(val)
    else:
        return None

pendingAdd = None

for cycle in range(0, 240):
    if cycle % 40 == 0:
        currentRow += 1
        CTR = 0

    if  CTR >= sprite - 1 and CTR <= sprite +1:
        array[currentRow][CTR] = "#"
    else:
        array[currentRow][CTR] = "."
    CTR+=1

    print('#' + str(cycle + 1), register)

    if pendingAdd:
        register += pendingAdd
        sprite = register
        pendingAdd = None
    else:
        pendingAdd = getPendingAdd()
        print(pendingAdd)

    """
    if cycle == finishCycle:
        register += value 
        sprite = register
        #if register < 0:
        #    print("NEGATIVE", register, cycle, value)
        [c, val] = getOperation()
        finishCycle = cycle + c
        value = val
        print('#' + str(cycle + 1), register, 'END')
    """

result = ""
for r in range(6):
    for c in range(40):
        result += array[r][c]
    result += "\n"
print(array)
        

print(result)
