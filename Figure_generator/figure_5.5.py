#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, Circle

# ----------------------------------------------------------
# 1.  RAFFLE PARAMETERS
# ----------------------------------------------------------
total_tickets = 100
win_tickets   = 3
lose_tickets  = total_tickets - win_tickets
p_win = win_tickets / total_tickets

# ----------------------------------------------------------
# 2.  FIGURE  (wide strip)
# ----------------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 1.8), dpi=300)
ax.set_xlim(0, total_tickets)
ax.set_ylim(0, 3)
ax.axis('off')

# ----------------------------------------------------------
# 3.  DRAW  TICKETS  (small squares)
# ----------------------------------------------------------
for i in range(total_tickets):
    color = '#FFC107' if i < win_tickets else '#E0E0E0'
    ax.add_patch(Rectangle((i, 0.5), 1, 1.2, facecolor=color, edgecolor='white', lw=0.3))

# ----------------------------------------------------------
# 4.  JAR  OUTLINE  (glass silhouette)
# ----------------------------------------------------------
jar = Circle(xy=(total_tickets/2, 1.1), radius=total_tickets/2 + 8,
             facecolor='none', edgecolor='#424242', lw=3)
ax.add_patch(jar)

# ----------------------------------------------------------
# 5.  PROBABILITY  CALLOUT
# ----------------------------------------------------------
ax.annotate('', xy=(win_tickets/2, 2.2), xytext=(win_tickets/2, 1.7),
            arrowprops=dict(arrowstyle='->', lw=2, color='#D32F2F'))
ax.text(win_tickets/2, 2.35, f'P(win) = {p_win} = {win_tickets}/{total_tickets}',
        ha='center', va='bottom', fontsize=11, weight='bold', color='#D32F2F')

# ----------------------------------------------------------
# 6.  TITLE
# ----------------------------------------------------------
ax.set_title('Fig. 5.5  Raffle jar – probability as a proportion of tickets',
             fontsize=11, pad=20)

# ----------------------------------------------------------
# 7.  SAVE
# ----------------------------------------------------------
plt.tight_layout()
plt.savefig('fig5_5_raffle_strip.png', dpi=300, transparent=True)
plt.close()
print('Figure 5.5 saved → fig5_5_raffle_strip.png')