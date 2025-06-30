import numpy as np
import matplotlib.pyplot as plt
from strategies.taught_life import TaughtLife
from strategies.early_extreme_saving import EarlyExtremeSaving

if __name__ == "__main__":
    years = np.linspace(25, 70, 100)
    start_income = 30000

    strategies = [
        TaughtLife("Taught Life", years, start_income),
        EarlyExtremeSaving("Extreme Saver", years, start_income)
    ]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for strategy in strategies:
        strategy.run()
        r = strategy.results()
        ax.plot(r['income'], r['cost'], r['prosperity'], label=strategy.name)

    ax.set_xlabel("Income")
    ax.set_ylabel("Cost")
    ax.set_zlabel("Prosperity")
    ax.set_title("Strategy Comparison: Prosperity Over Time")
    ax.legend()
    plt.show()
