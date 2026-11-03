import matplotlib.pyplot as plt
import numpy as np

# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4], [1, 2, 3, 4])
x = np.linspace(0, 2, 100)
fig, ax = plt.subplots(figsize=(5,  2.5))
ax.plot(x, x, label="linear")
ax.plot(x, x**2, label="quadratic")
ax.plot(x, x**3, label="cubic")
ax.plot(x, 2.718281828459045**x , label="expoential")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
plt.show()