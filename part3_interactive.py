import matplotlib
matplotlib.use('QtAgg')
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
matplotlib.rcParams['axes.unicode_minus'] = False

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import math

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

def taylor_sin(x, n_terms):
    """Approximate sin(x) using the first n_terms of its Taylor series."""
    result = np.zeros_like(x)
    for n in range(n_terms):
        sign = (-1) ** n
        power = 2 * n + 1
        result += sign * (x ** power) / math.factorial(power)
    return result

# Set up the figure
fig, ax = plt.subplots(figsize=(11, 7))
plt.subplots_adjust(bottom=0.2)  # Leave space for the slider

# Plot true sin(x)
ax.plot(x, np.sin(x), color='black', linewidth=2.5, label='sin(x) — true')

# Initial approximation with 1 term
y_init = taylor_sin(x, 1)
approx_line, = ax.plot(x, y_init, color='red', linewidth=2,
                        linestyle='--', label='Taylor approximation')

ax.set_ylim(-3, 3)
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
ax.set_xticklabels(['-2π', '-π', '0', 'π', '2π'])
ax.set_title('Taylor series approximation of sin(x) — drag the slider')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

# Term label shown on the plot
term_text = ax.text(0.02, 0.95, 'Terms: 1', transform=ax.transAxes,
                     fontsize=12, verticalalignment='top')

# Add the slider
slider_ax = fig.add_axes([0.2, 0.07, 0.6, 0.03])  # [left, bottom, width, height]
slider = Slider(slider_ax, 'Number of terms', 1, 10, valinit=1, valstep=1)

# Update function — called every time the slider moves
def update(val):
    n = int(slider.val)
    y_new = taylor_sin(x, n)
    approx_line.set_ydata(y_new)
    term_text.set_text(f'Terms: {n}')
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()