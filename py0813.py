# def add(a, b):
#     print(a + b)
#
# def sub(a, b):
#     print(a - b)
#
# def mul(a, b):
#     print(a * b)
#
# def div(a, b):
#     print(a / b)
#
# num1 = int(input('輸入第一個數字: '))
# num2 = int(input('輸入第二個數字: '))
# add(num1, num2)
# sub(num1, num2)
# mul(num1, num2)
# div(num1, num2)

# import os
# if os.path.isfile('file1.txt'):
#     f1 = open('file1.txt', 'r')
#     score = []
#     for i in f1.readlines():
#         score.append(int(i.replace('\n','')))
#         print(i)
#     print(score)
#     f1.close()
#
#     f2 = open('file1.txt', 'a')
#     s = '\nMax: ' + str(max(score))
#     s += '\nMin: ' + str(min(score))
#     s += '\nAverage: ' + str(sum(score)/len(score))
#     f2.write(s)
#     f2.close()

import sys
try:
    file1 = open("fileln.txt", 'r')
    file2 = open("fileOut.txt", 'w+')
except IOError:
    print('檔案不存在')
finally:
    i = 1
    for line in file1:
        print(line.rstrip())
        file2.write("line" + str(i) + ": " + line)
        i = i + 1
    file1.close()
    file2.close()
