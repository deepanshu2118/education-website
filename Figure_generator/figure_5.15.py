#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

# ----------------------------------------------------------
# 1.  TRANSFORMATION  MATRIX  (stretch along 45°)
# ----------------------------------------------------------
λ1, λ2 = 3, 0.5                          # eigenvalues
θ = np.pi/4                              # 45°
V = np.array([[np.cos(θ), -np.sin(θ)],
              [np.sin(θ),  np.cos(θ)]])  # rotation matrix
Λ = np.diag([λ1, λ2])
A = V @ Λ @ V.T                          # symmetric 2×2

# ----------------------------------------------------------
# 2.  EIGENVECTORS  (unit length)
# ----------------------------------------------------------
v1 = V[:, 0]   # first column → 45°
v2 = V[:, 1]   # second column → 135°

# ----------------------------------------------------------
# 3.  FIGURE  (2-panel: before → after)
# ----------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.5), dpi=300)

def draw_unit_circle(ax, title):
    circ = plt.Circle((0, 0), 1, fill=False, lw=2, color='grey', alpha=0.4)
    ax.add_patch(circ)
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.6, 1.6)
    ax.set_aspect('equal')
    ax.grid(alpha=0.25)
    ax.set_title(title, fontsize=11, pad=8)

draw_unit_circle(ax1, 'Before transform')
draw_unit_circle(ax2, 'After transform (A)')

# ----------------------------------------------------------
# 4.  ARROWS:  EIGENVECTORS  (red & blue)
# ----------------------------------------------------------
def eigen_arrow(ax, vec, colour, label):
    ax.arrow(0, 0, vec[0], vec[1], head_width=0.08, head_length=0.08,
             fc=colour, ec=colour, lw=3, length_includes_head=True)
    ax.text(vec[0]*1.15, vec[1]*1.15, label, ha='center', va='center',
            fontsize=11, weight='bold', color=colour)

eigen_arrow(ax1, v1, '#D32F2F', r'$\mathbf{v}_1$')
eigen_arrow(ax1, v2, '#2E7D32', r'$\mathbf{v}_2$')

# same arrows after transform
Av1 = A @ v1
Av2 = A @ v2
eigen_arrow(ax2, Av1, '#D32F2F', r'$\lambda_1\mathbf{v}_1$')
eigen_arrow(ax2, Av2, '#2E7D32', r'$\lambda_2\mathbf{v}_2$')

# ----------------------------------------------------------
# 5.  DIRECTION  UNCHANGED  CALLOUT
# ----------------------------------------------------------
ax2.text(0, -1.4, 'Directions of v₁ and v₂ stay fixed; only lengths scale by λ₁, λ₂',
         ha='center', va='center', fontsize=10,
         bbox=dict(boxstyle="round,pad=0.4", facecolor='white', edgecolor='#333'))

# ----------------------------------------------------------
# 6.  PAGE  TITLE
# ----------------------------------------------------------
fig.text(0.5, 0.92, 'Fig. 5.15  Eigenvectors – directions untouched by transformation',
         ha='center', va='center', fontsize=13, weight='bold')

# ----------------------------------------------------------
# 7.  SAVE
# ----------------------------------------------------------
plt.tight_layout()
plt.savefig('fig5_15_eigen_arrow.png', dpi=300, transparent=True)
plt.close()
print('Figure 5.15 saved → fig5_15_eigen_arrow.png')