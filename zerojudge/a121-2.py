import time
import math

primeRange = 1000
prime = [True] * primeRange
prime[0] = False
prime[1] = False

print(str(time.process_time()) + "s")
for i in range(2, len(prime)):
    if prime[i]:
        for j in range(i ** 2, len(prime), i):
            prime[j] = False
        print(str(time.process_time()) + "s  Num: " + str(i))
    if i > math.sqrt(len(prime)):
        break
print(str(time.process_time()) + "s")

printTime = 0
f = open("prime.txt", "w")
for i in range(len(prime)):
    if prime[i]:
        f.write("{},".format(i))
    printTime = max(printTime - 1, 0)
    if time.process_time() % 1 == 0 and printTime == 0:
        print(str(round(i / 100000000 * 100, 4)) + "%")
        printTime = 6000
f.close()