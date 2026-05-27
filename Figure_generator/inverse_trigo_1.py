import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# arcsin(x)
# -----------------------------
x = np.linspace(-1, 1, 400)
plt.figure(figsize=(7,5))
plt.plot(x, np.arcsin(x), 'b', label="arcsin(x)")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title("Inverse Sine Function (arcsin)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

# -----------------------------
# arccos(x)
# -----------------------------
plt.figure(figsize=(7,5))
plt.plot(x, np.arccos(x), 'r', label="arccos(x)")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title("Inverse Cosine Function (arccos)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

# -----------------------------
# arctan(x)
# -----------------------------
x_wide = np.linspace(-10, 10, 400)
plt.figure(figsize=(7,5))
plt.plot(x_wide, np.arctan(x_wide), 'g', label="arctan(x)")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title("Inverse Tangent Function (arctan)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

# -----------------------------
# arccot(x) = π/2 - arctan(x)
# -----------------------------
plt.figure(figsize=(7,5))
plt.plot(x_wide, np.pi/2 - np.arctan(x_wide), 'm', label="arccot(x)")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title("Inverse Cotangent Function (arccot)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

# -----------------------------
# arcsec(x)
# -----------------------------
x_outside = np.linspace(-10, -1.01, 200).tolist() + np.linspace(1.01, 10, 200).tolist()
x_outside = np.array(x_outside)
plt.figure(figsize=(7,5))
plt.plot(x_outside, np.arccos(1/x_outside), 'orange', label="arcsec(x)")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title("Inverse Secant Function (arcsec)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

# -----------------------------
# arccsc(x)
# -----------------------------
plt.figure(figsize=(7,5))
plt.plot(x_outside, np.arcsin(1/x_outside), 'purple', label="arccsc(x)")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title("Inverse Cosecant Function (arccsc)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
