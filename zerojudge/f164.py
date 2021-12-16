n, m, q = map(int, input().split())
a = list(range(n))
for i in range(m):
    b = input().split()
    if b[1] == b[2]:
        continue
    elif b[0] == "F":
        a.remove(int(b[1]))
        a.insert(a.index(int(b[2])) + 1, int(b[1]))
    else:
        a.remove(int(b[1]))
        a.insert(a.index(int(b[2])), int(b[1]))
b = [int(i) for i in input().split()]
for j in b:
    i = a.index(j)
    if (i - 1) < 0:
        print(a[-1], end=" ")
    else:
        print(a[i-1], end=" ")
    if (i + 1) >= len(a):
        print(a[0], end=" ")
    else:
        print(a[i+1], end=" ")