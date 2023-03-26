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
    # valve, minutes, totalPressure, openValves, nbrOfOpenValves
    queue = [(0, start, 30, "", 0)]
    # state contains of current valve, totalPressure and openList
    visited = dict()
    visited[(start, "")] = 0
    maxPressure = 0
    openList = ""
    
    while len(queue):
        (totalPressure, valve, minutes, openValves, nbrOfOpenValves) = queue.pop(0)
        if totalPressure > maxPressure:
                maxPressure = totalPressure
                openList = openValves
                print(maxPressure, openValves, len(queue))
        if minutes == 0 or nbrOfOpenValves == workingValves:
            continue

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

        
# answer input
# 1944 MH,QW,ZU,NT,KF,FF,XY,NQ,

# answer simple
# 1651 DD,BB,JJ,HH,EE,CC,
valves, valveWithFlow = parse()
maxPressure, open = bfs("AA", valves, valveWithFlow)
print("valveWithFlow", valveWithFlow)
print(maxPressure, open)