import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 400)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(8,4))
plt.plot(x, y1, label="sin(x)", color="blue")
plt.plot(x, y2, label="cos(x)", color="red")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.legend()
plt.title("Graphs of sin(x) and cos(x)")
plt.grid(True)
plt.savefig("static/images/trig_graph.png", dpi=150)
plt.show()
