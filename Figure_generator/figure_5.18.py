#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle
import networkx as nx   # pip install networkx

# ----------------------------------------------------------
# 1.  CREATE  A  SIMPLE  GRAPH
# ----------------------------------------------------------
G = nx.Graph()
G.add_edges_from([(1,2),(1,3),(2,4),(3,4),(3,5),(4,5)])
pos = nx.spring_layout(G, seed=42)   # 2-D positions

# ----------------------------------------------------------
# 2.  FIGURE  (wide strip)
# ----------------------------------------------------------
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(8, 3), dpi=300)

# ----------------------------------------------------------
# 3.  LEFT  PANEL  –  NODES & EDGES  (CARTOON STYLE)
# ----------------------------------------------------------
ax_left.set_xlim(-1.2, 1.2)
ax_left.set_ylim(-1.2, 1.2)
ax_left.axis('off')

# nodes (coloured circles)
node_colours = ['#FF9800', '#4CAF50', '#9C27B0', '#2E7D32', '#3F51B5']
for node, (x, y) in pos.items():
    ax_left.add_patch(Circle((x, y), 0.12, fc=node_colours[node-1], ec='black', lw=2))
    ax_left.text(x, y, str(node), ha='center', va='center', fontsize=11, weight='bold')

# edges (pipes)
for (u, v) in G.edges():
    x1, y1 = pos[u]
    x2, y2 = pos[v]
    ax_left.plot([x1, x2], [y1, y2], lw=4, color='grey', alpha=0.7)

# labels
ax_left.text(0, 1.35, 'Nodes (entities)', ha='center', va='center', fontsize=11,
             bbox=dict(boxstyle="round,pad=0.3", facecolor='white', edgecolor='#333'))
ax_left.text(0, -1.35, 'Edges (relations)', ha='center', va='center', fontsize=11,
             bbox=dict(boxstyle="round,pad=0.3", facecolor='white', edgecolor='#333'))

# ----------------------------------------------------------
# 4.  RIGHT  PANEL  –  ADJACENCY  MATRIX  (GRID)
# ----------------------------------------------------------
ax_right.set_xlim(-0.5, 4.5)
ax_right.set_ylim(-0.5, 4.5)
ax_right.axis('off')

A = nx.to_numpy_array(G)
n = A.shape[0]
for i in range(n):
    for j in range(n):
        colour = node_colours[i] if A[i, j] else 'white'
        ax_right.add_patch(Rectangle((j, n-1-i), 1, 1, facecolor=colour, lw=1.5, ec='black'))
        ax_right.text(j + 0.5, n-1-i + 0.5, int(A[i, j]), ha='center', va='center',
                      fontsize=12, weight='bold', color='black' if A[i, j] else 'grey')

ax_right.set_xticks(np.arange(n) + 0.5)
ax_right.set_xticklabels(range(1, n+1))
ax_right.set_yticks(np.arange(n) + 0.5)
ax_right.set_yticklabels(range(1, n+1)[::-1])
ax_right.set_xlabel('Node j', fontsize=10)
ax_right.set_ylabel('Node i', fontsize=10)
ax_right.set_title('Adjacency matrix A', fontsize=11, pad=8)

# ----------------------------------------------------------
# 5.  PAGE  TITLE
# ----------------------------------------------------------
fig.text(0.5, 0.92, 'Fig. 5.18  Graph = nodes + edges  (and its matrix)',
         ha='center', va='center', fontsize=13, weight='bold')

# ----------------------------------------------------------
# 6.  SAVE
# ----------------------------------------------------------
plt.tight_layout()
plt.savefig('fig5_18_graph_intro.png', dpi=300, transparent=True)
plt.close()
print('Figure 5.18 saved → fig5_18_graph_intro.png')