import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

def myFunction(x):
    R_a = 0.06 * (5.12 + x)
    R_b = 0.12 * (10.24 - x)
    return R_a - R_b

xVal = np.linspace(0, 10, 100)

# Find the intersection point using fsolve
intersection_point = fsolve(myFunction, 0.5)

print("Intersection point:", intersection_point)

# Plot the functions
plt.plot(xVal, 0.06 * (5.12 + xVal), label='R_a')
plt.plot(xVal, 0.12 * (10.24 - xVal), label='R_b')

# Highlight the intersection point
plt.scatter(intersection_point, 0.06 * (5.12 + intersection_point), color='red', label='Intersection')

plt.legend()
plt.show()
