#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------------------
# 1.  VECTORS
# ----------------------------------------------------------
a = np.array([4, 1])
b = np.array([2, 3])

# projection of b onto a
dot_ab = np.dot(a, b)
len_a  = np.linalg.norm(a)
proj_b_on_a = (dot_ab / len_a**2) * a            # vector projection
scalar_proj = dot_ab / len_a                     # length

# ----------------------------------------------------------
# 2.  FIGURE
# ----------------------------------------------------------
fig, ax = plt.subplots(figsize=(5, 4), dpi=300)
ax.set_xlim(-0.5, 5)
ax.set_ylim(-0.5, 4)
ax.set_aspect('equal')
ax.grid(alpha=0.25)

# ----------------------------------------------------------
# 3.  DRAW  VECTORS
# ----------------------------------------------------------
ax.arrow(0, 0, *a, head_width=0.15, head_length=0.15, fc='#FF9800', ec='#FF9800', lw=3, label='a')
ax.arrow(0, 0, *b, head_width=0.15, head_length=0.15, fc='#2E7D32', ec='#2E7D32', lw=3, label='b')

# projection vector (dashed)
ax.plot([0, proj_b_on_a[0]], [0, proj_b_on_a[1]], '--', color='#D32F2F', lw=2.5)
ax.arrow(0, 0, proj_b_on_a[0], proj_b_on_a[1], head_width=0.1, head_length=0.1,
         fc='#D32F2F', ec='#D32F2F', lw=2.5, label='proj_b_on_a')

# perpendicular dotted line
perp_start = proj_b_on_a
perp_end   = b
ax.plot([perp_start[0], perp_end[0]], [perp_start[1], perp_end[1]], ':', color='grey', lw=1.5)

# ----------------------------------------------------------
# 4.  ANNOTATIONS
# ----------------------------------------------------------
ax.text(a[0]/2, a[1]/2 - 0.3, r'$\mathbf{a}$', fontsize=14, ha='center', va='center', color='#FF9800')
ax.text(b[0]/2 + 0.2, b[1]/2, r'$\mathbf{b}$', fontsize=14, ha='center', va='center', color='#2E7D32')
ax.text(proj_b_on_a[0]/2 - 0.2, proj_b_on_a[1]/2 + 0.2,
        rf'$\frac{{\mathbf{{a}} \cdot \mathbf{{b}}}}{{\|\mathbf{{a}}\|}} = {scalar_proj:.1f}$',
        fontsize=11, ha='center', va='bottom', color='#D32F2F')

# ----------------------------------------------------------
# 5.  COSMETICS
# ----------------------------------------------------------
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y', fontsize=11)
ax.set_title(r'Fig. 5.13  Dot product = length of projection of $\mathbf{b}$ onto $\mathbf{a}$',
             fontsize=11, pad=10)
ax.legend(frameon=False, loc='upper left')

# ----------------------------------------------------------
# 6.  SAVE
# ----------------------------------------------------------
plt.tight_layout()
plt.savefig('fig5_13_dot_projection.png', dpi=300, transparent=True)
plt.close()
print('Figure 5.13 saved → fig5_13_dot_projection.png')