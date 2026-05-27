#!/usr/bin/env python3
# chart5_2_distance_table.py  –  Chart 5.2  distance-metrics cheat-sheet
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

# ----------------------------------------------------------
# 1.  PAGE  (landscape A4)
# ----------------------------------------------------------
fig = plt.figure(figsize=(11.69, 8.27), dpi=300)
ax = fig.add_axes([0, 0, 1, 1], xlim=(0, 11.69), ylim=(0, 8.27))
ax.axis('off')

# ----------------------------------------------------------
# 2.  HEADER  BOX
# ----------------------------------------------------------
ax.add_patch(FancyBboxPatch((0.5, 7.5), 10.69, 0.6, boxstyle="round,pad=0.05",
                            facecolor='#004d99', edgecolor='none'))
ax.text(11.69/2, 7.8, 'Chart 5.2  Distance-metrics cheat-sheet', ha='center', va='center',
        fontsize=18, weight='bold', color='white')

# ----------------------------------------------------------
# 3.  COLUMN  HEADERS
# ----------------------------------------------------------
hdr_color = '#757575'
headers = ['Metric', 'Formula / Code', 'When to remember it', 'Pro', 'Con']
col_x     = [0.5, 3.0, 5.5, 8.0, 9.8]
col_w     = [2.3, 2.3, 2.3, 1.6, 1.6]

for x, w, txt in zip(col_x, col_w, headers):
    ax.add_patch(FancyBboxPatch((x, 6.8), w, 0.5, boxstyle="round,pad=0.05",
                                facecolor=hdr_color, edgecolor=hdr_color, lw=1.5))
    ax.text(x + w/2, 6.8 + 0.25, txt, ha='center', va='center',
            fontsize=10, weight='bold', color='white')

# ----------------------------------------------------------
# 4.  ROW  HELPER
# ----------------------------------------------------------
def row(y, name, formula, when, pro, con, color):
    h = 0.45
    cells = [(col_x[i], col_w[i], txt) for i, txt in enumerate([name, formula, when, pro, con])]
    for x, w, txt in cells:
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05",
                                    facecolor='white', edgecolor=color, lw=1))
        ax.text(x + 0.05, y + h/2, txt, ha='left', va='center', fontsize=9)
    return y - h - 0.02

# ----------------------------------------------------------
# 5.  DATA  ROWS  (y-start = 6.1)
# ----------------------------------------------------------
y = 6.1
rows = [
    ('Euclidean', r'√Σ(xᵢ−yᵢ)²', 'Default for continuous features', 'Intuitive, rotation-invariant', 'Sensitive to scale'),
    ('Manhattan', r'Σ|xᵢ−yᵢ|', 'Grid cities, sparse counts', 'Robust to outliers', 'Not rotation-invariant'),
    ('Mahalanobis', r'√[(x−y)ᵀΣ⁻¹(x−y)]', 'Correlated features, elliptic clusters', 'Accounts for covariance', 'Needs Σ estimate'),
    ('Cosine', r'1−(x·y)/(‖x‖‖y‖)', 'Text / embedding similarity', 'Scale-invariant', 'Ignores vector length'),
    ('Edit (Levenshtein)', 'dynamic prog.', 'String matching', 'Handles insert/del/sub', 'O(n·m) time'),
    ('Dynamic Time Warp', 'stretch-allowed', 'Time-series alignment', 'Handles speed variation', 'Needs boundary constraint')
]

colours = ['#2E7D32', '#FF9800', '#9C27B0', '#3F51B5', '#607D8B', '#795548']
for r, c in zip(rows, colours):
    y = row(y, *r, c)

# ----------------------------------------------------------
# 6.  FOOTER  NOTE
# ----------------------------------------------------------
ax.text(11.69/2, 0.6, 'Choose metric after domain + scale + correlation checks',
        ha='center', va='center', fontsize=10, style='italic', color='#424542')

# ----------------------------------------------------------
# 7.  PAGE  TITLE
# ----------------------------------------------------------
ax.text(11.69/2, 8.05, 'Chart 5.2  Distance-metrics cheat-sheet', ha='center', va='center',
        fontsize=16, weight='bold', color='#333')

# ----------------------------------------------------------
# 8.  SAVE  PNG
# ----------------------------------------------------------
plt.savefig('chart5_2_distance_table.png', dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.close()
print('Chart 5.2 saved → chart5_2_distance_table.png')