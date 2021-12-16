import math
import plotly.graph_objects as go

v0 = 11107
parr = [0.064211, 0.8616, 1.4275, 13.225, 88.0348, 363.92, 1225]
for i in range(len(parr)):
    parr[i] = parr[i] / 1000
rarr = [14000, 20000, 4000, 15000, 12000, 9000, 11000]
garr = [9.598, 9.658, 9.67, 9.716, 9.752, 9.8, 9.813]


def cosatan(x):
    return 1 / math.sqrt(1 + x ** 2)


def tanacos(x):
    return math.sqrt(1 / x ** 2 - 1)


fig = go.Figure(layout=go.Layout(title="Effect of d and k on escape velocity",
                                 xaxis=dict(title="d (2*density)"),
                                 yaxis=dict(tickformat=".2f", title="Escape velocity (km/s)")))
start_mass = 400
end_mass = 1300
x = list(range(start_mass, end_mass, 5))
for j in range(6):
    k = 0.001 if j == 0 else j * 0.5
    y = []
    for l in range(len(x)):
        v0 = 11107
        m = start_mass + 10 * l
        for i in range(len(parr)):
            s1 = cosatan(math.sqrt(k * parr[i] / (garr[i] * m)) * v0)
            s2 = tanacos(math.e**(-(k*parr[i]*rarr[i]/m))*s1)
            v0 = s2 * math.sqrt(garr[i]*m/(k*parr[i]))
        y.append(v0/1000)
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        name='k={0}'.format(round(k, 3)),
    ))

fig.show()
