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

"""
while 1:
    try:
        num = input()
        if num == "":
            continue
        else:
            num = num.split()
        n = int(input())
        for i in range(n):
            a = 0
            b = 0
            tempNum = [str(i) for i in num]
            guess = input().split()
            for j in range(len(guess)):
                if tempNum[j] == guess[j]:
                    a += 1
                    guess[j] = "a"
                    tempNum[j] = "A"
            for j in range(len(guess)):
                for k in range(len(num)):
                    if tempNum[k] == guess[j]:
                        b += 1
                        guess[j] = "b"
                        continue
            print("{}A{}B".format(str(a), str(b)))
    except:
        break
"""

"""
import re

n = int(input())
for i in range(n):
    text = input()
    print("Case {}:".format(str(i + 1)), end=" ")
    a = True
    b = ""
    c = 0
    for j in text:
        if a:
            a = False
            b = j
        else:
            if re.match("[0-9]", j):
                c = c * 10 + int(j)
            else:
                print(b*c, end="")
                b = j
                c = 0
    print(b*c)
"""


"""
while 1:
    try:
        n = int(input())
        score = [int(i) for i in input().split()]
        score.sort()
        print(" ".join([str(i) for i in score]))
        for i in range(len(score)):
            if score[i] >= 60:
                if i == 0:
                    print("best case")
                    print(score[0])
                    break
                else:
                    print(score[i - 1])
                    print(score[i])
                    break
            if i == len(score) - 1:
                print(score[-1])
                print("worst case")
    except:
        break
"""

"""
a, b = map(int, input().split())
c = 0
for i in range(a, b+1):
    for j in str(i):
        if j == "2":
            c += 1
print(c)
"""


"""
import math
while 1:
    try:
        txt = input()
        print(txt)
        txt = txt.lower()
        a = []
        b = True
        for i in txt:
            if i.isalnum():
                a.append(i)
        for i in range(math.floor(len(a)/2)):
            if a[i] != a[-i-1]:
                b = False
        print(a)
        if b:
            print("-- is a palindrome")
        else:
            print("-- is not a palindrome")
    except:
        break
"""


"""
#'kuti' (10000000), 'lakh' (100000), 'hajar' (1000), 'shata' (100)
b = ["kuti", 'shata', 'hajar', 'lakh']
c = 0
while 1:
    try:
        num = input()
        c += 1
        print("{}.".format(c), end=" ")
        if int(num) == 0:
            print("0", end="")
        a = []
        append = True
        for i in range(1, len(num) + 1):
            if append:
                a.append(int(num[-i]))
                append = False
            else:
                a[-1] = a[-1] + int(num[-i]) * 10
                append = True
            if len(a) % 4 == 2:
                append = True
        for i in range(len(a)-1, -1, -1):
            if i == 0:
                if a[i] != 0:
                    print(a[i], end=" ")
            elif a[i] == 0 and i % 4 == 0:
                print(b[i % 4], end=" ")
            elif a[i] != 0:
                print(a[i], b[i % 4], end=" ")
        print()
    except:
        break
"""

"""
while 1:
    try:
        r, c, m = map(int, input().split())
        a = []
        for i in range(r):
            a.append([int(j) for j in input().split()])
        step = [int(i) for i in input().split()]
        for i in range(len(step)):
            tempA = []
            if step[-i-1] == 0:
                for j in range(len(a[0])):
                    tempA.append([k[-j-1] for k in a])
            else:
                for j in range(len(a)):
                    tempA.append(a[-j-1])
            a = tempA
        print(len(a), len(a[0]))
        for i in a:
            print(" ".join([str(j) for j in i]))
    except:
        break
"""


"""
while 1:
    try:
        n = int(input())
        a = [int(i) for i in input().split()]
        aSum = sum(a)
        b = 0
        for i in range(n-1):
            aSum -= a[i]
            b += a[i] * aSum
        print(b)
    except:
        break
"""


"""
input()
a = {}
while True:
    b = input()
    if b != "[1337]":
        c, d = map(str, b.split(":"))
        a[c] = d
    else:
        break
while True:
    b = input()
    if b != "[3ND]":
        c = b.split()
        for i in c:
            if i in a:
                print(a[i], end=" ")
            else:
                print(i, end=" ")
        print()
    else:
        break
"""


"""
a = input().split()
b = input().split()
c = [int(i) for i in input().split()]
d = 0
e = True
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            if i == 2:
                d = max(0, d - c[j])
                e = False
            else:
                d += c[j]
if e:
    d *= 2
print(d)
"""

"""
n = int(input())
for i in range(n):
    a = int(input())
    b = [0] * 10
    for j in range(1, a + 1):
        for k in str(j):
            b[int(k)] += 1
    print(" ".join([str(j) for j in b]))
"""

"""
import math
d = {'gb': 8000000000,  "mb": 8000000, "kb": 8000, "byte": 8, "bit": 1, "g": 8000000000, "m": 8000000, "k": 8000}
while True:
    try:
        a = input()
        b = 0
        c = []
        for i in range(len(a)-1):
            if a[i].isalpha() != a[i+1].isalpha():
                c.append(a[b:i+1])
                b = i+1
        c.append(a[b:])
        t = 0
        for i in range(0, len(c), 2):
            c[i] = math.modf(float(c[i]))[0] * 1.25 + math.modf(float(c[i]))[1] if c[i+1] != "kb" else float(c[i])
            t += int(c[i] * int(d[c[i+1]]))
        print(t)
    except:
        break
"""

"""
while True:
    a = input().lower().strip()
    b = 0
    c = False
    if a == "0":
        break
    for i in a:
        if i.isalpha():
            b += ord(i) - 96
        else:
            c = True
            break
    if c:
        print("Fail")
    else:
        print(b)
"""

"""
n = int(input())
a = {}
for i in range(n):
    b, c = map(str, input().split())
    a[b] = float(c)
d = {i: j for i, j in sorted(a.items(), key=lambda item: item[1])}
e = []
for i in range(int(n/8)):
    e.append([])
f = [i for i, j in d.items()]
g = 0
countUp = True
for i in range(n):
    e[g].append(f[i])
    g = g + 1 if countUp else g - 1
    if g == int(n/8):
        g -= 1
        countUp = False
    elif g == -1:
        g += 1
        countUp = True
h = []
for i in e:
    h.append([])
    for j in "75312468":
        h[-1].append(i[int(j) - 1])
for i in range(len(h)):
    print("{} {}".format(str(i+1), " ".join(h[i])))
"""


"""
while 1:
    try:
        a = input().split("/")
        a = int(a[0]) * 100 + int(a[1])
        if a < 121:
            print("摩羯座")
        elif a < 220:
            print("水瓶座")
        elif a < 321:
            print("雙魚座")
        elif a < 421:
            print("牡羊座")
        elif a < 522:
            print("金牛座")
        elif a < 622:
            print("雙子座")
        elif a < 723:
            print("巨蟹座")
        elif a < 822:
            print("獅子座")
        elif a < 924:
            print("處女座")
        elif a < 1024:
            print("天秤座")
        elif a < 1123:
            print("天蠍座")
        elif a < 1223:
            print("射手座")
        else:
            print("摩羯座")
    except:
        break
"""

"""
n = int(input())
pos = 0
c = 0
for i in range(n):
    a = input()
    if a == "L":
        pos -= 1
    elif a == "R":
        pos += 1
    else:
        b = int(a.split()[1])
        if pos == b:
            c += 1
print(c)
"""

"""
n = int(input())
input()
for i in range(n):
    a = int(input())
    b = int(input())
    for j in range(b):
        for k in range(1, a+1):
            print(str(k)*k)
        for k in range(a-1, 0, -1):
            print(str(k)*k)
        print()
"""



import math
while 1:
    try:
        a = round(float(input()) * 100)
        if a <= 10000:
            a = a * 0.9 + 800
        elif a <= 50000:
            a = a * 0.8
        else:
            a = a * 0.6
        a = math.floor(a)/100
        print("$" + "{:.2f}".format(a))
    except:
        break