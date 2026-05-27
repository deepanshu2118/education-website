#!/usr/bin/env python3
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np

# ----------------------------------------------------------
# 1.  FIGURE  (landscape)
# ----------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 3), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis('off')

# ----------------------------------------------------------
# 2.  TREE  STRUCTURE  (root → branches → leaves)
# ----------------------------------------------------------
def node(x, y, txt, fc='#E3F2FD', ec='#0288d1'):
    box = FancyBboxPatch((x-0.45, y-0.25), 0.9, 0.5,
                         boxstyle="round,pad=0.05", facecolor=fc, edgecolor=ec, lw=1.2)
    ax.add_patch(box)
    ax.text(x, y, txt, ha='center', va='center', fontsize=10, weight='bold')

def arrow(x1, y1, x2, y2, label=None, color='#424242'):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', lw=1.5, color=color))
    if label:
        midx, midy = (x1+x2)/2, (y1+y2)/2
        ax.text(midx, midy+0.15, label, ha='center', va='bottom', fontsize=9, color=color)

# nodes
node(1, 2, 'P(B)', fc='#FFF9C4', ec='#F57C00')                 # root
node(4, 2.7, 'P(A|B)', fc='#E8F5E9', ec='#388E3C')            # branch
node(4, 1.3, 'P(¬A|B)', fc='#FFEBEE', ec='#D32F2F')
node(8, 2.7, 'P(A∩B)', fc='#C8E6C9', ec='#2E7D32')            # joint leaves
node(8, 1.3, 'P(¬A∩B)', fc='#FFCDD2', ec='#B71C1C')

# branch arrows
arrow(1.45, 2, 3.55, 2.7, '× P(A|B)')
arrow(1.45, 2, 3.55, 1.3, '× P(¬A|B)')
# joint arrows
arrow(4.45, 2.7, 7.55, 2.7)
arrow(4.45, 1.3, 7.55, 1.3)

# ----------------------------------------------------------
# 3.  BAYES  RULE  CALLOUT
# ----------------------------------------------------------
ax.text(5, 0.3, 'Joint = Branch × Root\nP(A ∩ B) = P(A|B) · P(B)',
        ha='center', va='center', fontsize=11, weight='bold',
        bbox=dict(boxstyle="round,pad=0.4", facecolor='white', edgecolor='#333'))

# ----------------------------------------------------------
# 4.  TITLE
# ----------------------------------------------------------
ax.set_title('Fig. 5.7  Bayes tree – branches multiply, leaves add',
             fontsize=11, pad=15)

# ----------------------------------------------------------
# 5.  SAVE
# ----------------------------------------------------------
plt.tight_layout()
plt.savefig('fig5_7_bayes_tree.png', dpi=300, transparent=True)
plt.close()
print('Figure 5.7 saved → fig5_7_bayes_tree.png')