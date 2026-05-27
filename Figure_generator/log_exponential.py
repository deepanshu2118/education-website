import numpy as np
import matplotlib.pyplot as plt

# Data
x1 = np.linspace(-2, 2, 400)
x2 = np.linspace(0.1, 4, 400)

plt.figure(figsize=(7,5))

# Axes
plt.axhline(0, linewidth=1)
plt.axvline(0, linewidth=1)

# Curves
plt.plot(x1, np.exp(x1), label=r'$y=e^x$')
plt.plot(x2, np.log(x2), label=r'$y=\log_e x$')
plt.plot(x1, x1, '--', label=r'$y=x$')

# Points
plt.scatter([0], [1])
plt.scatter([1], [0])
plt.text(0.05, 1.1, '(0,1)')
plt.text(1.05, 0.1, '(1,0)')

# Axis limits
plt.xlim(-2,4)
plt.ylim(-3,6)

# Axis names (like textbook)
plt.text(4.05, -0.15, 'X', fontsize=12)
plt.text(-2.25, -0.15, "X′", fontsize=12)
plt.text(0.05, 6.1, 'Y', fontsize=12)
plt.text(0.05, -3.4, "Y′", fontsize=12)

# Legend & grid
plt.legend()
plt.grid(True)

# Save image
plt.savefig("static/images/exp_log_graph.png", dpi=300, bbox_inches='tight')
plt.show()
