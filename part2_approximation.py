import matplotlib
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
matplotlib.rcParams['axes.unicode_minus'] = False
import math
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

def taylor_sin(x, n_terms):
    """
    Approximate sin(x) using the first n_terms of its Taylor series.
    sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
    Each term: (-1)^n * x^(2n+1) / (2n+1)!
    """
    result = np.zeros_like(x)
    for n in range(n_terms):
        sign = (-1) ** n
        power = 2 * n + 1
        factorial = math.factorial(power)
        result += sign * (x ** power) / factorial
    return result

# Plot sin(x) and several Taylor approximations
fig, ax = plt.subplots(figsize=(11, 6))

# True sin(x)
ax.plot(x, np.sin(x), color='black', linewidth=2.5, label='sin(x) — true')

# Approximations with increasing number of terms
colors = ['red', 'orange', 'green', 'purple', 'brown']
for i, n in enumerate([1, 2, 3, 4, 5]):
    y_approx = taylor_sin(x, n)
    ax.plot(x, y_approx, color=colors[i], linewidth=1.5,
            linestyle='--', label=f'{n} term(s)')

ax.set_ylim(-3, 3)
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
ax.set_xticklabels(['-2π', '-π', '0', 'π', '2π'])

ax.set_title('Taylor series approximation of sin(x) — more terms = closer fit')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()