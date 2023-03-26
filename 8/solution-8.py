f = open("8/input.txt", "r")
grid = []
for line in f:
    line = line.strip()
    r = []
    for c in line:
        r.append(int(c))
    grid.append(r)
row = len(grid)
col = len(grid[0])
nbr = row*4 - 4
print(row, col)
print(nbr)

# part 1
def getNbrOfVisibleTrees():
    for r in range(1, row - 1):
        for c in range(1, col - 1):
            # Left Right Up Down
            hide = [False, False, False, False]
            currTree = grid[r][c]
            index = 0
            # check row
            for i in range(0, col):
                if hide[0] and hide[1]:
                    break
                if i == c:
                    index += 1
                    continue
                if grid[r][i] >= currTree:
                    hide[index] = True
            # check col
            index += 1
            for i in range(0, row):
                if hide[2] and hide[3]:
                    break
                if i == r:
                    index += 1
                    continue
                if grid[i][c] >= currTree:
                    hide[index] = True

            if not(hide[0] and hide[1] and hide[2] and hide[3]):
                nbr+= 1
    return nbr

# part 2
def getHighestScenicScore():
    maxScore = 0
    for r in range(1, row - 1):
        for c in range(1, col - 1):
            # Left Right Up Down
            trees = [0, 0, 0, 0]
            currTree = grid[r][c]
            index = 0
            # check left
            for i in range(c - 1, -1, -1):
                if grid[r][i] >= currTree:
                    trees[index] += 1
                    break
                trees[0] +=1
            # check right
            index += 1
            for i in range(c + 1, col):
                if grid[r][i] >= currTree:
                    trees[index] += 1
                    break
                trees[1] +=1
            # check up
            index += 1
            for i in range(r - 1, -1, -1):
                if grid[i][c] >= currTree:
                    trees[index] += 1
                    break
                trees[index] +=1
            # check down
            index += 1
            for i in range(r+1, row):
                if grid[i][c] >= currTree:
                    trees[index] += 1
                    break
                trees[index] +=1
            score = 1
            for t in trees:
                score *= t
            maxScore = max(maxScore, score)
    return maxScore        

print(getHighestScenicScore())