import math
a = int(input())
for i in range(a):
    k = int(input())
    m, n = map(int, input().split())
    mArray = [1000001] * m
    nArray = [1000001] * n
    lcd = m * n // math.gcd(m, n)
    for j in range(1, lcd // n + 1):
        b = n % m
        mArray[(b * j) % m] = n * j
    for j in range(1, lcd // m + 1):
        b = m % n
        nArray[(b * j) % n] = m * j
    limit = min(max(max(mArray), max(nArray)), k + 1)
    c = 0
    for j in range(1, limit):
        if mArray[j % m] > j and nArray[j % n] > j:
            c = j
    if c == 0:
        print("good")
    else:
        print(c)
