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
        return a / b

def performInverseOp(op, a, b):
    if op == "+":
        print(a, "-", b)
        return a - b
    if op == "-":
        print(a, "+", b)
        return a + b
    if op == "/":
        print(a, "*", b)
        return a * b
    if op == "*":
        print(a, "/", b)
        return a / b


def dfs(monkey, monkeys, variable):
    m = monkeys[monkey]
    if monkey == "humn":
        variable = True
    if type(m) is tuple:
        (left, leftVariable) = dfs(m[0], monkeys, variable)
        (right, rightVariable) = dfs(m[2], monkeys, variable)
        result = calculate(m[1], left, right)
        return result, leftVariable or rightVariable
    return int(m), variable
    
def buildEquation(monkey, monkeys):
    m = monkeys[monkey]
    if monkey == "humn":
        return "H"
    if type(m) is tuple:
        left = buildEquation(m[0], monkeys)
        right = buildEquation(m[2], monkeys)
        if (type(left) is int or type(left) is float) and (type(right) is int or type(right) is float):
            return calculate(m[1], left, right)
        return (left, m[1], right)
    else:
        return int(m)

monkeys = parse()
(leftMonkey, op, rightMonkey) = monkeys["root"]
(leftVal, leftVariable) = dfs(leftMonkey, monkeys, False )
(rightVal, rightVariable) = dfs(rightMonkey, monkeys, False)

equation = None
val = 0
if leftVariable:
   equation =  buildEquation(leftMonkey, monkeys)
   val = rightVal
else:
   equation =  buildEquation(rightMonkey, monkeys)
   val = leftVal

expresion = equation
while expresion:
    (left, op, right) = expresion
    if type(left) is int or type(left) is float:
        if op == "-":
            val = calculate("-", left, val)
        elif op == "/":
            val = calculate("/", left, val )
        else:
            val = performInverseOp(op, val, left)
        expresion = right
    if type(right) is int or type(right) is float:
        val = performInverseOp(op, val, right)
        expresion = left    
    if expresion == "H":
        break

print("RESULT", val)
    
# Test
monkeys["humn"] = val
print(dfs(leftMonkey, monkeys, False ))
print(dfs(rightMonkey, monkeys, False))


