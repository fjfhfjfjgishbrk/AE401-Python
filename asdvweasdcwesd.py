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

"""
import sys
import decimal

inp = sys.stdin.readlines()
for i in inp:
    a, b, n = map(int, i.strip().split(" "))
    decimal.getcontext().prec = len(str(a)) + n
    decimal.getcontext().rounding = "ROUND_DOWN"
    print(decimal.Decimal(a) / decimal.Decimal(b))
"""

"""
import math

while True:
    n = int(input())
    if n == 0:
        break
    a = map(int, input().split())
    b = 1
    for i in a:
        b = int(abs(b * i) / math.gcd(b, i))
    print(b)
"""

"""
a, b, c, d, e, f = map(int, input().split())
if (a*e - b*d) == 0:
    if (c*e - b*f) == 0 and (a*f - c*d) == 0:
        print("Too many")
    else:
        print("No answer")
else:
    x = (c*e - b*f) / (a*e - b*d)
    y = (a*f - c*d) / (a*e - b*d)
    print("x={:.2f}".format(x))
    print("y={:.2f}".format(y))
    """

"""
a = input()
n = int(input())
for i in range(n):
    t = input()
    b = 0
    c = 0
    while True:
        try:
            d = a.index(t, b)
            c += 1
            print(c)
            b = d + 1
        except:
            break
    print(c)
"""

print("1|1".replace("|", "je"))
