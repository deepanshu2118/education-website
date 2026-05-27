#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch

# ----------------------------------------------------------
# 1.  CREATE  A  SIMPLE  2-D  LANDSCAPE  (loss surface)
# ----------------------------------------------------------
x = np.linspace(-3, 3, 400)
y = 0.15 * x ** 4 - 1.2 * x ** 2 + 0.5 * x + 2          # non-convex bowl
dy = 0.6 * x ** 3 - 2.4 * x + 0.5                         # analytic gradient

# ----------------------------------------------------------
# 2.  FIGURE
# ----------------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 3.5), dpi=300)

# ----------------------------------------------------------
# 3.  DRAW  SURFACE  (filled area under curve)
# ----------------------------------------------------------
ax.fill_between(x, y, alpha=0.25, color='#81C784')
ax.plot(x, y, lw=2.5, color='#2E7D32', label='Loss surface L(w)')

# ----------------------------------------------------------
# 4.  FOG  EFFECT  (semi-transparent white overlay)
# ----------------------------------------------------------
ax.fill_between(x, y, 6, alpha=0.7, color='white', zorder=3)

# ----------------------------------------------------------
# 5.  CLIMBER  (circle) +  GRADIENT  ARROW
# ----------------------------------------------------------
w0 = 2.1
loss0 = 0.15 * w0 ** 4 - 1.2 * w0 ** 2 + 0.5 * w0 + 2
grad0 = 0.6 * w0 ** 3 - 2.4 * w0 + 0.5
step_size = 0.4
delta_w = -grad0 * step_size

# climber
ax.add_patch(Circle((w0, loss0), 0.08, color='#D32F2F', zorder=5))
# gradient arrow (direction only, not length)
ax.annotate('', xy=(w0 + delta_w, loss0 - 0.2), xytext=(w0, loss0),
            arrowprops=dict(arrowstyle='->', lw=3, color='#D32F2F'))
ax.text(w0 + 0.15, loss0 + 0.15, 'Climber\n(feels gradient)', ha='left', va='center',
        fontsize=9, weight='bold', color='#D32F2F')

# ----------------------------------------------------------
# 6.  DECORATIVE  ELEMENTS
# ----------------------------------------------------------
# valley minimum (invisible to climber)
w_min = -1.7
loss_min = 0.15 * w_min ** 4 - 1.2 * w_min ** 2 + 0.5 * w_min + 2
ax.plot(w_min, loss_min, 'o', ms=9, color='#2E7D32', zorder=4)
ax.text(w_min, loss_min - 0.25, 'Minimum\n(hidden by fog)', ha='center', va='top',
        fontsize=9, style='italic', color='#2E7D32')

# ----------------------------------------------------------
# 7.  AXES  LABELS
# ----------------------------------------------------------
ax.set_xlabel('Weight  w', fontsize=11)
ax.set_ylabel('Loss  L(w)', fontsize=11)
ax.set_title('Fig. 5.10  Hill-climbing in fog – gradient points to steepest descent',
             fontsize=11, pad=15)
ax.legend(loc='upper right', frameon=False)
ax.grid(alpha=0.25)

# ----------------------------------------------------------
# 8.  SAVE
# ----------------------------------------------------------
plt.tight_layout()
plt.savefig('fig5_10_hill_climb.png', dpi=300, transparent=True)
plt.close()
print('Figure 5.10 saved → fig5_10_hill_climb.png')