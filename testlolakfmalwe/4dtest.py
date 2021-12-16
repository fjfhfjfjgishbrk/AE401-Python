import numpy as np

def pmul(rarr, p):
    temp = p.copy()
    for i in rarr:
        temp = np.matmul(i, temp)
    return temp



point = [3, 5, 7, 1]
u = [-5, -1, -3, -5]
v = [2, 4, 6, 8]

m = v[1] * u[0] - u[1] * v[0]
n = - v[1] * u[2] + u[1] * v[2]

print(m, n)

cp1 = n/np.sqrt(m**2 + n**2)
sp1 = -m/np.sqrt(m**2 + n**2)

r1 = [[cp1, 0, -sp1, 0],
      [0, 1, 0, 0],
      [sp1, 0, cp1, 0],
      [0, 0, 0, 1]]
rr1 = [[cp1, 0, sp1, 0],
      [0, 1, 0, 0],
      [-sp1, 0, cp1, 0],
      [0, 0, 0, 1]]

u1 = np.matmul(r1, u)
v1 = np.matmul(r1, v)
print(u1[1] * v1[0], (v[0]*u[1]*n+v[2]*u[1]*m)/np.sqrt(m**2 + n**2))
print(v1)
print(u[1]*(v[0]*cp1-v[2]*sp1), v[1]*(u[0]*cp1-u[2]*sp1))


cp2 = v1[1] / np.sqrt(v1[0]**2 + v1[1]**2)
sp2 = v1[0] / np.sqrt(v1[0]**2 + v1[1]**2)

r2 = [[cp2, -sp2, 0, 0],
      [sp2, cp2, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]]

rr2 = [[cp2, sp2, 0, 0],
      [-sp2, cp2, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]]

u2 = np.matmul(r2, u1)
v2 = np.matmul(r2, v1)

p = u2[2] * v2[1] - v2[2] * u2[1]
q = - u2[2] * v2[3] + v2[2] * u2[3]

cp3 = q / np.sqrt(p**2 + q**2)
sp3 = -p / np.sqrt(p**2 + q**2)

r3 = [[1, 0, 0, 0],
      [0, cp3, 0, -sp3],
      [0, 0, 1, 0],
      [0, sp3, 0, cp3]]

rr3 = [[1, 0, 0, 0],
      [0, cp3, 0, sp3],
      [0, 0, 1, 0],
      [0, -sp3, 0, cp3]]

u3 = np.matmul(r3, u2)
v3 = np.matmul(r3, v2)

cp4 = v3[2] / np.sqrt(v3[1] ** 2 + v3[2] ** 2)
sp4 = v3[1] / np.sqrt(v3[1] ** 2 + v3[2] ** 2)

r4 = [[1, 0, 0, 0],
      [0, cp4, -sp4, 0],
      [0, sp4, cp4, 0],
      [0, 0, 0, 1]]

rr4 = [[1, 0, 0, 0],
      [0, cp4, sp4, 0],
      [0, -sp4, cp4, 0],
      [0, 0, 0, 1]]

u4 = np.matmul(r4, u3)
v4 = np.matmul(r4, v3)

cs = np.cos(np.pi)
ss = np.sin(np.pi)

rf = [[cs, -ss, 0, 0],
      [ss, cs, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]]

rp = np.add(u, v)
ps = np.subtract(point, rp)
plb = np.linalg.norm(ps)
us = np.subtract(u, rp)
ul = np.linalg.norm(us)
angb = np.dot(ps, us) / (plb * ul)
pointa = pmul([r1, r2, r3, r4, rf, rr4, rr3, rr2, rr1], point)
pointb = pmul([r1, r2, r3, r4, rf, rr4, rr3, rr2, rr1], pointa)
ua = pmul([r1, r2, r3, r4, rf, rr4, rr3, rr2, rr1], u)
psa = np.subtract(pointa, rp)
pla = np.linalg.norm(psa)
anga = np.dot(psa, us) / (pla * ul)


print(point, pointa, pointb)
print(angb, anga)
print(u, ua.round(7))
