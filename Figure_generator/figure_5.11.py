#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Arrow

# ----------------------------------------------------------
# 1.  FIGURE  (wide landscape)
# ----------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 3), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis('off')

# ----------------------------------------------------------
# 2.  THREE  BOWLS  (nested composite)
# ----------------------------------------------------------
bowls = [
    {'xy': (1, 1.5), 'w': 1.8, 'h': 1.0, 'label': 'x', 'color': '#FF9800'},
    {'xy': (4, 1.3), 'w': 2.2, 'h': 1.2, 'label': 'u = f(x)', 'color': '#4CAF50'},
    {'xy': (7, 1.1), 'w': 2.6, 'h': 1.4, 'label': 'L = g(u)', 'color': '#2E7D32'}
]

for b in bowls:
    bowl = FancyBboxPatch(b['xy'], b['w'], b['h'],
                          boxstyle="round,pad=0.08", facecolor=b['color'], alpha=0.25,
                          edgecolor=b['color'], lw=2.5)
    ax.add_patch(bowl)
    ax.text(b['xy'][0] + b['w']/2, b['xy'][1] + b['h']/2, b['label'],
            ha='center', va='center', fontsize=12, weight='bold', color=b['color'])

# ----------------------------------------------------------
# 3.  CHAIN-RULE  ARROWS  (derivative flow)
# ----------------------------------------------------------
arrow_kw = dict(arrowstyle='->', lw=3, color='#424242')
ax.annotate('', xy=(2.8, 1.9), xytext=(1.8, 1.9), arrowprops=arrow_kw)
ax.text(2.3, 2.15, '∂u/∂x', ha='center', va='bottom', fontsize=11, weight='bold')

ax.annotate('', xy=(6.8, 1.9), xytext=(4.2, 1.9), arrowprops=arrow_kw)
ax.text(5.5, 2.15, '∂L/∂u', ha='center', va='bottom', fontsize=11, weight='bold')

# final chain
ax.annotate('', xy=(9.5, 1.9), xytext=(7.8, 1.9), arrowprops=arrow_kw)
ax.text(8.65, 2.15, '∂L/∂x = (∂L/∂u)·(∂u/∂x)', ha='center', va='bottom',
        fontsize=11, weight='bold', color='#D32F2F')

# ----------------------------------------------------------
# 4.  TITLE
# ----------------------------------------------------------
ax.set_title('Fig. 5.11  Chain-rule map – nested bowls: gradient = local slope × upstream slope',
             fontsize=11, pad=20)

# ----------------------------------------------------------
# 5.  SAVE
# ----------------------------------------------------------
plt.tight_layout()
plt.savefig('fig5_11_chain_bowls.png', dpi=300, transparent=True)
plt.close()
print('Figure 5.11 saved → fig5_11_chain_bowls.png')