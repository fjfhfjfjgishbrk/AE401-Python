"""
import time

def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][W]

print(time.process_time())
val = [1, 2, 3, 3]
print(knapSack(sum(val) // 3, val, val, len(val)))
print(time.process_time())
"""


def recursiveKnapsack(w, v, ans):
    if w[0] > v:
        return 0, ans
    if len(w) == 1:
        ans.append(w[0])
        return w[0], ans
    poppedWeight = w.pop(0)
    solWithout = recursiveKnapsack(w.copy(), v, ans.copy())
    solWith = recursiveKnapsack(w.copy(), v - poppedWeight, ans.copy())
    if solWith[0] + poppedWeight > solWithout[0]:
        solWith[1].append(poppedWeight)
        return solWith[0] + poppedWeight, solWith[1]
    return solWithout[0], solWithout[1]


input()
w = [int(i) for i in input().split()]
w.sort()
weightSum = sum(w)
if weightSum % 3 != 0:
    print("NO")
else:
    firstGroup = recursiveKnapsack(w.copy(), weightSum // 3, [])
    if firstGroup[0] == weightSum // 3:
        for i in firstGroup[1]:
            w.remove(i)
        secondGroup = recursiveKnapsack(w.copy(), (weightSum - firstGroup[0]) // 2, [])
        if secondGroup[0] != (weightSum - firstGroup[0]) // 2 or (weightSum - firstGroup[0]) % 2 != 0:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")
