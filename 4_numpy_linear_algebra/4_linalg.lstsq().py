import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,9)
print()

print(x)
print()
A = np.array([x,np.ones(9)])

print(A)
print()
y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]

w = np.linalg.lstsq(A.T,y,rcond=None)[0]

print(A.T)
print()

line = w[0] * x +w[1]

plt.plot(x, line, 'r-', label='Regression Line')
plt.plot(x, y, 'o', label='Data Points')
plt.legend()
plt.show()