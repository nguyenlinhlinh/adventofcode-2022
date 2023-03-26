import heapq
import sys
f = open("16/input-simple.txt", "r")
def parse():
    valves = {}
    valvesWithFlow = 0
    for line in f:
        [first, second] = line.strip().split(";")
        first = first.split(" ")
        name = first[1]
        rate = int(first[-1].split("=")[-1])
        neighbors = [valve.replace(",", "") for valve in second.split(" ")[5:]]
        valves[name] = (rate, neighbors)
        if rate > 0:
            valvesWithFlow += 1
    return valves, valvesWithFlow

def bfs(start, valves, workingValves):
    # totalPressure, valve, minutes, openValves, nbrOfOpenValves
    queue = [(0, start, start, 30, "", 0)]
    # state contains of current valve human is at, current valve elephant is at, openList, totalPressure
    visited = dict()
    visited[(start, start, 30, "")] = 0
    maxPressure = 0
    openList = ""
    
    while len(queue):
        (totalPressure, hValve, eValve, minutes, openValves, nbrOfOpenValves) = queue.pop(0)
        if totalPressure > maxPressure:
                maxPressure = totalPressure
                openList = openValves
                print(maxPressure, openValves, len(queue))
        if minutes == 0 or nbrOfOpenValves == workingValves:
            continue
        # Both human and elephant are at the same valve
        if hValve == eValve:
            # Do something
        # Human and elephant are at different valve
        else:
            # case 1 human go to the next one
            # case 2 open the valve
        for v in valves[valve][1]:
            # not open go to the next one
            nextState = (v, openValves)
            if nextState not in visited:
                data = (totalPressure, v, minutes - 1, openValves, nbrOfOpenValves)
                queue.append(data)
                visited[nextState] = totalPressure            
        # open 
        flowRate = valves[valve][0]
        newTotalPressure = totalPressure + (minutes - 1) * flowRate
        newOpenList = openValves + valve + ","
        nextState = (valve, newOpenList)
        if flowRate > 0 and valve not in openValves and nextState not in visited:
            data = (newTotalPressure, valve, minutes - 1, newOpenList, nbrOfOpenValves + 1)
            queue.append(data)            
            visited[nextState] = newTotalPressure

    return maxPressure, openList

        


valves, valveWithFlow = parse()
maxPressure, open = bfs("AA", valves, valveWithFlow)
print("valveWithFlow", valveWithFlow)
print(maxPressure, open)

#1103