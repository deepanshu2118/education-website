# fig4_6_box.py  –  horizontal box-plots with red outlier dots
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# ------------------------------------------------------------------
# 1.  ANY OPEN DATASET  (Titanic used here)
# ------------------------------------------------------------------
df = sns.load_dataset('titanic')[['age', 'fare', 'parch', 'sibsp']]

# ------------------------------------------------------------------
# 2.  PLOT
# ------------------------------------------------------------------
plt.figure(figsize=(8, 2.5), dpi=300)
ax = sns.boxplot(data=df, orient='h', palette='Set2', linewidth=1.2)

# colour outlier markers red  (FlierProps)
for artist in ax.lines:
    # seaborn boxplot uses Line2D objects; outliers are the diamond markers
    if artist.get_marker() in ['d', 'o']:          # diamond or circle
        artist.set_color('#D32F2F')
        artist.set_markersize(4)

plt.title('Fig. 4.6  Box-plot outlier illustration', pad=10, fontsize=11)
plt.xlabel('Value (units)')
plt.tight_layout()

# ------------------------------------------------------------------
# 3.  SAVE
# ------------------------------------------------------------------
plt.savefig('fig4_6_box.png', dpi=300, bbox_inches='tight')
plt.close()
print('Figure 4.6 saved → fig4_6_box.png')