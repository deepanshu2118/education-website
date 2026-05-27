# fig4_4_radar.py
import numpy as np
import matplotlib.pyplot as plt
from math import pi

# ---------- 1.  DATA  ----------
labels = ['Accuracy', 'Completeness', 'Consistency', 'Timeliness',
          'Validity', 'Uniqueness', 'Representativeness']

# Dataset A (good quality)
A = np.array([90, 85, 88, 92, 90, 95, 70])
# Dataset B (poor quality)
B = np.array([60, 55, 65, 50, 60, 70, 40])

# ---------- 2.  ANGLES FOR EACH AXIS  ----------
num_vars = len(labels)
angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
angles += angles[:1]  # complete the circle

A = np.concatenate((A, [A[0]]))  # close curve
B = np.concatenate((B, [B[0]]))

# ---------- 3.  INIT PLOT  ----------
fig, ax = plt.subplots(figsize=(4, 4), dpi=300, subplot_kw=dict(projection='polar'))
fig.patch.set_facecolor('white')
ax.set_theta_offset(pi / 2)      # put first axis on top
ax.set_theta_direction(-1)       # clockwise
ax.set_rscale('linear')
ax.set_ylim(0, 100)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20', '40', '60', '80', '100'], fontsize=9)
ax.grid(True, color='grey', alpha=0.3)

# ---------- 4.  PLOT DATA  ----------
ax.plot(angles, A, 'o-', linewidth=2, label='Dataset A (good)', color='#2E7D32')
ax.fill(angles, A, alpha=0.25, color='#2E7D32')

ax.plot(angles, B, 'o-', linewidth=2, label='Dataset B (poor)', color='#D32F2F')
ax.fill(angles, B, alpha=0.25, color='#D32F2F')

# ---------- 5.  LABELS  ----------
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=10)
fig.legend(loc='upper right', bbox_to_anchor=(1.15, 1.05), frameon=False)

# ---------- 6.  SAVE  ----------
plt.tight_layout()
plt.savefig('fig4_4_radar.png', dpi=300, bbox_inches='tight')
plt.close()
print("Figure 4.4 saved → fig4_4_radar.png")