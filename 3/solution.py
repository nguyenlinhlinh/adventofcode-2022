f = open("3/input.txt", "r")
# part 1
# sum = 0
# for line in f:
#     idx = len(line)//2
#     first = set(sorted(line[:idx]))
#     second = set(sorted(line[idx: -1]))
#     result = []
#     for char in first:
#         if char in second:
#             result.append(char)
#     for char in result:
#         priority = ord(char)
#         p = 0
#         if priority >= 97:
#             p = priority - 96
#         else:
#             p = priority - 38
#         print(char, p)
#         sum += p
# print (sum)

# part 2
counter = 0
sets = []
sum = 0
for line in f:
    sack = line.strip()
    sets.append(set(sack))
    if len(sets) == 3:
        result = sets[0].intersection(sets[1], sets[2])
        print(result)
        for char in result:
            priority = ord(char)
            p = 0
            if priority >= 97:
                p = priority - 96
            else:
                p = priority - 38
            sum += p
        sets = []
        
print(sum)