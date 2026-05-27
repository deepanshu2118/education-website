#!/usr/bin/env python3
# chart5_1_dist_picker.py  –  quick-picker flow chart (Chart 5.1)
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch

# ----------------------------------------------------------
# 1.  PAGE  (landscape A4)
# ----------------------------------------------------------
fig = plt.figure(figsize=(11.69, 8.27), dpi=300)
ax = fig.add_axes([0, 0, 1, 1], xlim=(0, 11.69), ylim=(0, 8.27))
ax.axis('off')

# ----------------------------------------------------------
# 2.  HELPER  –  rounded box
# ----------------------------------------------------------
def box(x, y, w, h, txt, fc='#E3F2FD', ec='#0288d1'):
    b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                       facecolor=fc, edgecolor=ec, lw=2)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, txt, ha='center', va='center',
            fontsize=11, weight='bold', color=ec)

# ----------------------------------------------------------
# 3.  FLOW  NODES  (x, y, width, height, text, colour)
# ----------------------------------------------------------
nodes = [
    (5.2, 7.5, 1.8, 0.7, "Start", '#424242'),
    (5.2, 6.5, 2.5, 0.7, "Continuous data?", '#FF9800'),
    (3.0, 5.3, 2.5, 0.7, "Symmetric?", '#4CAF50'),
    (7.4, 5.3, 2.5, 0.7, "Skewed?", '#9C27B0'),
    (1.2, 4.0, 2.0, 0.7, "Gaussian", '#2E7D32'),
    (3.8, 4.0, 2.0, 0.7, "Log-normal / Box-Cox", '#795548'),
    (6.8, 4.0, 2.0, 0.7, "Count data?", '#607D8B'),
    (9.2, 4.0, 2.0, 0.7, "Binary?", '#E91E63'),
    (6.8, 2.7, 2.0, 0.7, "Poisson", '#3F51B5'),
    (9.2, 2.7, 2.0, 0.7, "Bernoulli", '#FFC107'),
    (5.2, 1.4, 4.0, 0.7, "Use family table / diagnostics", '#424542')
]

for n in nodes:
    box(*n)

# ----------------------------------------------------------
# 4.  ARROWS  (decision flows)
# ----------------------------------------------------------
arrow_kw = dict(arrowstyle='->', lw=2.5, color='#424242')
def arrow(x1, y1, x2, y2, lbl=None, off=0.1):
    ax.annotate('', xy=(x2, y2 + off), xytext=(x1, y1 - off),
                arrowprops=arrow_kw)
    if lbl:
        ax.text((x1+x2)/2, (y1+y2)/2, lbl, ha='center', va='center',
                fontsize=10, weight='bold', color='#424242')

# decision branches
arrow(5.2, 6.5, 3.0, 5.3, 'yes')
arrow(5.2, 6.5, 7.4, 5.3, 'no')
arrow(3.0, 5.3, 1.2, 4.0, 'yes')
arrow(3.0, 5.3, 3.8, 4.0, 'no')
arrow(7.4, 5.3, 6.8, 4.0, 'count')
arrow(7.4, 5.3, 9.2, 4.0, 'binary')
arrow(6.8, 4.0, 6.8, 2.7, '')
arrow(9.2, 4.0, 9.2, 2.7, '')
arrow(1.2, 4.0, 5.2, 1.4, '', off=0.3)
arrow(3.8, 4.0, 5.2, 1.4, '', off=0.3)
arrow(6.8, 2.7, 5.2, 1.4, '', off=0.3)
arrow(9.2, 2.7, 5.2, 1.4, '', off=0.3)

# ----------------------------------------------------------
# 5.  PAGE  TITLE
# ----------------------------------------------------------
ax.text(11.69/2, 8.0, 'Chart 5.1  Distribution quick-picker flow',
        ha='center', va='center', fontsize=16, weight='bold')

# ----------------------------------------------------------
# 6.  SAVE  PNG
# ----------------------------------------------------------
plt.savefig('chart5_1_dist_picker.png', dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.close()
print('Chart 5.1 saved → chart5_1_dist_picker.png')