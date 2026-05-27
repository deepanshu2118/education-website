import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.linspace(-3, 3, 200)

y_inc = np.exp(x)      # Strictly increasing
y_dec = np.exp(-x)     # Strictly decreasing

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

# -----------------------------
# (i) Strictly Increasing
# -----------------------------
axes[0].plot(x, y_inc)
axes[0].axhline(0)
axes[0].axvline(0)

axes[0].set_title("Strictly Increasing Function")
axes[0].set_xlim(-3, 3)
axes[0].set_ylim(-1, 10)

# -----------------------------
# (ii) Strictly Decreasing
# -----------------------------
axes[1].plot(x, y_dec)
axes[1].axhline(0)
axes[1].axvline(0)

axes[1].set_title("Strictly Decreasing Function")
axes[1].set_xlim(-3, 3)
axes[1].set_ylim(-1, 10)

# -----------------------------
# (iii) Neither Increasing nor Decreasing
# -----------------------------
axes[2].plot([1, 3], [2, 2], marker='o')
axes[2].axhline(0)
axes[2].axvline(0)

axes[2].set_title("Neither Increasing nor Decreasing")
axes[2].set_xlim(-3, 3)
axes[2].set_ylim(-3, 5)

# Labels
for ax in axes:
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

plt.tight_layout()
plt.savefig("static/images/in_dec.png", dpi=300, bbox_inches='tight')
plt.show()