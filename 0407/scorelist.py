peopleNum = int(input("how many people: "))
scoreList = []

for i in range(peopleNum):
    scoreList.append(int(input("person " + str(i+1) + " score: ")))

scoreList.sort()
print("lowest score: " + str(scoreList[0]))
print("highest score: " + str(scoreList[-1]))
print("average: " + str(sum(scoreList) / peopleNum))
