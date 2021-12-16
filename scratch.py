import numpy as np

array = [[1, 2, 3], [4, 5, 6]]

arrayOut = []
times = 4

for i in range(len(array)):
    arrayTemp = []
    for j in range(len(array[0])):
        for k in range(times):
            arrayTemp.append(array[i][j])
    for j in range(times):
        arrayOut.append(arrayTemp)

for i in arrayOut:
    print(i)

