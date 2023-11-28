import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def drift(t, x):
    a = np.sin(t) * x
    return a


def diffusion(t, x):
    b = (t / (1.0 + t)) * x
    return b


def strong_brownian_path(N, T):
    delta = T / N
    h = 1.0 / N
    t = np.linspace(0, T, N + 1)
    b = np.random.binomial(1, 0.5, N)  # bernulli 0,1
    omega = 2.0 * b - 1  # bernulli -1,1
    Xn = h * (omega.cumsum())  # bernulli -h,h
    Xn = np.concatenate(([0], Xn))
    M = np.abs(Xn).max() + h
    mu = Xn.mean() * np.ones(Xn.shape)
    return t, Xn


def get_em_solution(x_0, T, N):
    x_t = np.zeros(N + 1)
    x_t[0] = x_0
    dt = T / N
    t, W = strong_brownian_path(N, T)
    for i in np.arange(N):
        w_inc = W[i + 1] - W[i]
        f = drift(t[i], x_t[i])
        g = diffusion(t[i], x_t[i])
        x_t[i + 1] = x_t[i] + f * dt + sigma * g * w_inc
    return t, x_t


sigma = 2 ** (-2)
N = 2 ** 10
T = 5.0
x_0 = 1.0
fig, ax = plt.subplots()
df = []
for k in np.arange(200):
    t, x_t = get_em_solution(x_0, T, N)
    df.append([t, x_t])
    ax.plot(t, x_t, color="C0", alpha=0.1)
plt.show()