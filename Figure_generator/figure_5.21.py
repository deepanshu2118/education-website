#!/usr/bin/env python3
# fig5_21_dartboards.py  –  4-panel dart-board cartoon (Fig 5.21)
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Wedge

# ----------------------------------------------------------
# 1.  DART-BOARD  HELPER
# ----------------------------------------------------------
def dartboard(ax, title, bull=(0,0), spread=1, bias_angle=0, colour='#1976D2'):
    """draw 30 darts around bull; spread & bias for demo"""
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.axis('off')

    # rings
    for r in [1.0, 0.8, 0.6, 0.4, 0.2]:
        ax.add_patch(Circle((0, 0), r, lw=1, ec='grey', fc='none'))
    ax.add_patch(Circle((0, 0), 0.2, fc='red', ec='black', lw=2))  # bull's-eye

    # darts
    rng = np.random.default_rng(42)
    for i in range(30):
        # polar → cartesian
        angle = rng.uniform(0, 2*np.pi) + np.radians(bias_angle)
        r = rng.exponential(scale=spread) * 0.15
        x = bull[0] + r * np.cos(angle)
        y = bull[1] + r * np.sin(angle)
        ax.plot(x, y, 'o', ms=5, color=colour, alpha=0.9)

    ax.set_title(title, fontsize=11, weight='bold', pad=8)

# ----------------------------------------------------------
# 2.  FIGURE  (2×2 grid)
# ----------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(6, 6), dpi=300,
                         subplot_kw={'aspect': 'equal'})
axes = axes.flatten()
titles = ['Low bias / Low variance\n(bull’s-eye)',
          'High bias\n(tight but off-centre)',
          'High variance\n(scattered around centre)',
          'High bias + High variance\n(scattered & off-centre)']
colours = ['#2E7D32', '#FF9800', '#9C27B0', '#D32F2F']
params  = [{'spread': 0.6, 'bias_angle': 0},
           {'spread': 0.4, 'bias_angle': 45},
           {'spread': 1.8, 'bias_angle': 0},
           {'spread': 1.6, 'bias_angle': 60}]

for ax, title, col, par in zip(axes, titles, colours, params):
    dartboard(ax, title, colour=col, **par)

# ----------------------------------------------------------
# 3.  PAGE  TITLE
# ----------------------------------------------------------
fig.text(0.5, 0.92, 'Fig. 5.21  Bias–variance dartboards – total error = bias² + variance + noise',
         ha='center', va='center', fontsize=13, weight='bold')

# ----------------------------------------------------------
# 4.  SAVE  PNG
# ----------------------------------------------------------
plt.tight_layout()
plt.savefig('fig5_21_dartboards.png', dpi=300, transparent=True)
plt.close()
print('Figure 5.21 saved → fig5_21_dartboards.png')