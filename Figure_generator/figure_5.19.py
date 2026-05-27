#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from sklearn.cluster import SpectralClustering

# ----------------------------------------------------------
# 1.  CREATE  A  TOY  GRAPH  (KARATE CLUB)
# ----------------------------------------------------------
G = nx.karate_club_graph()   # 34 nodes, two natural clubs
adj = nx.to_numpy_array(G)

# ----------------------------------------------------------
# 2.  SPECTRAL  EMBEDDING  (2-D  VIA  LAPLACIAN  EIGENVECTORS)
# ----------------------------------------------------------
sc = SpectralClustering(n_clusters=2, affinity='precomputed', random_state=42)
labels = sc.fit_predict(adj)

# Laplacian eigenvectors (smallest non-zero) for 2-D plot
L = nx.laplacian_matrix(G).toarray()
vals, vecs = np.linalg.eigh(L)
embed = vecs[:, 1:3]  # 2nd & 3rd smallest eigenvectors

# ----------------------------------------------------------
# 3.  FIGURE  (2-panel: graph + eigen-space)
# ----------------------------------------------------------
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(8, 3.5), dpi=300)

# ----------------------------------------------------------
# 4.  LEFT  –  ORIGINAL  GRAPH  (COLOURED  BY  CLUSTER)
# ----------------------------------------------------------
pos = nx.spring_layout(G, seed=42, k=2)
cols = np.array(['#2E7D32' if lbl == 0 else '#FF9800' for lbl in labels])

nx.draw(G, pos, ax=ax_left, node_color=cols, node_size=180, width=1.5,
        edge_color='grey', alpha=0.8, with_labels=False)
ax_left.set_title('Original graph', fontsize=11, pad=8)
ax_left.axis('off')

# ----------------------------------------------------------
# 5.  RIGHT  –  EIGEN-SPACE  (2-D  EMBED)
# ----------------------------------------------------------
for lbl in (0, 1):
    mask = labels == lbl
    ax_right.scatter(embed[mask, 0], embed[mask, 1],
                     c=cols[mask], s=80, edgecolors='black', linewidth=1,
                     label=f'Cluster {lbl+1}')
ax_right.set_xlabel(r'$\mathbf{v}_2$ (2nd eigenvector)', fontsize=10)
ax_right.set_ylabel(r'$\mathbf{v}_3$ (3rd eigenvector)', fontsize=10)
ax_right.set_title('Spectral embedding (Laplacian eigenvectors)', fontsize=11, pad=8)
ax_right.legend(frameon=False, loc='upper right')
ax_right.grid(alpha=0.25)
ax_right.set_aspect('equal')

# ----------------------------------------------------------
# 6.  CALLOUT  –  WHY  IT  WORKS
# ----------------------------------------------------------
fig.text(0.5, 0.92, 'Fig. 5.19  Spectral clustering – embed nodes via eigenvectors of Laplacian',
         ha='center', va='center', fontsize=13, weight='bold')

# ----------------------------------------------------------
# 7.  SAVE
# ----------------------------------------------------------
plt.tight_layout()
plt.savefig('fig5_19_spectral_embed.png', dpi=300, transparent=True)
plt.close()
print('Figure 5.19 saved → fig5_19_spectral_embed.png')
