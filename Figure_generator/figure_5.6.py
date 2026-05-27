#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle
from matplotlib_venn import venn2          # pip install matplotlib-venn

# ----------------------------------------------------------
# 1.  VENN DATA  (example counts)
# ----------------------------------------------------------
# Universe 1000 people
# A = owns cat, B = owns dog
total = 1000
only_cat = 350
only_dog = 250
both     = 150
neither  = total - (only_cat + only_dog + both)

# ----------------------------------------------------------
# 2.  FIGURE
# ----------------------------------------------------------
fig, ax = plt.subplots(figsize=(5, 4), dpi=300)
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.axis('off')

# ----------------------------------------------------------
# 3.  DRAW  VENN
# ----------------------------------------------------------
venn = venn2(subsets=(only_cat, only_dog, both),
             set_labels=('Owns cat (A)', 'Owns dog (B)'),
             ax=ax, alpha=0.75, normalize_to=1.0)
# colour
venn.get_patch_by_id('10').set_color('#FF9800')  # only A
venn.get_patch_by_id('01').set_color('#4CAF50')  # only B
venn.get_patch_by_id('11').set_color('#FFC107')  # intersection

# label sizes
for text in venn.set_labels: text.set_fontsize(10)
for text in venn.subset_labels: text.set_fontsize(9)

# ----------------------------------------------------------
# 4.  ANNOTATE  JOINT,  MARGINAL,  CONDITIONAL
# ----------------------------------------------------------
# joint  P(A ∩ B)
ax.annotate('Joint\nP(A ∩ B)', xy=(0, 0), ha='center', va='center', fontsize=9,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', edgecolor='#333'))

# marginal  P(A)
ax.annotate('Marginal\nP(A)', xy=(-0.7, 0.4), ha='center', va='center', fontsize=9,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', edgecolor='#333'))

# conditional  P(A|B) = both / B_total
p_a_given_b = both / (both + only_dog)
ax.annotate(f'Conditional\nP(A|B) = {p_a_given_b:.2f}', xy=(0.7, -0.4), ha='center', va='center',
            fontsize=9, bbox=dict(boxstyle="round,pad=0.3", facecolor='white', edgecolor='#D32F2F'))

# ----------------------------------------------------------
# 5.  TITLE
# ----------------------------------------------------------
ax.set_title('Fig. 5.6  Venn view: joint, marginal, conditional probability',
             fontsize=11, pad=25)

# ----------------------------------------------------------
# 6.  SAVE
# ----------------------------------------------------------
plt.tight_layout()
plt.savefig('fig5_6_venn.png', dpi=300, transparent=True)
plt.close()
print('Figure 5.6 saved → fig5_6_venn.png')