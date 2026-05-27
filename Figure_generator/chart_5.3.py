#!/usr/bin/env python3
# chart5_3_optimiser_card.py  –  optimiser cheat-card (Chart 5.3)
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# ----------------------------------------------------------
# 1.  PAGE  (portrait A4)
# ----------------------------------------------------------
fig = plt.figure(figsize=(8.27, 11.69), dpi=300)
ax = fig.add_axes([0, 0, 1, 1], xlim=(0, 8.27), ylim=(0, 11.69))
ax.axis('off')

# ----------------------------------------------------------
# 2.  HEADER
# ----------------------------------------------------------
ax.add_patch(FancyBboxPatch((0.5, 10.8), 7.27, 0.6, boxstyle="round,pad=0.05",
                            facecolor='#004d99', edgecolor='none'))
ax.text(8.27/2, 11.1, 'Chart 5.3  Optimiser cheat-card', ha='center', va='center',
        fontsize=18, weight='bold', color='white')

# ----------------------------------------------------------
# 3.  ROW  TEMPLATE
# ----------------------------------------------------------
def row(y, name, when, pro, con, color):
    h = 0.45
    # name box
    ax.add_patch(FancyBboxPatch((0.5, y), 1.8, h, boxstyle="round,pad=0.05",
                                facecolor=color, edgecolor=color, lw=1.5))
    ax.text(0.5 + 1.8/2, y + h/2, name, ha='center', va='center', fontsize=10,
            weight='bold', color='white')
    # when
    ax.add_patch(FancyBboxPatch((2.4, y), 1.9, h, boxstyle="round,pad=0.05",
                                facecolor='white', edgecolor=color, lw=1))
    ax.text(2.4 + 0.05, y + h/2, when, ha='left', va='center', fontsize=9)
    # pro
    ax.add_patch(FancyBboxPatch((4.4, y), 1.9, h, boxstyle="round,pad=0.05",
                                facecolor='white', edgecolor=color, lw=1))
    ax.text(4.4 + 0.05, y + h/2, pro, ha='left', va='center', fontsize=9)
    # con
    ax.add_patch(FancyBboxPatch((6.4, y), 1.3, h, boxstyle="round,pad=0.05",
                                facecolor='white', edgecolor=color, lw=1))
    ax.text(6.4 + 0.05, y + h/2, con, ha='left', va='center', fontsize=9)

# ----------------------------------------------------------
# 4.  COLUMN  HEADERS
# ----------------------------------------------------------
header_color = '#757575'
ax.text(1.4, 10.35, 'Optimiser', ha='center', va='center', fontsize=11, weight='bold', color='white')
ax.text(3.35, 10.35, 'When to use', ha='center', va='center', fontsize=11, weight='bold', color='white')
ax.text(5.35, 10.35, 'Pro', ha='center', va='center', fontsize=11, weight='bold', color='white')
ax.text(7.05, 10.35, 'Con', ha='center', va='center', fontsize=11, weight='bold', color='white')

# ----------------------------------------------------------
# 5.  DATA  ROWS  (y, name, when, pro, con, colour)
# ----------------------------------------------------------
rows = [
    (9.8,  'Batch GD',  'Small data, smooth loss',  'Stable convergence',  'Slow, memory hog',  '#2E7D32'),
    (9.25, 'SGD',  'Large data, noisy acceptable',  'Fast, memory lean',  'Chaotic updates',  '#FF9800'),
    (9.25-0.55, 'Momentum',  'SGD too noisy',  'Dampens oscillations',  'Extra hyper-param',  '#FFC107'),
    (9.25-1.1,  'AdaGrad',  'Sparse features (text)',  'Auto-scaled LR',  'LR decays to zero',  '#9C27B0'),
    (9.25-1.65, 'RMSprop',  'Non-stationary loss',  'Forgets old gradients',  'Still need momentum',  '#3F51B5'),
    (9.25-2.2,  'Adam',  'Default first choice',  'Robust, fast, well tuned',  'Generalisation gap*',  '#607D8B'),
    (9.25-2.75, 'L-BFGS',  'Small batch, smooth H',  'Quasi-Newton speed',  'Batch only, memory',  '#795548')
]

for r in rows:
    row(*r)

# ----------------------------------------------------------
# 6.  FOOTER  NOTE
# ----------------------------------------------------------
ax.text(4.1, 6.8, '*Use AdamW + weight decay + learning-rate schedule for best practice',
        ha='center', va='center', fontsize=9, style='italic', color='#424242')

# ----------------------------------------------------------
# 7.  PAGE  TITLE
# ----------------------------------------------------------
ax.text(4.1, 11.4, 'Chart 5.3  Optimiser cheat-card', ha='center', va='center',
        fontsize=16, weight='bold', color='#333')

# ----------------------------------------------------------
# 8.  SAVE  PNG
# ----------------------------------------------------------
plt.savefig('chart5_3_optimiser_card.png', dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.close()
print('Chart 5.3 saved → chart5_3_optimiser_card.png')