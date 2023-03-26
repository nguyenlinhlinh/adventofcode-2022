import sys
f = open("19/input.txt", "r")
ROBOT_TYPES = ["geode", "obsidian", "clay", "ore"]
MAX_ROBOTS = []
MAX_ROBOTS_1 = {"ore": 3,"clay": 14, "obsidian": 7, "geode": sys.maxsize}
MAX_ROBOTS_2 = {"ore": 3,"clay": 8, "obsidian": 12, "geode": sys.maxsize}
def getBluePrints(f):
    blueprints = []
    for line in f:
        line = line.strip().split(" ")
        data = {}
        data["ore"] = [(int(line[6]), line[7].replace(".", ""))]
        data["clay"] = [(int(line[12]), line[13].replace(".", ""))]
        data["obsidian"] = [(int(line[18]), line[19].replace(".", "")), (int(line[21]), line[22].replace(".", ""))]
        data["geode"] = [(int(line[27]), line[28].replace(".", "")), (int(line[30]), line[31].replace(".", ""))]
        blueprints.append(data)
        MAX_ROBOTS.append({"ore": 0,"clay": 0, "obsidian": 0, "geode": sys.maxsize})
        n = len(blueprints)
        for robot, requrirements in data.items():
            for (r, type)  in requrirements:
                MAX_ROBOTS[n - 1][type] = max(MAX_ROBOTS[n - 1][type], r)

        #MAX_ROBOTS[n - 1]["clay"] = int(MAX_ROBOTS[n - 1]["clay"] * 0.6)

        # for blueprint in blueprints:
        #     print(blueprint)
    return blueprints

def collectResources(robots, resources):
    updatedResources ={}
    for robot, nbrOfRobot in robots.items():
        updatedResources[robot] = resources[robot] + nbrOfRobot
    return updatedResources

def addNewRobot(robots, robotName):
    updated = {}
    for robot, nbrOfRobot in robots.items():
        updated[robot] = nbrOfRobot
    updated[robotName] +=1
    return updated

def isBuildAble(requiredResources, resources, nbrOfRobots, maxRobots, robot, minutes):
    for (amount, type) in requiredResources:
        if type not in resources or resources[type] < amount or nbrOfRobots >= maxRobots: # or resources[robot] + nbrOfRobots * minutes > maxRobots * minutes:
            return False
                
    return True

def buildRobot(requiredResources, resources):
    reducedResources = dict(resources)
    for (amount, type) in requiredResources:
        reducedResources[type] = resources[type] - amount
    return reducedResources


def getMaxGeode(blueprint, maxRobots, minutes, resources, robots, cache, itrs):
    key = (robots["ore"], robots["clay"], robots["obsidian"], robots["geode"], resources["ore"], resources["clay"], resources["obsidian"], resources["geode"], minutes)
    if key in cache:
        return cache[key]

    itrs["value"] += 1
    if itrs["value"] % 1000000 == 0:
        print(itrs["value"] // 1000000)

    #print(minutes, robots, resources)

    if minutes <= 0:
        return resources["geode"]
    maxGeode = 0
    for robot in ROBOT_TYPES:
        requiredResources = blueprint[robot]       
        if isBuildAble(requiredResources, resources, robots[robot], maxRobots[robot], robot, minutes):
            reducedResources = buildRobot(requiredResources, resources)            
            newResources = collectResources(robots, reducedResources)
            #print("Build")
            geode = getMaxGeode(blueprint, maxRobots, minutes - 1, newResources, addNewRobot(robots, robot), cache, itrs)
            maxGeode = max(maxGeode, geode)
            if robot == "geode":
                cache[key] = maxGeode
                return maxGeode
            
    #print("not Build", blueprint, minutes - 1, collectResources(robots, resources), robots)
    notBuild = getMaxGeode(blueprint,maxRobots, minutes - 1, collectResources(robots, resources), robots, cache, itrs)
    maxGeode = max(maxGeode, notBuild)
    
    cache[key] = maxGeode
    return maxGeode

def findMaxGeode(blueprints):
    sum = 1

    for i in range(2, 3):
        resources = {}
        robots = {}
        for type in ROBOT_TYPES:
            resources[type] = 0
            robots[type] = 0
        robots["ore"] = 1
        blueprint = blueprints[i]
        print("call", i)
        result = 0
        result = getMaxGeode(blueprint, MAX_ROBOTS[i], 32, resources, robots, {}, { "value": 0 })
        print("result", result)
        sum *= result

    return sum
# 41, 11

blueprints = getBluePrints(f)
print(findMaxGeode(blueprints))