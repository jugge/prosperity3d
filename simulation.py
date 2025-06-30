import numpy as np

def run_simulation(inputs):
    years = np.linspace(inputs['current_age'], inputs['retirement_age'], 100)
    strategy = inputs['strategy_class'](inputs['strategy_name'], years, inputs['salary'])
    strategy.run()
    return strategy.results(), inputs['strategy_name']
