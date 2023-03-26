f = open("4/input.txt")
counter = 0
for line in f:
    pairs = line.strip().split(",")
    range1 = [int(i) for i in pairs[0].split("-")]
    range2 = [int(i) for i in pairs[1].split("-")]
    oneIsInTwo = range1[0] >= range2[0] and range1[1] <= range2[1]
    twoIsInOne = range2[0] >= range1[0] and range2[1] <= range1[1]
    sectionTwoOverlapp = range2[0] >= range1[0] and range2[0] <= range1[1]
    sectionOneOverlapp = range1[0] >= range2[0] and range1[0] <= range2[1]

    if oneIsInTwo or twoIsInOne or sectionOneOverlapp or sectionTwoOverlapp:
        print(range1, range2)
        counter += 1

print(counter)