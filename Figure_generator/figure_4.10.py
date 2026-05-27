#!/usr/bin/env python3
# fig4_10_text_aug.py
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# 1.  ORIGINAL SENTENCE & AUGMENTATIONS
# ------------------------------------------------------------------
original = "The movie was surprisingly good."

examples = {
    "Original":                          original,
    "Word-dropout":                      "The movie was ▁ good.",
    "Synonym swap":                      "The film was surprisingly great.",
    "Back-translation (round-trip)":     "The cinema was unexpectedly nice."
}

# ------------------------------------------------------------------
# 2.  BUILD FIGURE
# ------------------------------------------------------------------
fig, axes = plt.subplots(len(examples), 1, figsize=(6, 4), dpi=300,
                         gridspec_kw={'hspace': 0.6})
axes = axes.flatten()

for ax, (name, sent) in zip(axes, examples.items()):
    ax.text(0.05, 0.6, sent, fontsize=13, fontfamily='monospace',
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#f7f7f7", edgecolor="#cccccc"))
    ax.text(0.05, 0.15, name, fontsize=11, weight='bold', color="#333")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

plt.suptitle("Fig. 4.10  Text augmentation example", fontsize=12)
plt.tight_layout()

# ------------------------------------------------------------------
# 3.  SAVE
# ------------------------------------------------------------------
plt.savefig("fig4_10_text_aug.png", dpi=300, bbox_inches="tight")
plt.close()
print("Figure 4.10 saved → fig4_10_text_aug.png")