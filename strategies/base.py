import numpy as np

class Strategy:
    def __init__(self, name, years, start_income):
        self.name = name
        self.years = years
        self.start_income = start_income
        self.income = []
        self.cost = []
        self.prosperity = []

    def run(self):
        raise NotImplementedError

    def results(self):
        return {
            'income': np.array(self.income),
            'cost': np.array(self.cost),
            'prosperity': np.array(self.prosperity)
        }
