#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

# ----------------------------------------------------------
# 1.  CREATE  A  UNIT  CIRCLE  (set of points)
# ----------------------------------------------------------
theta = np.linspace(0, 2*np.pi, 100)
unit_circle = np.array([np.cos(theta), np.sin(theta)])          # 2×100

# ----------------------------------------------------------
# 2.  EXAMPLE  MATRIX  A  =  U Σ Vᵀ
# ----------------------------------------------------------
U = np.array([[ np.cos(np.pi/6), -np.sin(np.pi/6)],
              [ np.sin(np.pi/6),  np.cos(np.pi/6)]])   # rotate 30°
S = np.diag([3, 0.5])                                   # stretch 3×, 0.5×
Vt = np.array([[ np.cos(np.pi/4),  np.sin(np.pi/4)],
               [-np.sin(np.pi/4),  np.cos(np.pi/4)]])  # rotate 45°
A = U @ S @ Vt

# ----------------------------------------------------------
# 3.  TRANSFORM  PIPELINE
# ----------------------------------------------------------
stages = {
    'Original': unit_circle,
    'Rotate (Vᵀ)': Vt @ unit_circle,
    'Stretch (Σ)': S @ (Vt @ unit_circle),
    'Rotate (U)': U @ (S @ Vt @ unit_circle)
}

# ----------------------------------------------------------
# 4.  FIGURE  (4-panel row)
# ----------------------------------------------------------
fig, axes = plt.subplots(1, 4, figsize=(10, 2.5), dpi=300)
colors = ['#424242', '#FF9800', '#4CAF50', '#2E7D32']
titles = list(stages.keys())

for ax, title, pts, col in zip(axes, titles, stages.values(), colors):
    ax.plot(pts[0], pts[1], lw=2.5, color=col)
    ax.fill(pts[0], pts[1], alpha=0.2, color=col)
    ax.set_aspect('equal')
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-2, 2)
    ax.grid(alpha=0.25)
    ax.set_title(f'{title}', fontsize=10, pad=8)
    ax.set_xticks([])
    ax.set_yticks([])

# ----------------------------------------------------------
# 5.  ARROWS  BETWEEN  PANELS
# ----------------------------------------------------------
for i in range(3):
    x = 0.245 + i*0.25
    y = 0.45
    w, h = 0.06, 0.1
    fig.patches.append(FancyBboxPatch((x, y), w, h,
                                      boxstyle="round,pad=0.01",
                                      facecolor='white', edgecolor='none'))
    fig.text(x + w/2, y + h/2, '→', fontsize=20, ha='center', va='center',
             weight='bold', color='#333')

# ----------------------------------------------------------
# 6.  PAGE  TITLE
# ----------------------------------------------------------
fig.text(0.5, 0.92, 'Fig. 5.16  SVD = rotate → stretch → rotate',
         ha='center', va='center', fontsize=13, weight='bold')

# ----------------------------------------------------------
# 7.  SAVE
# ----------------------------------------------------------
plt.tight_layout()
plt.savefig('fig5_16_svd_cartoon.png', dpi=300, transparent=True)
plt.close()
print('Figure 5.16 saved → fig5_16_svd_cartoon.png')
