import numpy as np
import matplotlib.pyplot as plt

# Define x range
x = np.linspace(-1, 1, 400)   # For arcsin and arccos
x_wide = np.linspace(-10, 10, 400)  # For arctan and arccot

# ==========================
# arcsin(x) and arccos(x)
# ==========================
plt.figure(figsize=(8,5))
plt.plot(x, np.arcsin(x), 'b', label="arcsin(x)")
plt.plot(x, np.arccos(x), 'r', label="arccos(x)")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title("Graphs of arcsin(x) and arccos(x)")
plt.legend()
plt.grid(True)
plt.show()

# ==========================
# arctan(x) and arccot(x)
# ==========================
plt.figure(figsize=(8,5))
plt.plot(x_wide, np.arctan(x_wide), 'g', label="arctan(x)")
plt.plot(x_wide, np.pi/2 - np.arctan(x_wide), 'm', label="arccot(x)")  # arccot(x) = π/2 - arctan(x)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title("Graphs of arctan(x) and arccot(x)")
plt.legend()
plt.grid(True)
plt.show()

# ==========================
# arcsec(x) and arccsc(x)
# ==========================
x_outside = np.linspace(-10, -1.01, 200).tolist() + np.linspace(1.01, 10, 200).tolist()
x_outside = np.array(x_outside)

plt.figure(figsize=(8,5))
plt.plot(x_outside, np.arccos(1/x_outside), 'orange', label="arcsec(x)")
plt.plot(x_outside, np.arcsin(1/x_outside), 'purple', label="arccsc(x)")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title("Graphs of arcsec(x) and arccsc(x)")
plt.legend()
plt.grid(True)
plt.show()
