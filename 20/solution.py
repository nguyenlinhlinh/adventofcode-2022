f = open("20/input.txt", "r")
class Node:
    def __init__(self, left, right, value, idx):
        self.left = left
        self.right = right
        self.value = value
        self.index = idx

def parse():
    l = []
    s = set()
    for line in f:
        line = line.strip()
        l.append(int(line))
        s.add(int(line))

    print("set vs list", len(l), len(s))
    return l


def createLinkedList(list):
    start = Node(None, None, list[0], 0)
    currentNode = start
    zeroIdx = -1
    for i in range(1, len(list)):
        if list[i] == 0:
            zeroIdx = i
        n = Node(currentNode, None, list[i], i)
        currentNode.right = n
        currentNode = n

    currentNode.right = start
    start.left = currentNode
    return (start, zeroIdx)

def find(idx, start):
    curr = start
    while True:
        if curr.index == idx:
            return curr
        curr = curr.left

def moveRight(source, steps):
    if steps == 0: return
    l = source.left
    r = source.right
    l.right = r
    r.left = l
    curr = r
    for i in range(1,steps):
        curr = curr.right
    
    right = curr.right

    curr.right = source
    source.left = curr
    source.right = right
    right.left = source
    return source

def moveLeft(source, steps):
    if steps == 0: return
    
    l= source.left
    r = source.right
    l.right = r
    r.left = l
    curr = l
    for i in range(1,steps):
        curr = curr.left
    left = curr.left
    curr.left = source
    source.right = curr
    source.left = left
    left.right = source
    return source

def mixing(start, list):
    source = start
    for i in range(len(list)):
        curr = find(i, source)
        if curr.value > 0:
            source = moveRight(curr, curr.value)
        elif curr.value < 0:
            source = moveLeft(curr, abs(curr.value))
    return source
        
        # print("****",curr.value, "****")
        # result = ""
        # n = find(startVal, curr)
        # for i in range(len(list)):
        #     result += " "+ str(n.value)
        #     n = n.right
        # result += "\n"
        # print(result)

        


original = parse()

(start, zeroIdx) = createLinkedList(original)

mixing(start, original)

node_zero = find(zeroIdx, start)
n  = node_zero
sum = 0
for i in range(3001):
    if i == 1000:
        print(1000, n.value)
        sum += n.value
    elif i == 2000:
        print("2000", n.value)
        sum += n.value
    elif i == 3000:
        print("3000", n.value)
        sum += n.value
    n = n.right
print(sum)