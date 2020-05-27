import imageio

im = imageio.imread("asdfasdfasdfasdfhjhghj.png")
f = open("a.txt", "w")
a = []
for i in range(len(im)):
    a.append([])
    for j in im[i]:
        a[i].append(str(j[0]))
print(a)
f.write("[")
for i in a:
    f.write("[")
    f.write(",".join(i))
    f.write("],")
f.write("]")