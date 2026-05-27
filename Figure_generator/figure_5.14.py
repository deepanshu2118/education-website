#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, FancyArrowPatch

# ----------------------------------------------------------
# 1.  EXAMPLE  MATRICES
# ----------------------------------------------------------
A = np.array([[2, 1, 3],
              [1, 4, 2]])          # 2×3
B = np.array([[1, 2],
              [3, 1],
              [2, 3]])          # 3×2
C = A @ B                       # 2×2  (for verification)

# ----------------------------------------------------------
# 2.  FIGURE
# ----------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 4), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.axis('off')

# ----------------------------------------------------------
# 3.  COLOUR  SCHEME
# ----------------------------------------------------------
cA, cB, cC = '#FF9800', '#4CAF50', '#2E7D32'

# ----------------------------------------------------------
# 4.  DRAW  MATRIX  BLOCKS  (A , B , C)
# ----------------------------------------------------------
def mat_block(x0, y0, mat, colour, label):
    rows, cols = mat.shape
    dw, dh = 0.8, 0.6
    for r in range(rows):
        for c in range(cols):
            rect = Rectangle((x0 + c*dw, y0 - r*dh), dw, dh,
                             facecolor=colour, alpha=0.25,
                             edgecolor=colour, lw=2)
            ax.add_patch(rect)
            ax.text(x0 + c*dw + dw/2, y0 - r*dh + dh/2, f'{mat[r, c]}',
                    ha='center', va='center', fontsize=12, weight='bold')
    ax.text(x0 - 0.3, y0 + dh/2, label, ha='right', va='center',
            fontsize=12, weight='bold', color=colour)

mat_block(0.5, 3, A, cA, 'A')
mat_block(3.5, 3, B, cB, 'B')
mat_block(7.0, 3, C, cC, 'C')

# ----------------------------------------------------------
# 5.  ROW  ×  COLUMN  “PIPES”  (animated arrows)
# ----------------------------------------------------------
pipe_y = 1.5
# A row 1  ×  B col 1  →  C[0,0]
r1, c1 = 0, 0
ax.annotate('', xy=(6.2, 3 - r1*0.6), xytext=(2.6, 3 - r1*0.6),
            arrowprops=dict(arrowstyle='-', lw=2, color=cA, shrinkA=5, shrinkB=5))
ax.annotate('', xy=(4.7, 3 - c1*0.6), xytext=(4.7, pipe_y),
            arrowprops=dict(arrowstyle='-', lw=2, color=cB, shrinkA=5, shrinkB=5))
ax.annotate('', xy=(7.8, 3 - r1*0.6), xytext=(6.8, pipe_y),
            arrowprops=dict(arrowstyle='->', lw=3, color=cC))

ax.text(4.7, pipe_y - 0.25, r'$\sum_{k} A_{1,k}\cdot B_{k,1}$', ha='center', va='top',
        fontsize=11, weight='bold', color='#424242')

# ----------------------------------------------------------
# 6.  TITLE
# ----------------------------------------------------------
ax.text(5, 3.8, 'Fig. 5.14  Matrix multiply – row × column pipes', ha='center',
        va='center', fontsize=13, weight='bold')

# ----------------------------------------------------------
# 7.  SAVE
# ----------------------------------------------------------
plt.tight_layout()
plt.savefig('fig5_14_mat_pipes.png', dpi=300, transparent=True)
plt.close()
print('Figure 5.14 saved → fig5_14_mat_pipes.png')