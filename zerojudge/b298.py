class Node():
    def __init__(self):
        self.isPoison = False
        self.children = []

    def addNode(self, node):
        self.children.append(node)


facNum = [0]
n, m, l, q = map(int, input().split())
for i in range(n):
    facNum.append(Node())
for i in range(m):
    parent, child = map(int, input().split())
    facNum[parent].addNode(facNum[child])
for i in range(l):
    poisonFac = int(input())
    facNum[poisonFac].isPoison = True
    poisonChild = []
    for j in facNum[poisonFac].children:
        if not j.isPoison:
            poisonChild.append(j)
    while True:
        if poisonChild == []:
            break
        for j in poisonChild:
            j.isPoison = True
            for k in j.children:
                if not k.isPoison:
                    poisonChild.append(k)
            poisonChild.remove(j)
for i in range(q):
    searchNum = int(input())
    if facNum[searchNum].isPoison:
        print("TUIHUOOOOOO")
    else:
        print("YA~~")
