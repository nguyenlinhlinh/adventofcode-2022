f = open("21/input.txt", "r")
def parse():
    monkeys = {}
    for line in f:
        line = line.strip().split()
        if len(line) > 2:
            monkeys[line[0].replace(":", "")] = (line[1], line[2], line[3])
        else:
            monkeys[line[0].replace(":","")] = line[1]
    return monkeys

def calculate(op, a, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a // b

def dfs(monkey, monkeys):
    m = monkeys[monkey]
    if type(m) is tuple:
        return calculate(m[1], dfs(m[0], monkeys), dfs(m[2], monkeys))
    return int(m)
    



monkeys = parse()
for m, v in monkeys.items():
    print(m,v)  

print(dfs("root", monkeys))