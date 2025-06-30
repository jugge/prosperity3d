from strategies.base import Strategy
import numpy as np

class EarlyExtremeSaving(Strategy):
    def run(self):
        savings_account = 0
        min_prosperity = 1000
        max_necessary_cost = 50000

        for i, year in enumerate(self.years):
            income = self.start_income * (1.02) ** (year - self.years[0])
            saving_returns = savings_account * 0.04
            spendable = income + saving_returns

            # Dynamic saving until target buffer
            if savings_account < 120_000:
                savings_investment = max(income - 10000, 0)
            else:
                savings_investment = 0

            spendable -= savings_investment
            savings_account += savings_investment

            cost = min(spendable - min_prosperity, max_necessary_cost)
            cost = max(cost, 0)

            prosperity = spendable - cost

            self.income.append(income)
            self.cost.append(cost)
            self.prosperity.append(prosperity)
