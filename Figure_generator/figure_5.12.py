#!/usr/bin/env python3
# fig5_12_lego_box.py
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle
import matplotlib.cm as cm

# ------------------------------------------------------------------
# 1.  PAGE  (landscape A4)
# ------------------------------------------------------------------
fig = plt.figure(figsize=(11.69, 8.27), dpi=300)
ax = fig.add_axes([0, 0, 1, 1], xlim=(0, 11.69), ylim=(0, 8.27))
ax.axis('off')

# ------------------------------------------------------------------
# 2.  CARD  HELPER
# ------------------------------------------------------------------
def card(x0, y0, w, h, title, colour):
    box = FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.08",
                         facecolor='white', edgecolor=colour, lw=3)
    ax.add_patch(box)
    ax.text(x0 + w/2, y0 + h - 0.35, title, ha='center', va='center',
            fontsize=15, weight='bold', color=colour)

# ------------------------------------------------------------------
# 3.  THREE  CARDS  (side-by-side)
# ------------------------------------------------------------------
card(0.8, 4.5, 3.2, 3.2, 'Vector  –  arrow', '#FF9800')
card(4.4, 4.5, 3.2, 3.2, 'Matrix  –  grid', '#4CAF50')
card(8.0, 4.5, 3.2, 3.2, 'Tensor  –  Rubik', '#2E7D32')

# ------------------------------------------------------------------
# 4.  VECTOR  ARROW  (inside left card)
# ------------------------------------------------------------------
vec_ax = fig.add_axes([1.0/11.69, 5.0/8.27, 2.4/11.69, 2.2/8.27], xlim=(-1, 4), ylim=(-1, 3))
vec_ax.arrow(0, 0, 3, 2, head_width=0.2, head_length=0.15, fc='#FF9800', ec='#FF9800', lw=3)
vec_ax.text(1.5, 1.3, r'$\mathbf{v}$', fontsize=20, color='#FF9800', ha='center')
vec_ax.grid(alpha=0.2); vec_ax.set_aspect('equal'); vec_ax.axis('off')

# ------------------------------------------------------------------
# 5.  MATRIX  GRID  (middle card)
# --------------------------------------------------------------------------
mat_ax = fig.add_axes([4.6/11.69, 5.0/8.27, 2.4/11.69, 2.2/8.27])
mat = np.arange(1, 13).reshape(3, 4)
cmap = cm.get_cmap('Greens')
mat_ax.matshow(mat, cmap=cmap, alpha=0.8)
for (i, j), val in np.ndenumerate(mat):
    mat_ax.text(j, i, val, ha='center', va='center', fontsize=12, weight='bold')
mat_ax.axis('off')

# ------------------------------------------------------------------
# 6.  TENSOR  RUBIK  (right card)
# --------------------------------------------------------------------------
ten_ax = fig.add_axes([8.2/11.69, 5.0/8.27, 2.4/11.69, 2.2/8.27])
cube = np.random.choice([0, 1, 2], (3, 3, 3))   # 3×3×3 tensor
colors = ['#ffffff', '#2E7D32', '#FFC107']
for i in range(3):
    for j in range(3):
        for k in range(3):
            ten_ax.add_patch(Rectangle((j + 0.1 * k, i + 0.1 * k), 0.9, 0.9,
                                       facecolor=colors[cube[i, j, k]], lw=0.5, ec='grey'))
ten_ax.set_xlim(-0.1, 3.4); ten_ax.set_ylim(-0.1, 3.4); ten_ax.axis('off')

# ------------------------------------------------------------------
# 7.  PAGE  TITLE
# ------------------------------------------------------------------
ax.text(11.69/2, 8.0, 'Fig. 5.12  Linear-algebra Lego box – vector, matrix, tensor',
        ha='center', va='center', fontsize=18, weight='bold')

# ------------------------------------------------------------------
# 8.  SAVE  PNG
# ------------------------------------------------------------------
plt.savefig('fig5_12_lego_box.png', dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.close()
print('Figure 5.12 saved → fig5_12_lego_box.png')