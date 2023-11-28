import numpy as np

T = 1.0
L = 2 ** 13
dt = T / L
dW = np.sqrt(dt) * np.random.normal(size=L)
W = np.zeros(L + 1)
W[1 :] = np.cumsum(dW)
ito_integral = np.sum(np.multiply(W[0: -1], dW))
err = np.abs(ito_integral - 0.5 * (W[-1] ** 2 - T))
print(err)