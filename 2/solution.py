# A = Rock
# B = Paper
# C = Scissors
# Y = Paper = 2
# X = Rock = 1
# Z = Scisscors = 3

# lost = 0
# draw = 3
# won = 6
# X = 1
# Y = 2
# Z = 3

# Part 1
# resultScore = {"A X": 3, "B X": 0, "C X": 6, "A Y": 6, "B Y": 3, "C Y": 0, "A Z": 0, "B Z": 6, "C Z" : 3}
# shapeScore = {"X": 1, "Y": 2, "Z": 3}
# f = open("2/input.txt", "r")
# score = 0
# for line in f:
#     match = line.strip()
#     result = resultScore[match]
#     score = score + result + shapeScore[match[2]]
# print(score)

# Part 2
X = 0 # lose
Y = 3 # draw 
Z = 6 # win
shapeScore = { "A X": 3, "B X": 1, "C X": 2, "A Y": 1, "B Y": 2, "C Y": 3, "A Z": 2, "B Z":3, "C Z": 1} 
resultScore = {"X": 0, "Y": 3, "Z": 6}
f = open("2/input.txt", "r")
score = 0
for line in f:
    match = line.strip()
    result = resultScore[match[2]]
    score = score + result + shapeScore[match]
    print(result + shapeScore[match])
print(score)