#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# ----------------------------------------------------------
# 1.  SAME 30 STUDENTS AS FIG 5.3
# ----------------------------------------------------------
rng = np.random.default_rng(5)
base = 160
heights = np.round(base + rng.normal(0, 8, 30)).astype(int)
heights = np.clip(heights, 145, 190)
heights.sort()

mean_h = heights.mean()
std_h  = heights.std()

# ----------------------------------------------------------
# 2.  FIGURE
# ----------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 3), dpi=300)
ax.set_xlim(143, 193)
ax.set_ylim(-0.5, 2.2)
ax.axis('off')

# ----------------------------------------------------------
# 3.  DRAW  STUDENTS  (same stick style)
# ----------------------------------------------------------
for x in heights:
    ax.scatter(x, 1.75, s=80, color='#1976D2', zorder=3)
    ax.plot([x, x], [1.75, 1.1], lw=2, color='#1976D2')
    ax.plot([x, x-0.2], [1.1, 0.8], lw=2, color='#1976D2')
    ax.plot([x, x+0.2], [1.1, 0.8], lw=2, color='#1976D2')

# ----------------------------------------------------------
# 4.  MEAN  ±1  SD  SHADING  &  ERROR BAR
# ----------------------------------------------------------
# shaded band
ax.axvspan(mean_h - std_h, mean_h + std_h, ymin=0, ymax=1.9,
           alpha=0.25, color='#2E7D32', label='±1 SD')
# error-bar glyph (centered on mean)
ax.errorbar(mean_h, 2.05, xerr=std_h, fmt='none', lw=4,
            ecolor='#2E7D32', capsize=8, capthick=3)

# text
ax.text(mean_h, 2.15, f'Mean ± 1 SD = {mean_h:.1f} ± {std_h:.1f} cm',
        ha='center', va='bottom', fontsize=10, weight='bold', color='#2E7D32')

# ----------------------------------------------------------
# 5.  RULE-OF-THUMB  CALLOUT
# ----------------------------------------------------------
ax.text(170, 0.4, '≈ 68 % of students fall inside the green band\n(empirical rule for normal-like data)',
        ha='left', va='center', fontsize=9, color='#2E7D32',
        bbox=dict(boxstyle="round,pad=0.3", facecolor='white', edgecolor='#2E7D32'))

# ----------------------------------------------------------
# 6.  TITLE
# ----------------------------------------------------------
ax.set_title('Fig. 5.4  Heights with ±1 standard deviation (empirical 68 % rule)',
             fontsize=11, pad=20)

# ----------------------------------------------------------
# 7.  SAVE
# ----------------------------------------------------------
plt.tight_layout()
plt.savefig('fig5_4_errorbar.png', dpi=300, transparent=True)
plt.close()
print('Figure 5.4 saved → fig5_4_errorbar.png')