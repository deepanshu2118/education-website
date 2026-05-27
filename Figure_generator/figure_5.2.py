#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------------------
# 1.  COORDINATES  (two torches on the floor)
# ----------------------------------------------------------
A = np.array([1, 2])
B = np.array([4, 5])

# ----------------------------------------------------------
# 2.  FIGURE
# ----------------------------------------------------------
fig, ax = plt.subplots(figsize=(4, 4), dpi=300)
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.set_aspect('equal')
ax.axis('off')

# ----------------------------------------------------------
# 3.  DRAW  GRID  (floor tiles)
# ----------------------------------------------------------
grid_kw = dict(color='#CCCCCC', linewidth=0.5, alpha=0.7)
ax.set_xticks(np.arange(0, 7, 1), minor=False)
ax.set_yticks(np.arange(0, 7, 1), minor=False)
ax.grid(True, **grid_kw)

# ----------------------------------------------------------
# 4.  TORCHES  (yellow circles) +  LABELS
# ----------------------------------------------------------
ax.scatter(*A, s=180, color='#FFC107', edgecolors='#FF8F00', zorder=3)
ax.scatter(*B, s=180, color='#FFC107', edgecolors='#FF8F00', zorder=3)
ax.text(A[0]-0.2, A[1]+0.25, 'Torch A', ha='center', fontsize=10, weight='bold')
ax.text(B[0]+0.2, B[1]+0.25, 'Torch B', ha='center', fontsize=10, weight='bold')

# ----------------------------------------------------------
# 5.  DISTANCE  ARROW  (cable between torches)
# ----------------------------------------------------------
ax.annotate('', xy=B, xytext=A,
            arrowprops=dict(arrowstyle='<->', lw=3, color='#2E7D32'))
mid = (A + B) / 2
ax.text(mid[0], mid[1] + 0.15, f'd = {np.linalg.norm(B - A):.1f}', va='bottom',
        ha='center', fontsize=11, color='#2E7D32', weight='bold')

# ----------------------------------------------------------
# 6.  TITLE
# ----------------------------------------------------------
ax.set_title('Fig. 5.2  Flashlight grid – Euclidean distance on the floor',
             fontsize=11, pad=10)

# ----------------------------------------------------------
# 7.  SAVE
# ----------------------------------------------------------
plt.tight_layout()
plt.savefig('fig5_2_flashlight.png', dpi=300, transparent=True)
plt.close()
print('Figure 5.2 saved → fig5_2_flashlight.png')