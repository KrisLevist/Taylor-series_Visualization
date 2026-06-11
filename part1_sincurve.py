import matplotlib
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
matplotlib.rcParams['axes.unicode_minus'] = False

import numpy as np
import matplotlib.pyplot as plt

# Generate x values from -2π to 2π
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Compute the true sin(x)
y = np.sin(x)

# Plot
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, y, color='blue', linewidth=2, label='sin(x)')

# Add reference lines
ax.axhline(0, color='black', linewidth=0.8)  # horizontal axis
ax.axvline(0, color='black', linewidth=0.8)  # vertical axis

# Mark x-axis with π labels
ax.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
ax.set_xticklabels(['-2π', '-π', '0', 'π', '2π'])

ax.set_title('The sine function — what we are trying to approximate')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()