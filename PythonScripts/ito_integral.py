import numpy as np
import brownian_motion as bw

# Tarea 


def f(x: float, t: float):
    y = x
    return y
     

def fB(partition: np.array, x: float, t: float):
    y = 0
    for i in range(len(partition) - 1):
        if partition[i] <= t < partition[i + 1]:
            y = f(x, t)
    return y

def ito_n(n_points: int, t: float):
    time, w = bw.u(t, n_points)
    integral = np.zeros(n_points)
    for i in range(n_points - 1):
        integral[i] = fB(time, time[i], time[i]) * (w[i + 1] - w[i])
    ito = integral.sum()
    return w, ito


samples = 100
points = 100

time = 1

t, w = bw.u(time, points)

sIto_n = 0
for i in range(samples):
    A = 0
    for j in range(points - 1):
        I_i = t[j] * (w[j + 1] - w[j])
        A += I_i
    A = A ** 2
    sIto_n += A

print(sIto_n * samples ** (-1))





