import numpy as np
import matplotlib.pyplot as plt

def u(t: float, n_points: int):
    dt = t / (n_points - 1)
    dw = np.sqrt(dt) * np.random.standard_normal(n_points - 1)
    w = np.zeros(n_points)
    w[1:] = dw.cumsum()
    time = np.linspace(0, t, n_points)
    return time, w