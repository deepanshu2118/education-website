#!/usr/bin/env python3
# fig4_12_eps.py  –  ε-differential privacy noise vs. privacy budget
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------------
# 1.  DATA  (Laplace scale = 1 / ε)
# ------------------------------------------------------------------
eps = np.array([0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0])
noise_scale = 1 / eps                        # Laplace scale parameter

# ------------------------------------------------------------------
# 2.  BAR CHART
# ------------------------------------------------------------------
plt.figure(figsize=(5, 3), dpi=300)
bars = plt.bar(eps, noise_scale, width=0.6 * np.diff(eps, prepend=0.1),
               color='#0288d1', edgecolor='#01579b', linewidth=0.8)
# colour gradient from light (high ε) to dark (low ε)
for bar, e in zip(bars, eps):
    bar.set_alpha(0.1 + 0.9 * (e / 10))   # simple linear fade

# ------------------------------------------------------------------
# 3.  COSMETICS
# ------------------------------------------------------------------
plt.xlabel('Privacy budget  ε', fontsize=11)
plt.ylabel('Laplace noise scale  (1/ε)', fontsize=11)
plt.title('Fig. 4.12  Noise magnitude vs. privacy budget', fontsize=12, pad=10)
plt.xscale('log')
plt.yscale('log')
plt.grid(axis='y', linestyle='-', alpha=0.25)
plt.tight_layout()

# ------------------------------------------------------------------
# 4.  SAVE
# ------------------------------------------------------------------
plt.savefig('fig4_12_eps.png', dpi=300, bbox_inches='tight')
plt.close()
print('Figure 4.12 saved → fig4_12_eps.png')