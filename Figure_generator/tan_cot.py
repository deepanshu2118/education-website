import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 2000)  # more points for smoother vertical asymptotes

# --- Tangent Graph ---
plt.figure(figsize=(6,4))
plt.ylim(-10, 10)
plt.plot(x, np.tan(x), label="tan(x)", color="orange")
plt.title("Graph of tan(x)")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.savefig("static/images/tan_graph.png", dpi=150, bbox_inches="tight")
plt.close()

# --- Cotangent Graph ---
plt.figure(figsize=(6,4))
plt.ylim(-10, 10)
plt.plot(x, 1/np.tan(x), label="cot(x)", color="green")
plt.title("Graph of cot(x)")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.savefig("static/images/cot_graph.png", dpi=150, bbox_inches="tight")
plt.close()

# --- Secant Graph ---
plt.figure(figsize=(6,4))
plt.ylim(-10, 10)
plt.plot(x, 1/np.cos(x), label="sec(x)", color="red")
plt.title("Graph of sec(x)")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.savefig("static/images/sec_graph.png", dpi=150, bbox_inches="tight")
plt.close()

# --- Cosecant Graph ---
plt.figure(figsize=(6,4))
plt.ylim(-10, 10)
plt.plot(x, 1/np.sin(x), label="cosec(x)", color="purple")
plt.title("Graph of cosec(x)")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.savefig("static/images/cosec_graph.png", dpi=150, bbox_inches="tight")
plt.close()
