'''
print('*')
print('**')
print('***')
print('****')
print('*****')
print('******')
print('*******')
print('********')
print('*********')
print('**********')


for i in range(0, 10, 1):
    print(str(i)*i)

item = input('商品名稱: ')
num = int(input('商品數量: '))
sale = float(input('商品單價: '))

print('{:10s} {:03d}件 總價{:.1f}元'.format(item, num, num*sale))
print('%-10s %03d件 總價%.1f元' % (item, num, num*sale))'''