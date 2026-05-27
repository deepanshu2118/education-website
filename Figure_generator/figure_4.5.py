import seaborn as sns, matplotlib.pyplot as plt
df = sns.load_dataset('titanic')   # demo dataset
plt.figure(figsize=(10,3),dpi=300)
sns.heatmap(df.isnull(),cbar=False,cmap='Greys',yticklabels=False)
plt.title('Fig. 4.5  Missing values (grey) across Titanic variables')
plt.tight_layout(); plt.savefig('fig4_5_missingness.png')