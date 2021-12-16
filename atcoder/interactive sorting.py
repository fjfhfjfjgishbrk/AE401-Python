n, q = map(int, input().split())
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
listToSort = list(alpha[:n])


def sortPivot(sortList):
    if len(sortList) < 2:
        return sortList
    pivot = sortList[-1]
    pivotList = [pivot]
    beforeP = []
    afterP = []
    for i in sortList:
        if i == pivot:
            continue
        print("? {} {}".format(i, pivot))
        res = input()
        if res == "<":
            beforeP.append(i)
        else:
            afterP.append(i)
    return sortPivot(beforeP) + pivotList + sortPivot(afterP)


print("! " + "".join(sortPivot(listToSort)))