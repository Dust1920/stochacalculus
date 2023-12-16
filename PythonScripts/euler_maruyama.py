import numpy as np
import matplotlib.pyplot as plt
import brownian_motion as bw


def drift(t, x):
    a = np.sin(t) * x
    return a


def diffusion(t, x):
    b = (t / (1.0 + t)) * x
    return b


def get_em_solution(x_0, T, N):
    x_t = np.zeros(N)
    x_t[0] = x_0
    dt = T / N
    t, W = bw.u(T, N)
    for i in np.arange(N - 1):
        w_inc = W[i + 1] - W[i]
        f = drift(t[i], x_t[i])
        g = diffusion(t[i], x_t[i])
        x_t[i + 1] = x_t[i] + f * dt + sigma * g * w_inc
    return t, x_t


sigma = 2 ** (-2)
N = 2 ** 10
T = 10.0
x_0 = 1.0
fig, ax = plt.subplots()
df = []
for k in np.arange(100):
    t, x_t = get_em_solution(x_0, T, N)
    df.append([t, x_t])
    ax.plot(t, x_t, color="C0", alpha= 0.1)
plt.show()