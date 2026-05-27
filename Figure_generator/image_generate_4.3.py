import matplotlib.pyplot as plt, numpy as np, pandas as pd
from sklearn.model_selection import train_test_split
# 10 000 points, 2 features, hidden income quartile
rng = np.random.default_rng(42)
income = rng.lognormal(10, 0.8, 10000)
df = pd.DataFrame({'x': rng.normal(0,1,10000)+income/1e5,
                   'y': rng.normal(0,1,10000)+income/1e4,
                   'q': pd.qcut(income,4,labels=False)})
fig,ax=plt.subplots(1,2,figsize=(2,1),dpi=300)

# (a) simple random
rsamp, _ = train_test_split(df, test_size=0.8, random_state=1)
ax[0].scatter(rsamp.x,rsamp.y,c='steelblue',s=4,alpha=0.7)
ax[0].set_title('(a) Simple random sample')

# (b) stratified
strat, _ = train_test_split(df, test_size=0.8, random_state=1, stratify=df.q)
cols=['tab:blue','tab:orange','tab:green','tab:red']
for q in range(4):
    sub=strat[strat.q==q]
    ax[1].scatter(sub.x,sub.y,c=cols[q],s=4,label=f'Q{q+1}')
ax[1].legend();ax[1].set_title('(b) Stratified by income quartile')
plt.tight_layout(); plt.savefig('fig4_3_sampling.png')