import numpy as np
import matplotlib.pyplot as plt

# Time (years after starting to work)
n_years = 50
time = np.arange(n_years)

# Salary is common, so refactored here
start_income = 30000

# Salary grows linearly
salary = start_income * (1 + 0.02) ** time


# Calculations for Taught Strategy as suggested by Society

# Savings
savings_taught = 0

# Spendable amount of money after savings
spendable_taught = salary - savings_taught

# Stepped costs (increase in blocks of 5000)
cost_taught = np.floor(spendable_taught / 5000) * 5000

# Prosperity = income − cost
prosperity_taught = spendable_taught - cost_taught

# Calculations for Early Life Extreme Savings Strategy

# Parameters
start_salary = 30000
savings_return_rate = 0.04 
max_necessary_costs = 50000
min_prosperity_level = 1000
min_cost = 20000
max_cost = 50000

# Fill arrays with start values
salary = start_salary * (1 + 0.02) ** time
savings_account_early_life = np.zeros(n_years)
prosperity_early_life = np.zeros(n_years)

for i in range(n_years):
    saving_returns = savings_account_early_life[i-1] * savings_return_rate if i > 0 else 0
    spendable = salary[i] + saving_returns
    
    cost_early_life = np.clip(spendable * 0.7, min_cost, max_cost)
    
    savings_investment =  (spendable - cost_early_life)* 0.5
    
    if i > 0:
        savings_account_early_life[i] = savings_account_early_life[i-1] + savings_investment
    else:
        savings_account_early_life[i] = savings_investment
        
    prosperity_early_life[i] = spendable - cost_early_life - savings_investment
 
# Presentation of Data
 
# 3D plot with wealth as vertical axis (z)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(salary, cost_taught, prosperity_taught, label='Taught Life Prosperity')
ax.plot(salary, cost_early_life, prosperity_early_life, label='Early Life Extreme Savings')

# Axis labels
ax.set_xlabel('Salary')
ax.set_ylabel('Cost')
ax.set_zlabel('Prosperity')
ax.set_title('3D curve with Prosperity as vertical axis')
ax.legend()

plt.show()