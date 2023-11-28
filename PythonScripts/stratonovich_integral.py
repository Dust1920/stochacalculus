import numpy as np
import matplotlib.pyplot as plt
import brownian_motion as bw

t_f = 1
n_p = 2** 13
t, bt = bw.u(t_f, n_p)
y = 0.5 * np.sqrt(t[1] - t[0]) * np.random.standard_normal(n_p)
stratonovich = [(0.5 * (bt[i + 1] + bt[i]) + y[i])* (bt[i + 1] - bt[i]) for i in range(n_p - 1)]
stratonovich = np.array(stratonovich).sum()
print(np.abs(stratonovich - 0.5 * bt[-1] ** 2))