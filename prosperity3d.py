import numpy as np
import matplotlib.pyplot as plt

# Time (e.g. months)
age = np.linspace(25, 70, 100)
years_after_25 = age - 25

# Start income at 24 years of age (in SEK)
start_income = 30000

# Income grows linearly
income_taught = start_income * (1 + 0.02) ** years_after_25
income_early_life = start_income * (1 + 0.02) ** years_after_25

# Savings
savings_taught = 0
savings_early_life = income_early_life - 1000

# Spendable amount of money after savings
spendable_taught = income_taught - savings_taught
spendable_early_life = income_early_life - savings_early_life

# Stepped costs (increase in blocks of 5000)
cost_taught = np.floor(spendable_taught / 5000) * 5000
cost_early_life = np.floor(spendable_early_life - 1000)

# Prosperity = income − cost
prosperity_taught = income_taught - cost_taught
prosperity_early_life = spendable_early_life - cost_early_life

# 3D plot with wealth as vertical axis (z)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(income_taught, cost_taught, prosperity_taught, label='Taught Life Prosperity')
ax.plot(income_early_life, cost_early_life, prosperity_early_life, label='Early Life Extreme Savings')

# Axis labels
ax.set_xlabel('Income')
ax.set_ylabel('Cost')
ax.set_zlabel('Prosperity')
ax.set_title('3D curve with Prosperity as vertical axis')
ax.legend()

plt.show()
