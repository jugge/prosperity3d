import numpy as np
import matplotlib.pyplot as plt

# Time (e.g. months)
t = np.linspace(0, 10, 200)

# Income grows linearly
income = 3000 * t

# Stepped costs (increase in blocks of 5000)
cost = np.floor(income / 5000) * 5000

# Prosperity = income − cost
prosperity = income - cost

# 3D plot with wealth as vertical axis (z)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(income, cost, prosperity, label='Taught Life Prosperity')

# Axis labels
ax.set_xlabel('Income')
ax.set_ylabel('Cost')
ax.set_zlabel('Prosperity')
ax.set_title('3D curve with Prosperity as vertical axis')
ax.legend()

plt.show()
