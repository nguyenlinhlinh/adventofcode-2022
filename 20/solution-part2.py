f = open("20/input-simple.txt", "r")
class Node:
    def __init__(self, left, right, value, original, idx):
        self.left = left
        self.right = right
        self.value = value
        self.original = original
        self.index = idx

def parse(decryptionKey):
    l = []
    for line in f:
        line = line.strip()
        l.append(int(line)*decryptionKey)
    return l


def createLinkedList(list):
    # reduce the big nbr buy list length - 1 (1 is to excluded the nbr to be move)
    start = Node(None, None, list[0]% ((len(list) - 1)),list[0], 0)
    currentNode = start
    nodeZero = None
    for i in range(1, len(list)):
        n = Node(currentNode, None, list[i]%((len(list) - 1)),list[i],i)
        if list[i] == 0:
            nodeZero = n
        currentNode.right = n
        currentNode = n

    currentNode.right = start
    start.left = currentNode
    return (start, nodeZero)

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
    print
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
    for i in range(len(list)):
        curr = find(i, start)

        if curr.value > 0:
            moveRight(curr, curr.value)
        elif curr.value < 0:
            moveLeft(curr, abs(curr.value))
        
        # print("****",curr.value, "****")
        # result = ""
        # n = find(startVal, curr)
        # for i in range(len(list)):
        #     result += " "+ str(n.value)
        #     n = n.right
        # result += "\n"
        # print(result)
#811589153
original = parse(811589153)

(start, nodeZero) = createLinkedList(original)

for i in range(10):
    mixing(start, original)

n  = nodeZero
sum = 0
for i in range(3001):
    if i == 1000:
        print(1000, n.original)
        sum += n.original
    elif i == 2000:
        print("2000", n.original)
        sum += n.original
    elif i == 3000:
        print("3000", n.original)
        sum += n.original
    n = n.right
print(sum)


