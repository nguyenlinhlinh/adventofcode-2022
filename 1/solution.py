f= open("1/input-simple.txt", "r")
counter = 0
sum = 0
elf = 0
maxCal = 0
result = [0]
for line in f:
    if line == "\n":
        counter+=1
        result.append(0)
    else:
        result[counter] += int(line)
result.sort(reverse=True)
sum = 0
for i in range(0,3):
    sum+=result[i]
print(sum )