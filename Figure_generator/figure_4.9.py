#!/usr/bin/env python3
# fig4_9_aug_fixB.py  –  image-augmentation montage (offline)
import matplotlib.pyplot as plt
import torchvision.transforms as T
from skimage import data              # <<<  offline image source
from PIL import Image
import numpy as np

# ------------------------------------------------------------------
# 1.  OFFLINE IMAGE  (512×512 astronaut photo)
# ------------------------------------------------------------------
pil_img = Image.fromarray(data.astronaut())   # RGB already

# ------------------------------------------------------------------
# 2.  DEFINE AUGMENTATIONS
# ------------------------------------------------------------------
transforms = {
    "Original": T.Lambda(lambda x: x),
    "Horizontal flip": T.RandomHorizontalFlip(p=1),
    "Rotate 15°": T.RandomRotation(degrees=15),
    "Brightness ±20%": T.ColorJitter(brightness=0.2),
}

# ------------------------------------------------------------------
# 3.  BUILD 2×2 GRID
# ------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(6, 4.5), dpi=300)
axes = axes.flatten()

for idx, (name, T_fn) in enumerate(transforms.items()):
    aug = T_fn(pil_img)
    ax = axes[idx]
    ax.imshow(aug)
    ax.set_title(name, fontsize=10)
    ax.axis("off")

plt.suptitle("Fig. 4.9  Image augmentation montage", fontsize=11)
plt.tight_layout()

# ------------------------------------------------------------------
# 4.  SAVE
# ------------------------------------------------------------------
plt.savefig("fig4_9_aug.png", dpi=300, bbox_inches="tight")
plt.close()
print("Figure 4.9 saved → fig4_9_aug.png")