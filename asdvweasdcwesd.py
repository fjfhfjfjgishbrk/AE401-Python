"""
import sys
while True:
    i = sys.stdin.readline().strip()
    if i == "":
        break
    if not (i & (i-1)):
        print("Yes")
    else:
        print("No")
"""

"""
n = int(input())
for a in range(n):
    x, y, z, w, n, m = map(int, input().split(" "))
    eat = [int(i) if i != "" else "" for i in input().split(" ")]
    dead = False
    poison = 0
    for i in eat:
        m -= poison * n
        if m <= 0:
            dead = True
            break
        if i == 1:
            m += x
        elif i == 2:
            m += y
        elif i == 3:
            m -= z
        elif i == 4:
            m -= w
            poison += 1
        if m <= 0:
            dead = True
            break
    if dead:
        print("bye~Rabbit")
    else:
        print("{}g".format(m))
"""

import sys
import decimal

inp = sys.stdin.readlines()
for i in inp:
    a, b, n = map(int, i.strip().split(" "))
    decimal.getcontext().prec = len(str(a)) + n
    decimal.getcontext().rounding = "ROUND_DOWN"
    print(decimal.Decimal(a) / decimal.Decimal(b))

