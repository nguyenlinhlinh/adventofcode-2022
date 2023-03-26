import functools
import copy
f = open("13/input.txt", "r")
arrays = []
stack = []
for line in f:
    if line == '\n':
        continue
    line = line.strip()
    nbr = ""
    prev = ""
    for char in line:
        if char == "[":
            stack.append("[")
        elif char == "]":
            if nbr:
                stack.append(int(nbr))
                nbr = ""
            array = []
            while len(stack) > 0:
                e = stack.pop()
                if e == "[":
                    break
                array.insert(0, e)
            stack.append(array)
        elif char == ",":
            if prev != "]":
                stack.append(int(nbr))
                nbr = ""
        else:
            nbr += char
        prev = char
    arrays.append(stack.pop())

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
        
    if isinstance(a, list) and isinstance(b,int):
        b = [b]
    elif isinstance(a, int) and isinstance(b, list):
        a = [a]
        
    if isinstance(a, list) and isinstance(b, list):
        for i in range(len(a)):
            if i < len(b):
                aElement = a[i]
                bElement = b[i]
                result = compare(aElement, bElement)
                if result != 0:
                    return result
            else:
                break

        if len(a) == len(b):
            return 0
        if len(a) < len(b):
            return -1
        if len(a) > len(b):
            return 1
# 5169
index = 1
sum = 0
print(len(arrays))
for i in range(0, len(arrays), 2):
    first =  copy.deepcopy(arrays[i])
    second = copy.deepcopy(arrays[i+1])
    result = compare(first, second)
    if result <= 0:
        sum += index
    print(index, i, i +1)
    index += 1
arrays.append([[2]])
arrays.append([[6]])
arrays.sort(key=functools.cmp_to_key(compare))
for a in arrays:
    print(a)
print("sum", sum)
 
test = 1
for i in range(len(arrays)):
    print("print",str(arrays[i]))
    if str(arrays[i]) == "[[2]]" or str(arrays[i]) == "[[6]]":
        test *= i + 1
print(test)
