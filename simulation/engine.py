"""
Runs the chosen prosperity strategy simulation based on user input.

Responsible for instantiating the strategy class, running it, and returning results.
"""


import numpy as np

def run_simulation(inputs):
    years = np.linspace(inputs['current_age'], inputs['retirement_age'], 100)
    strategy = inputs['strategy_class'](inputs['strategy_name'], years, inputs['salary'])
    strategy.run()
    results = strategy.results()
    results['years'] = years  # Include time axis in results for plotting
    return results, inputs['strategy_name']
