#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Rectangle

# ----------------------------------------------------------
# 1.  SYNTHETIC 30-STUDENT HEIGHTS (cm)
# ----------------------------------------------------------
rng = np.random.default_rng(5)
base = 160
heights = np.round(base + rng.normal(0, 8, 30)).astype(int)
heights = np.clip(heights, 145, 190)          # keep realistic range
heights.sort()

mean_h  = heights.mean()
median_h = np.median(heights)
mode_h   = pd.Series(heights).mode()[0]

# ----------------------------------------------------------
# 2.  FIGURE
# ----------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 3), dpi=300)
ax.set_xlim(143, 193)
ax.set_ylim(-0.5, 2.2)
ax.axis('off')

# ----------------------------------------------------------
# 3.  DRAW  EACH  STUDENT  (stick figure + height label)
# ----------------------------------------------------------
for x in heights:
    # head
    ax.scatter(x, 1.75, s=80, color='#1976D2', zorder=3)
    # body
    ax.plot([x, x], [1.75, 1.1], lw=2, color='#1976D2')
    # legs
    ax.plot([x, x-0.2], [1.1, 0.8], lw=2, color='#1976D2')
    ax.plot([x, x+0.2], [1.1, 0.8], lw=2, color='#1976D2')
    # height label (tiny)
    ax.text(x, 1.9, str(x), ha='center', va='bottom', fontsize=7, color='black')

# ----------------------------------------------------------
# 4.  MEAN, MEDIAN, MODE  LINES  +  SHADING
# ----------------------------------------------------------
def add_stat_line(val, color, label):
    ax.axvline(val, 0, 1.9, color=color, lw=3)
    ax.text(val, 2.0, f'{label} = {val:.1f} cm', ha='center', va='bottom',
            fontsize=9, weight='bold', color=color)

add_stat_line(mean_h,  '#2E7D32', 'Mean')
add_stat_line(median_h, '#FF9800', 'Median')
add_stat_line(mode_h,  '#9C27B0', 'Mode')

# ----------------------------------------------------------
# 5.  TITLE
# ----------------------------------------------------------
ax.set_title('Fig. 5.3  Class-photo heights (n = 30) – mean, median, mode',
             fontsize=11, pad=20)

# ----------------------------------------------------------
# 6.  SAVE
# ----------------------------------------------------------
plt.tight_layout()
plt.savefig('fig5_3_height_line.png', dpi=300, transparent=True)
plt.close()
print('Figure 5.3 saved → fig5_3_height_line.png')