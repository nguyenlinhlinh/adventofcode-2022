class TreeNode:
    def __init__(self, name, type,child, parent=None, size=0,):
        self.parent = parent
        self.child = child
        self.size = size
        self.type = type
        self.name = name
root = None
currentDir = None
f = open("7/input-simple.txt", "r")
for line in f:
    line = line.strip()
    if "$ cd" in line:
        argument = line.replace("$ cd ", "")
        if (argument == "/"):
            root = TreeNode(name="/", type="dir", child={})
            currentDir = root
            
        elif argument == "..":
            currentDir = currentDir.parent
        else:
            currentDir = currentDir.child[argument]
    elif "$ ls" in line:
        continue
    else:
        [prefix, filename] = line.split(" ")
        if prefix == "dir":
            currentDir.child[filename] = TreeNode(name=filename, type=prefix, parent=currentDir, child={})
        else:
            currentDir.child[filename]= TreeNode(name=filename, type="file", size=int(prefix), parent=currentDir, child={})
def printTree(node, indent):
    q = [[node, indent]]
    while len(q) > 0:
        [n, indent] = q.pop()
        print(indent + n.type ,  n.name , str(n.size))
        for filename, data in n.child.items():
            q.append([data, indent + " "])

result = []
def recursive(node):
    if (node.type == "file"):
        return node.size
    sum = 0
    for filename, data  in node.child.items():
        sum += recursive(data)
    node.size = sum
    # if node.size < 100000:
        # result.append(node.size)
    result.append(node.size)
    return node.size

recursive(root)
printTree(root, "")
result.sort()
print(result)
maxSpace = 70000000
usedSpace = root.size
requiredSpace = 30000000
minSpace =  requiredSpace - (maxSpace - usedSpace)
print(minSpace)
for size in result:
    if size >= minSpace:
        print(size)
        break