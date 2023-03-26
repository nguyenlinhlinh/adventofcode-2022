import sys
f = open("12/input.txt")
matrix = []
starts = []
goal = None
row = 0
offset = 96

for line in f:
    line = line.strip()
    a = []
    for i in range(len(line)):
        c = line[i]
        if c == "E":
            goal = (row, i)
            c = "z"
        elif c == "S":
            # start = (row, i)
            c = "a" 
        if c == "a":
            starts.append((row, i))       
        a.append(ord(c) - offset)
    row += 1
    matrix.append(a)
col = len(matrix[0])
# part 1
def bfs(start, end):
    q = [(start[0], start[1],0)]
    visited = [[False for i in range(col)] for i in range(row)]
    visited[start[0]][start[1]] = True
    while len(q):
        (r, c, s) = q.pop(0)
        print(len(q))
        print("visited", r, c, visited[r][c])
        if (r,c) == end:
            return s
        elevation = matrix[r][c]
        # Left
        nextC = c - 1
        nextR = r
        if nextC >= 0 and (not visited[nextR][nextC]) and matrix[nextR][nextC] - elevation <= 1: 
            visited[nextR][nextC] = True
            q.append((nextR, nextC, s+1))
        # Right
        nextC = c + 1
        nextR = r
        if nextC < col and (not visited[nextR][nextC]) and matrix[nextR][nextC] - elevation <= 1: 
            visited[nextR][nextC] = True
            q.append((nextR, nextC, s+1))

        # Up
        nextC = c
        nextR = r + 1
        if nextR < row and (not visited[nextR][nextC]) and matrix[nextR][nextC] - elevation <= 1: 
            visited[nextR][nextC] = True
            q.append((nextR, nextC, s+1))

        # Down
        nextC = c
        nextR = r - 1
        if nextR >= 0 and (not visited[nextR][nextC]) and matrix[nextR][nextC] - elevation <= 1: 
            visited[nextR][nextC] = True
            q.append((nextR, nextC, s+1))
# part 2
def bfs2(starts, end):
    minSteps = sys.maxsize
    for start in starts:
        q = [(start[0], start[1],0)]
        visited = [[False for i in range(col)] for i in range(row)]
        visited[start[0]][start[1]] = True
        while len(q):
            (r, c, s) = q.pop(0)
            if (r,c) == end:
                minSteps = min(minSteps, s)
                break 
            elevation = matrix[r][c]
            # Left
            nextC = c - 1
            nextR = r
            if nextC >= 0 and (not visited[nextR][nextC]) and matrix[nextR][nextC] - elevation <= 1: 
                visited[nextR][nextC] = True
                q.append((nextR, nextC, s+1))
            # Right
            nextC = c + 1
            nextR = r
            if nextC < col and (not visited[nextR][nextC]) and matrix[nextR][nextC] - elevation <= 1: 
                visited[nextR][nextC] = True
                q.append((nextR, nextC, s+1))

            # Up
            nextC = c
            nextR = r + 1
            if nextR < row and (not visited[nextR][nextC]) and matrix[nextR][nextC] - elevation <= 1: 
                visited[nextR][nextC] = True
                q.append((nextR, nextC, s+1))

            # Down
            nextC = c
            nextR = r - 1
            if nextR >= 0 and (not visited[nextR][nextC]) and matrix[nextR][nextC] - elevation <= 1: 
                visited[nextR][nextC] = True
                q.append((nextR, nextC, s+1))
    return minSteps
print(starts, goal)
print(bfs2(starts, goal))

