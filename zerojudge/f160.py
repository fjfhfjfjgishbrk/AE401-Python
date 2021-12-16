t, n = map(int, input().split())
a = [int(i) for i in input().split()]
a.insert(0, 0)
b = 0
c = 1
for i in range(len(a)):
    if (a[i] - a[b]) > t:
        c += 1
        b = i - 1
print(c)