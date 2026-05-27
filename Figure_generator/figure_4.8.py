#!/usr/bin/env python3
# fig4_8_leakage.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# ------------------------------------------------------------------
# 1.  OPEN DATA  (Titanic – we'll treat 'survived' as target)
# ------------------------------------------------------------------
df = sns.load_dataset('titanic')

# ------------------------------------------------------------------
# 2.  TARGET + NUMERIC FEATURES ONLY (demo)
# ------------------------------------------------------------------
target = 'survived'
num_cols = ['age', 'fare', 'parch', 'sibsp', 'pclass']
corr_df = df[num_cols + [target]].corr()[[target]].sort_values(target, ascending=False)

# ------------------------------------------------------------------
# 3.  PLOT
# ------------------------------------------------------------------
plt.figure(figsize=(6, 4), dpi=300)
ax = sns.heatmap(
        corr_df,
        annot=True,
        fmt=".2f",
        cmap='RdBu_r',
        center=0,
        cbar_kws={'label': 'Pearson r'},
        linewidths=.5)
plt.title('Fig. 4.8  Feature-target correlation (leakage check)', pad=10)
plt.xlabel(''); plt.ylabel('')
plt.tight_layout()

# ------------------------------------------------------------------
# 4.  SAVE
# ------------------------------------------------------------------
plt.savefig('fig4_8_leakage.png', dpi=300, bbox_inches='tight')
plt.close()
print('Figure 4.8 saved → fig4_8_leakage.png')