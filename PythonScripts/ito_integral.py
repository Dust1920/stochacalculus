import numpy as np
from PythonScripts import brownian_motion as bw

# Tarea 


def f(x: float, t: float):
    y = x ** 2
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
        integral[i] = fB(time, w[i], time[i]) * (w[i + 1] - w[i])
    ito = integral.sum()
    return w, ito

