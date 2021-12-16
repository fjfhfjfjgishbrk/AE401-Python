"""
alpha = "abcdefghijklmnopqrstuvwxyz"

text = "Happy Valentines Day"
outText = ""
outNum = []

for n in range(1):
    outText = ""
    for i in text:
        if i.lower() in alpha:
            outText += alpha[(alpha.index(i.lower()) + 14) % 26]
            outNum.append((alpha.index(i.lower()) + 14) % 26)
        else:
            outText += i
    print(outText)
    print(outNum)
"""

def gen(n,r=[]):
    for x in range(n):
        l = len(r)
        r = [1 if i == 0 or i == l else r[i-1]+r[i] for i in range(l+1)]
        yield r
print(list(gen(15)))
