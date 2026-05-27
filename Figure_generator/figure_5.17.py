#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LightSource

# ----------------------------------------------------------
# 1.  GRID  (weight space)
# ----------------------------------------------------------
w1 = np.linspace(-2, 2, 400)
w2 = np.linspace(-2, 2, 400)
W1, W2 = np.meshgrid(w1, w2)

# ----------------------------------------------------------
# 2.  LOSS  SURFACES
# ----------------------------------------------------------
# convex bowl
L_conv = 0.5 * (W1**2 + W2**2)

# non-convex (two minima)
L_nonc = 0.2 * W1**4 - 1.2 * W1**2 + 0.5 * W2**2 + 0.3 * W1

# ----------------------------------------------------------
# 3.  FIGURE  (2-panel row)
# ----------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(9, 3.5), dpi=300, subplot_kw={'projection': '3d'})

# ----------------------------------------------------------
# 4.  PLOT  CONVEX  BOWL
# ----------------------------------------------------------
ax = axes[0]
ls = LightSource(270, 45)
rgb = ls.shade(L_conv, plt.cm.viridis)
surf = ax.plot_surface(W1, W2, L_conv, rstride=2, cstride=2, facecolors=rgb,
                       linewidth=0, antialiased=True, alpha=0.9)
ax.contour(W1, W2, L_conv, zdir='z', offset=0, levels=8, linewidths=0.5, colors='k', alpha=0.4)
ax.set_title('Convex – single minimum', fontsize=11, pad=10)
ax.set_xlabel('w₁'); ax.set_ylabel('w₂'); ax.set_zlabel('L(w)')
ax.view_init(elev=25, azim=45)

# ----------------------------------------------------------
# 5.  PLOT  NON-CONVEX  (TWO  MINIMA)
# ----------------------------------------------------------
ax = axes[1]
rgb = ls.shade(L_nonc, plt.cm.plasma)
surf = ax.plot_surface(W1, W2, L_nonc, rstride=2, cstride=2, facecolors=rgb,
                       linewidth=0, antialiased=True, alpha=0.9)
ax.contour(W1, W2, L_nonc, zdir='z', offset=-2, levels=12, linewidths=0.5, colors='k', alpha=0.4)
ax.set_title('Non-convex – multiple valleys', fontsize=11, pad=10)
ax.set_xlabel('w₁'); ax.set_ylabel('w₂'); ax.set_zlabel('L(w)')
ax.view_init(elev=25, azim=45)

# ----------------------------------------------------------
# 6.  PAGE  TITLE
# ----------------------------------------------------------
fig.text(0.5, 0.92, 'Fig. 5.17  Loss landscapes – convex vs. non-convex',
         ha='center', va='center', fontsize=13, weight='bold')

# ----------------------------------------------------------
# 7.  SAVE
# ----------------------------------------------------------
plt.tight_layout()
plt.savefig('fig5_17_landscapes.png', dpi=300, transparent=True)
plt.close()
print('Figure 5.17 saved → fig5_17_landscapes.png')