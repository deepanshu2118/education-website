# import matplotlib.pyplot as plt

# plt.rcParams["text.usetex"] = True  # requires LaTeX installed (MiKTeX/TeX Live)

# matrix_latex = r"$A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$"

# fig, ax = plt.subplots()
# ax.axis("off")

# ax.text(0.5, 0.5, matrix_latex, fontsize=30, ha="center", va="center")

# plt.savefig("matrix.png", bbox_inches="tight", dpi=200)
# plt.show()



import numpy as np
import matplotlib.pyplot as plt

matrix = np.array([[1, -1, 3], [2, 5, 4]])
plt.matshow(matrix, cmap='gray')
plt.savefig("matrix_image.png")
