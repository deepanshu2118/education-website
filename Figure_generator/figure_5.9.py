#!/usr/bin/env python3
# fig5_9_surprise_bar.py  –  surprise vs probability (entropy intro)
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------------------
# 1.  DATA  (probability range 0.01 → 0.99)
# ----------------------------------------------------------
p = np.linspace(0.01, 0.99, 100)
surprise = -np.log2(p)          # bits

# ----------------------------------------------------------
# 2.  FIGURE
# ----------------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 3), dpi=300)

# ----------------------------------------------------------
# 3.  DRAW  SURPRISE  CURVE
# ----------------------------------------------------------
ax.plot(p, surprise, lw=3, color='#D32F2F', label='Surprise  −log₂ p')

# highlight three example bars
for prob, col in [(0.5, '#FF9800'), (0.25, '#FFC107'), (0.125, '#FFEB3B')]:
    h = -np.log2(prob)
    ax.bar(prob, h, width=0.03, color=col, edgecolor='black', lw=1)
    ax.text(prob, h + 0.15, f'{h:.1f}', ha='center', va='bottom', fontsize=9, weight='bold')

# ----------------------------------------------------------
# 4.  ENTROPY  OF  A  FAIR  COIN  (optional overlay)
# ----------------------------------------------------------
fair_p = 0.5
fair_h = -(fair_p * np.log2(fair_p) + fair_p * np.log2(fair_p))
ax.axhline(fair_h, 0, 1, color='#2E7D32', ls='--', lw=2, label=f'Entropy fair coin = {fair_h:.1f} bits')

# ----------------------------------------------------------
# 5.  COSMETICS
# ----------------------------------------------------------
ax.set_xlabel('Probability  p', fontsize=11)
ax.set_ylabel('Surprise  (bits)', fontsize=11)
ax.set_title('Fig. 5.9  Surprise bars – lower probability → higher "wow"  (entropy H = average surprise)',
             fontsize=11, pad=15)
ax.legend(loc='upper right', frameon=False)
ax.grid(alpha=0.25)

# ----------------------------------------------------------
# 6.  SAVE
# ----------------------------------------------------------
plt.tight_layout()
plt.savefig('fig5_9_surprise_bar.png', dpi=300, transparent=True)
plt.close()
print('Figure 5.9 saved → fig5_9_surprise_bar.png')