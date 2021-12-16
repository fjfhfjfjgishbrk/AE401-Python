import math
import time
primeNumber = []
isPrime = False
printTime = 0
for i in range(3, 100000000, 2):
    isPrime = True
    printTime = max(printTime - 1, 0)
    if time.process_time() % 1 == 0 and printTime == 0:
        print(str(round(i / 100000000 * 100, 4)) + "%")
        printTime = 1500
    for j in primeNumber:
        if i % j == 0:
            isPrime = False
            break
        if j > math.sqrt(i):
            break
    if isPrime:
        primeNumber.append(i)

print(primeNumber)
print(time.process_time())