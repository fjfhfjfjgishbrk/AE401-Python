'''
num1 = 3
num2 = 4

print(num1 + num2)

str1 = 'drtfijlkhtuiyo'
print(str1)

flo1 = 15.234
print(flo1)

print('Hello world')

a = input('請輸入文字: ')
print(a)

name = 'aaa'
bmi = 23.5
print(name, bmi)
print(name + str(bmi))

age = int(input('年齡?'))
if age >= 18:
    print('成年')
else:
    print('小孩')

num = int(input('數字?'))
if num > 0:
    print('正數')
elif num == 0:
    print('零')
else:
    print('負數')

score = float(input('分數?'))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')'''

score = float(input('分數?'))
if score >= 90 and score <= 100:
    print('A')
elif score >= 80 and score < 90:
    print('B')
elif score >= 70 and score < 80:
    print('C')
elif score >= 60 and score < 70:
    print('D')
else:
    print('F')
'''
score = float(input('分數?'))
if 90 <= score <= 100:
    print('A')
elif 80 <= score < 90:
    print('B')
elif 70 <= score < 80:
    print('C')
elif 60 <= score < 70:
    print('D')
else:
    print('F')'''