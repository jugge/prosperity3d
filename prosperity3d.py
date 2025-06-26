import numpy as np
import matplotlib.pyplot as plt

# Ålder från 25 till 70 år
ålder = np.linspace(25, 70, 1000)
år_efter_25 = ålder - 25

# Inkomst ökar 2 % per år från 30 000
startinkomst = 30000
inkomst = startinkomst * (1 + 0.02) ** år_efter_25

# Trappstegskostnad (5000 kr per steg)
kostnad = np.floor(inkomst / 5000) * 5000

# Välstånd = inkomst − kostnad
välstånd = inkomst - kostnad

# 3D-plot med önskad axelordning
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# X = Inkomst, Y = Kostnad, Z = Välstånd
ax.plot(inkomst, kostnad, välstånd, label='Välståndskurva')

ax.set_xlabel('Inkomst')
ax.set_ylabel('Kostnader')
ax.set_zlabel('Välstånd (Inkomst − Kostnader)')
ax.set_title('3D-kurva: Välstånd som funktion av Inkomst och Kostnader')
ax.legend()

plt.show()
