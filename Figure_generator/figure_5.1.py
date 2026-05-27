#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------------------
# 1.  DATA  (simple line y = m x + b)
# ----------------------------------------------------------
m = 1.5               # slope knob
b = 1.0               # intercept
x = np.linspace(-1, 3, 100)
y = m * x + b

# ----------------------------------------------------------
# 2.  FIGURE  (no axes, clean illustration)
# ----------------------------------------------------------
fig, ax = plt.subplots(figsize=(5, 3.5), dpi=300)
ax.set_xlim(-1.2, 3.2)
ax.set_ylim(-0.5, 5.5)
ax.axis('off')

# ----------------------------------------------------------
# 3.  DRAW  SEESAW  (line) +  SUPPORT  (triangle fulcrum)
# ----------------------------------------------------------
ax.plot(x, y, lw=4, color='#2E7D32')                       # seesaw plank
tri = plt.Polygon([[-0.3, 0], [0.3, 0], [0, -0.45]], closed=True, color='#424242')
ax.add_patch(tri)

# ----------------------------------------------------------
# 4.  ANNOTATE  KNOB  &  MOVEMENT  ARROWS
# ----------------------------------------------------------
ax.annotate('', xy=(1, m*1+b), xytext=(1, b),
            arrowprops=dict(arrowstyle='<->', lw=2, color='#D32F2F'))
ax.text(1.05, (m*1+b)/2, f'Δy = {m}·Δx', va='center', fontsize=11, color='#D32F2F')

ax.annotate('', xy=(0, b), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', lw=1.5, color='#757575'))
ax.text(-0.15, b/2, 'b', va='center', ha='right', fontsize=12, weight='bold')

# ----------------------------------------------------------
# 5.  TITLE
# ----------------------------------------------------------
ax.set_title('Fig. 5.1  The seesaw of linearity  –  slope m is the only learner knob',
             fontsize=11, pad=20)

# ----------------------------------------------------------
# 6.  SAVE
# ----------------------------------------------------------
plt.tight_layout()
plt.savefig('fig5_1_seesaw.png', dpi=300, transparent=True)
plt.close()
print('Figure 5.1 saved → fig5_1_seesaw.png')