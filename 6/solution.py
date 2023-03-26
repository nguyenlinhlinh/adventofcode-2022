f = open("6/input.txt")

for line in f:
    array = []
    for i in range(len(line)):
        char = line[i]
        if len(array) == 0:
            array.append(char)
        else:
            for j in range(len(array)):
                if(array[j] == char):
                    array = array[j+1:]
                    break
            array.append(char)

        if len(array) == 14:
            print(i + 1, array)
            break