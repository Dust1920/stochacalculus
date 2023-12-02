import numpy as np
import brownian_motion as bw


# h(t) = Bt^2
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
    return ito


n = 500
t = 1

samples = 500

E_ito = np.zeros(samples)


for i in range(samples):
    E_ito[i] = ito_n(n, t) ** 2

ito_mean = E_ito.mean()


ew = np.zeros(n)
for i in range(samples):
    vector, b = bw.u(t, n)
    ws = (b**2) ** 2
    ew += ws

ew = ew * samples ** (-1)

r = np.zeros(n)
for i in range(n- 1):
    r[i] = ew[i] * (vector[i + 1] - vector[i])
riemann = r.sum()


# E[If^2] = INT_0^1 Ef^2
print(ito_mean - riemann)