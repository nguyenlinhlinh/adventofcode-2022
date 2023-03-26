import math
import copy
import sys

CASES = {"0":0, "1":1, "2":2, "=": -2, "-": -1}
f = open("25/input.txt", "r")

def convertToDecimal(string):
    sum = 0
    x = len(string) - 1
    for char in string:
        place = math.pow(5, x)
        if char.isnumeric():
            sum += int(char) * place
        elif char == "=":
            sum += -2 * place
        elif char == "-":
            sum += -1 * place
        x-=1
    return int(sum)

# 976 / 5 = 195 rest 1
# 195/5 = 39 rest 0
# 39/5 = 7 rest 4
# 7/5 = 1 rest = 2
# 1/5 = 0 rest = 1

def convertToSnafu(number):
    if number == 0:
        return 0
    
    divisor = 5
    d = number
    x = -1
    while d > 0:
        d = d // divisor
        x += 1
    if math.pow(5,x) < number and 2*math.pow(5,x) < number:
        x+=1
    cases = {"0":0,"1":1, "2":2}
    result = ""
    currNbr = 0
    while x >= 0:
        key = ""
        minGap = sys.maxsize
        newPlace = 0
        p = math.pow(5, x)
        for k, v in cases.items():
            n = currNbr + v*p
            rest = abs(number - n)
            if rest < minGap:
                minGap = rest
                key = k
                newPlace = v * p

        result += key
        currNbr += newPlace
        x -= 1
        cases = CASES
    return result
tempIndecimal = 0
for line in f:
    line = line.strip()
    tempIndecimal += convertToDecimal(line)
print(tempIndecimal)
print("snafu", convertToSnafu(tempIndecimal))