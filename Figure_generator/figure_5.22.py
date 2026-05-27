#!/usr/bin/env python3
# fig5_22_lln_demo.py  –  Law of Large Numbers simulation (Figure 5.22)
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------------------
# 1.  EXPERIMENT  SET-UP
# ----------------------------------------------------------
rng = np.random.default_rng(42)
n_max = 10_000
experiments = {
    'Fair coin': rng.integers(0, 2, n_max),          # 0/1  p=0.5
    'Die roll':  rng.integers(1, 7, n_max),          # 1-6  mean=3.5
    'Gaussian':  rng.normal(0, 1, n_max)             # mean=0
}

theoretical = {'Fair coin': 0.5, 'Die roll': 3.5, 'Gaussian': 0.0}

# ----------------------------------------------------------
# 2.  RUNNING  MEAN  CALCULATION
# ----------------------------------------------------------
def running_mean(x):
    return np.cumsum(x) / np.arange(1, len(x) + 1)

results = {name: running_mean(seq) for name, seq in experiments.items()}

# ----------------------------------------------------------
# 3.  FIGURE  (3-panel row)
# ----------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(9, 3), dpi=300)
axes = axes.flatten()
colours = ['#2E7D32', '#FF9800', '#9C27B0']

for ax, (name, seq), mu, col in zip(axes, experiments.items(), theoretical.values(), colours):
    n = np.arange(1, len(seq) + 1)
    ax.plot(n, results[name], lw=1.8, color=col, label='Running mean')
    ax.axhline(mu, 0, 1, ls='--', lw=2, color=col, alpha=0.7, label=f'Theoretical = {mu}')
    ax.set_xlabel('Number of trials  n', fontsize=10)
    ax.set_ylabel('Sample mean', fontsize=10)
    ax.set_title(f'{name}', fontsize=11, weight='bold')
    ax.grid(alpha=0.25)
    ax.legend(frameon=False, fontsize=9)

# ----------------------------------------------------------
# 4.  PAGE  TITLE
# ----------------------------------------------------------
fig.text(0.5, 0.92, 'Fig. 5.22',
         ha='center', va='center', fontsize=13, weight='bold')

# ----------------------------------------------------------
# 5.  SAVE  PNG
# ----------------------------------------------------------
plt.tight_layout()
plt.savefig('fig5_22_lln_demo.png', dpi=300, transparent=True)
plt.close()
print('Figure 5.22 saved → fig5_22_lln_demo.png')