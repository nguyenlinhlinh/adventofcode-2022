
def performOperation(item, operation):
    operand1 = item
    op = operation[1]
    operand2 = int(operand1 if operation[2] == "old" else operation[2])
    if op == "+":
        return operand1 + operand2
    if op == "*":
        return operand1 * operand2

def performTest(worryLevel, number, prim):
    if worryLevel % number == 0:
        # counter = 0
        # while (worryLevel % number == 0):
        #     print(number, worryLevel)
        #     counter+=1
        #     worryLevel = worryLevel // number
        # print("counter", counter)
        return (True, worryLevel % prim)
    return (False, worryLevel % prim)

f = open("11/input.txt", "r")

monkeys = []
counter = -1
for line in f:

    if "Monkey" in line:
        monkeys.append({})
        counter += 1
    elif "Starting" in line:
        items = [int(item) for item in line.strip().replace("Starting items:", "").split(",")]
        monkeys[counter]["items"] = items
    elif "Operation" in line:
        operation = line.strip().replace("Operation: new = ", "").split(" ")        
        monkeys[counter]["operation"] = operation
    elif "Test" in line:
        test = int(line.replace("Test: divisible by", ""))
        monkeys[counter]["test"] = test
    elif "true" in line:
        monkey = int(line.replace("If true: throw to monkey", ""))
        monkeys[counter]["true"] = monkey
    elif "false" in line:
        monkey = int(line.replace("If false: throw to monkey", ""))
        monkeys[counter]["false"] = monkey
prim = 1
for i in monkeys:
    prim *= i["test"]
inspections = [0 for i in range(len(monkeys))]
times = [{} for i in range(len(monkeys))]
def printMonkeys(monkeys):
    for i in range(len(monkeys)):
        print(i, monkeys[i]["items"])

# 32397480045
for i in range(10000):
    # print("round", i+1)
    # printMonkeys(monkeys)
    for m in range(len(monkeys)):
        monkey = monkeys[m]
        inspections[m] += len(monkey["items"])
        while len(monkey["items"]):
            item = monkey["items"].pop(0)
            worryLevel = performOperation(item, monkey["operation"])
            (result, worryLevel) = performTest(worryLevel, monkey["test"], prim)
            if result:
                monkeys[monkey["true"]]["items"].append(worryLevel)
            else:
                monkeys[monkey["false"]]["items"].append(worryLevel)
            if item in times[m]:
                times[m][item] += 1
            else:
                times[m][item] = 1
    print("after", i+1)
    #printMonkeys(monkeys)
    print(inspections)


inspections.sort(reverse=True)
result = inspections[0] * inspections[1]


print(result)