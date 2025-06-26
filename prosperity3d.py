import numpy as np
import matplotlib.pyplot as plt

# Tid (t.ex. månader)
t = np.linspace(0, 10, 200)

# Inkomst ökar linjärt
inkomst = 3000 * t

# Trappformade kostnader
kostnad = np.floor(inkomst / 5000) * 5000

# Välstånd = inkomst − kostnad
välstånd = inkomst - kostnad

# 3D-plot med välstånd som vertikal axel (z)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(inkomst, kostnad, välstånd, label='Välståndskurva')

# Etiketter
ax.set_xlabel('Inkomst')
ax.set_ylabel('Kostnader')
ax.set_zlabel('Välstånd (Inkomst − Kostnader)')
ax.set_title('3D-kurva med Välstånd som vertikal axel')
ax.legend()

plt.show()
