##print
print('Hello')

# 變數
a = 'David'
print(a)

# 型別
x = 1
y = 2.6
z = 'apple'
print(type(y))

# print相加
print(x, y, z)

# while
a = 0
while a < 3:
    print('abc')
    a = a + 1

# star tower1
i = 1
while i < 6:
    print("*" * i)
    i = i + 1

# star tower2
i = 1
while i < 6:
    print(" " * (5 - i), "*" * i)
    i = i + 1

# example a取代空白
# print('aaaa*a')
# print('aaa*a*a')
# print('aa*a*a*a')
# print('a*a*a*a*a')
# print('*a*a*a*a*a')


# star tower3
i = 0
while i < 5:
    print(" " * (4 - i), "* " * (i + 1))
    i = i + 1
