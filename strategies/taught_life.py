from strategies.base import Strategy
import numpy as np

class TaughtLife(Strategy):
    def run(self):
        for year in self.years:
            income = self.start_income * (1.02) ** (year - self.years[0])
            cost = np.floor(income / 5000) * 5000
            prosperity = income - cost

            self.income.append(income)
            self.cost.append(cost)
            self.prosperity.append(prosperity)
