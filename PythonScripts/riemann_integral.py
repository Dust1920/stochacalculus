import numpy as np

def v(t: float):
    y = np.exp( - t)
    return y

def riemann_integral(a, b, n_points):
    r = np.zeros(n_points)
    time = np.linspace(a,b,n_points)
    for i in range(n_points - 1):
        r[i] = v(time[i]) * (time[i + 1] - time[i])
    riemann = r.sum()
    return riemann
