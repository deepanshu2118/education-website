#!/usr/bin/env python3
# fig5_20_vc_ruler.py  –  VC-dimension ruler (Fig 5.20)
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle

# ----------------------------------------------------------
# 1.  PAGE  (landscape A4)
# ----------------------------------------------------------
fig = plt.figure(figsize=(11.69, 8.27), dpi=300)
ax = fig.add_axes([0, 0, 1, 1], xlim=(0, 11.69), ylim=(0, 8.27))
ax.axis('off')

# ----------------------------------------------------------
# 2.  RULER  BAR  (0 → 30)
# ----------------------------------------------------------
x0, y0, length = 1.0, 5.0, 9.0          # inches on page
vc_max = 30
ticks = np.arange(0, vc_max + 1, 5)

# bar outline
ax.add_patch(Rectangle((x0, y0), length, 0.4, lw=2, ec='black', fc='white'))
# ticks & labels
for v in ticks:
    x = x0 + v / vc_max * length
    ax.plot([x, x], [y0, y0 + 0.4], lw=2, color='black')
    ax.text(x, y0 - 0.25, str(v), ha='center', va='top', fontsize=10, weight='bold')

# ----------------------------------------------------------
# 3.  VC  EXAMPLES  (placed on ruler + icon)
# ----------------------------------------------------------
examples = [
    (3,  '2-D linear classifier', '#2E7D32'),
    (8,  'Decision tree depth=3', '#FF9800'),
    (10, 'SVM RBF γ=0.1', '#9C27B0'),
    (20, 'Neural net 20 weights', '#3F51B5'),
    (25, 'Large CNN (VGG)', '#607D8B')
]

for vc, name, col in examples:
    x = x0 + vc / vc_max * length
    # marker line
    ax.plot([x, x], [y0 + 0.4, y0 + 0.7], lw=3, color=col)
    # icon circle
    ax.add_patch(Circle((x, y0 + 0.9), 0.12, fc=col, ec='black', lw=1.5))
    # label
    ax.text(x, y0 + 1.25, name, ha='center', va='bottom', fontsize=9, weight='bold',
            rotation=45, color=col)

# ----------------------------------------------------------
# 4.  RULE-OF-THUMB  BAND
# ----------------------------------------------------------
safe_x = x0 + 10 / vc_max * length
ax.add_patch(Rectangle((safe_x, y0 - 0.1), length - (safe_x - x0), 0.6,
                       facecolor='#E8F5E9', edgecolor='#2E7D32', lw=2, alpha=0.4))
ax.text(x0 + length/2 + 0.5, y0 - 0.4,
        'Keep samples ≥ 10 × VC  for over-fit risk < 5 %',
        ha='center', va='top', fontsize=11, weight='bold', color='#2E7D32')

# ----------------------------------------------------------
# 5.  TITLE
# ----------------------------------------------------------
ax.text(11.69/2, 7.5, 'Fig. 5.20  VC-dimension ruler – capacity vs. sample-size guide',
        ha='center', va='center', fontsize=14, weight='bold')

# ----------------------------------------------------------
# 6.  SAVE  PNG
# ----------------------------------------------------------
plt.savefig('fig5_20_vc_ruler.png', dpi=300, bbox_inches='tight')
plt.close()
print('Figure 5.20 saved → fig5_20_vc_ruler.png')
