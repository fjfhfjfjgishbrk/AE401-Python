"""
b = []
while 1:
    a = input().split()
    if a[0] == "SHOW":
        break
    elif a[0] == "ADD":
        b.append(a[1])
    elif a[0] == "INSERT":
        b.insert(b.index(a[2]), a[1])
    elif a[0] == "REMOVE":
        b.remove(a[1])
print(" ".join(b))
"""

"""
a = "314159265358979323846264338327950288419716939937510\
58209749445923078164062862089986280348253421170679\
82148086513282306647093844609550582231725359408128\
48111745028410270193852110555964462294895493038196\
44288109756659334461284756482337867831652712019091\
45648566923460348610454326648213393607260249141273\
72458700660631558817488152092096282925409171536436\
78925903600113305305488204665213841469519415116094\
33057270365759591953092186117381932611793105118548\
07446237996274956735188575272489122793818301194912\
98336733624406566430860213949463952247371907021798\
60943702770539217176293176752384674818467669405132\
00056812714526356082778577134275778960917363717872\
14684409012249534301465495853710507922796892589235\
42019956112129021960864034418159813629774771309960\
51870721134999999837297804995105973173281609631859\
50244594553469083026425223082533446850352619311881\
71010003137838752886587533208381420617177669147303\
59825349042875546873115956286388235378759375195778\
18577805321712268066130019278766111959092164201989"
while 1:
    try:
        print(a[0:int(int(input()) / 2) + 1])
    except:
        break
"""


"""
n = int(input())
for i in range(n):
    input()
    a = [int(i) for i in input().split()]
    high = low = 0
    for j in range(0, len(a) - 1):
        if a[j] < a[j + 1]:
            high += 1
        elif a[j] > a[j + 1]:
            low += 1
    print("Case {}: {} {}".format(str(i + 1), str(high), str(low)))
"""



"""
a = input()
b = input()
c = [0]
for i in a:
    c.append(b.count(i) + c[-1])
n = int(input())
for i in range(n):
    d = int(input())
    for j in range(len(c)):
        if d <= c[j]:
            print(a[j-1])
            break
"""

"""
c = 0
while 1:
    c += 1
    n = int(input())
    if n == 0:
        break
    a = [int(i) for i in input().split()]
    avg = int(sum(a) / n)
    b = 0
    for i in a:
        if i > avg:
            b += (i - avg)
    print("Set #{}".format(str(c)))
    print("The minimum number of moves is {}.".format(str(b)))
    print()
"""


"""
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())
for i in range(n):
    b = input()
    c = ""
    for j in b:
        c += a[(a.find(j) + 3) % len(a)]
    print(c)
"""

"""
n = int(input())
for i in range(n):
    a = [j.strip() for j in input().split(",")]
    b = [j.strip() for j in input().split(",")]
    c = len(set(a).intersection(b))
    print(c)
"""

"""
import math
while 1:
    try:
        c = [[250, 75], [400, 110], [500, 140], [750, 250]]
        p = 1000000000
        use = []
        a, b = map(int, input().split())
        for i in c:
            if b == 0:
                tempP = math.ceil(a/i[0]) * i[1]
                if tempP < p and math.ceil(a/i[0]) <= 8:
                    use = [math.ceil(a/i[0]), i[0], i[1], math.ceil(a/i[0])]
                    p = tempP
            elif b == 1:
                tempP = math.ceil(a/i[0]) * 2 * i[1]
                if tempP < p and math.ceil(a/i[0]) <= 4:
                    use = [math.ceil(a/i[0]) * 2, i[0], i[1], math.ceil(a/i[0])]
                    p = tempP
            elif b == 5:
                tempP = (math.ceil(a/i[0]) + 1) * i[1]
                if tempP < p and math.ceil(a/i[0]) <= 7:
                    use = [math.ceil(a/i[0]) + 1, i[0], i[1], math.ceil(a/i[0])]
                    p = tempP
        print("Qty: {} Disk: {}GB Price: ${}".format(str(use[0]), str(use[1]), str(use[2])))
        print("Total price of this {}GB array: ${}".format(str(use[3] * use[1]), str(use[0] * use[2])))
        print()
    except:
        break
"""

"""
while 1:
    try:
        inp = input()
        a = inp.split()
        outstr = inp.replace(" and ", "&&").replace(" or ", "||").strip()
        for i in range(0, len(a), 2):
            a[i] = int(a[i], 2)
        for i in range(2, len(a), 2):
            if a[i-1] == "or":
                a[i] = a[i-2] | a[i]
            else:
                a[i] = a[i-2] & a[i]
        print("{} = {}".format(outstr, bin(a[-1])[2:].zfill(5)))
    except:
        break
"""

"""
while 1:
    try:
        a = input()
        b = {}
        for i in a:
            c = ord(i)
            if c in b:
                b[c] += 1
            else:
                b[c] = 1
        b = {k: v for k, v in sorted(b.items(), key=lambda item: (item[1], -item[0]))}
        for i, j in b.items():
            print(i, j)
        print()
    except:
        break
"""


a = input()
b = ""
temp = a[0]
for i in range(1, len(a)):
    if ord(temp[-1]) + 1 == ord(a[i]):
        temp += a[i]
    else:
        if len(temp) >= len(b):
            b = temp
        temp = a[i]
if len(temp) >= len(b):
    b = temp
print(len(b), b)