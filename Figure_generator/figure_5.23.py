#!/usr/bin/env python3
# fig5_23_bootstrap_bar.py  –  Bootstrap CI demo (Figure 5.23)
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# ----------------------------------------------------------
# 1.  ORIGINAL  SAMPLE
# ----------------------------------------------------------
rng = np.random.default_rng(42)
n_orig = 30
sample = rng.normal(loc=50, scale=8, size=n_orig)   # unknown mean

# ----------------------------------------------------------
# 2.  BOOTSTRAP  RE-SAMPLES  (percentile method)
# ----------------------------------------------------------
n_boot = 1000
boot_means = [np.mean(rng.choice(sample, size=n_orig, replace=True))
              for _ in range(n_boot)]
boot_means = np.array(boot_means)

# confidence interval
ci_lower = np.percentile(boot_means, 2.5)
ci_upper = np.percentile(boot_means, 97.5)
mean_est = np.mean(boot_means)

# ----------------------------------------------------------
# 3.  FIGURE  (2-panel: histogram + bar)
# ----------------------------------------------------------
fig, (ax_hist, ax_bar) = plt.subplots(1, 2, figsize=(7, 3), dpi=300)

# ----------------------------------------------------------
# 4.  HISTOGRAM  OF  BOOTSTRAP  MEANS
# ----------------------------------------------------------
ax_hist.hist(boot_means, bins=40, density=True, alpha=0.7, color='#2E7D32', edgecolor='white')
ax_hist.axvline(ci_lower, 0, 1, ls='--', lw=2, color='#D32F2F', label='2.5 %')
ax_hist.axvline(mean_est, 0, 1, ls='-', lw=2, color='black', label='Bootstrap mean')
ax_hist.axvline(ci_upper, 0, 1, ls='--', lw=2, color='#D32F2F', label='97.5 %')
ax_hist.set_xlabel('Bootstrap sample mean', fontsize=10)
ax_hist.set_ylabel('Density', fontsize=10)
ax_hist.set_title('Bootstrap distribution (n=1000)', fontsize=11, weight='bold')
ax_hist.legend(frameon=False, fontsize=9)
ax_hist.grid(alpha=0.25)

# ----------------------------------------------------------
# 5.  CONFIDENCE  BAR  (visual summary)
# ----------------------------------------------------------
ax_bar.add_patch(Rectangle((ci_lower, 0.2), ci_upper - ci_lower, 0.6,
                           facecolor='#81C784', edgecolor='#2E7D32', lw=2))
ax_bar.errorbar(mean_est, 0.5, xerr=[[mean_est - ci_lower], [ci_upper - mean_est]],
                fmt='none', ecolor='black', capsize=8, capthick=2.5)
ax_bar.set_xlim(ci_lower - 2, ci_upper + 2)
ax_bar.set_ylim(0, 1)
ax_bar.set_xlabel('Mean estimate ± 95 % CI', fontsize=10)
ax_bar.set_title('Confidence interval bar', fontsize=11, weight='bold')
ax_bar.set_yticks([])
ax_bar.grid(axis='x', alpha=0.25)

# ----------------------------------------------------------
# 6.  PAGE  TITLE
# ----------------------------------------------------------
fig.text(0.5, 0.92, 'Fig. 5.23',
         ha='center', va='center', fontsize=13, weight='bold')

# ----------------------------------------------------------
# 7.  SAVE  PNG
# ----------------------------------------------------------
plt.tight_layout()
plt.savefig('fig5_23_bootstrap_bar.png', dpi=300, transparent=True)
plt.close()
print('Figure 5.23 saved → fig5_23_bootstrap_bar.png')