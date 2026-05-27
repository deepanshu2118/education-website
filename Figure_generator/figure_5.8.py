#!/usr/bin/env python3
# fig5_8_dist_cards.py  –  six distribution cards on one page (300 dpi PNG)
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
from matplotlib.patches import FancyBboxPatch

# ----------------------------------------------------------
# 1.  PAGE SET-UP  (landscape A4  11.69 × 8.27 in)
# ----------------------------------------------------------
fig = plt.figure(figsize=(11.69, 8.27), dpi=300)
ax = fig.add_axes([0, 0, 1, 1], xlim=(0, 11.69), ylim=(0, 8.27))
ax.axis('off')

# ----------------------------------------------------------
# 2.  CARD  TEMPLATE
# ----------------------------------------------------------
def draw_card(x0, y0, title, pdf_name, x, y, use_case, color):
    """Draw one card at (x0, y0) inches"""
    w, h = 3.6, 2.4
    # rounded border
    box = FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.08",
                         facecolor='white', edgecolor=color, lw=2)
    ax.add_patch(box)
    # header
    ax.text(x0 + w/2, y0 + h - 0.25, title, ha='center', va='center',
            fontsize=13, weight='bold', color=color)
    # plot area
    ax2 = fig.add_axes([x0/11.69, (y0 + 0.35)/8.27, 2.8/11.69, 1.3/8.27])
    ax2.plot(x, y, lw=2.5, color=color)
    ax2.fill_between(x, y, alpha=0.2, color=color)
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.spines[:].set_visible(False)
    # use-case text
    ax.text(x0 + w/2, y0 + 0.18, use_case, ha='center', va='center',
            fontsize=10, style='italic', color='#424242')

# ----------------------------------------------------------
# 3.  DISTRIBUTION  DATA
# ----------------------------------------------------------
distributions = [
    ("Gaussian",    st.norm,      dict(loc=0, scale=1),   -4, 4, 0.1,
     "Linear models, least-squares, CLT", '#2E7D32'),
    ("Bernoulli",   st.bernoulli, dict(p=0.3),            0, 1, 1,
     "Logistic regression, cross-entropy", '#FF9800'),
    ("Multinomial", None,         None,                   0, 2, 1,
     "Naïve Bayes text classifiers", '#FFC107'),
    ("Poisson",     st.poisson,   dict(mu=4),             0, 12, 1,
     "Event counts, arrival rates", '#9C27B0'),
    ("Exponential", st.expon,     dict(scale=2),          0, 10, 0.2,
     "Time-between-events", '#3F51B5'),
    ("Power-law",   lambda x: x**(-1.5), None,            1, 20, 0.2,
     "Long-tail, log-transform first", '#795548')
]

# ----------------------------------------------------------
# 4.  POPULATE  CARDS  (2 rows × 3 columns)
# ----------------------------------------------------------
row_h, col_w = 2.6, 3.8
for idx, (name, dist, kw, x0, x1, dx, use, col) in enumerate(distributions):
    r, c = divmod(idx, 3)
    x_card = 0.6 + c * col_w
    y_card = 5.5 - r * row_h

    # special case: Multinomial (n=1 => categorical distribution)
    if name == "Multinomial":
        x = np.arange(3)  # categories 0, 1, 2
        y = np.array([0.3, 0.5, 0.2])
    else:
        x = np.arange(x0, x1 + dx, dx)  # always 1-D array

        # 1.  lambda functions (like Power-law)
        if callable(dist) and not hasattr(dist, 'pmf') and not hasattr(dist, 'pdf'):
            y = np.array([dist(xi) for xi in x])  # ensure same shape
        # 2.  discrete scipy distributions
        elif hasattr(dist, 'pmf'):
            y = dist.pmf(x, **kw)
        # 3.  continuous scipy distributions
        else:
            y = dist.pdf(x, **kw)

    draw_card(x_card, y_card, name, None, x, y, use, col)

# ----------------------------------------------------------
# 5.  PAGE  TITLE
# ----------------------------------------------------------
ax.text(11.69/2, 8.0, 'Fig. 5.8  Distribution cheat-sheet cards', ha='center',
        va='center', fontsize=16, weight='bold')

# ----------------------------------------------------------
# 6.  SAVE  PNG
# ----------------------------------------------------------
plt.savefig('fig5_8_dist_cards.png', dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.close()
print('Figure 5.8 saved → fig5_8_dist_cards.png')
