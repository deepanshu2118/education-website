#!/usr/bin/env python3
# fig4_13_datacard_jpg.py  –  blank Dataset Card  (JPG output)
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
import qrcode
from io import BytesIO
import pathlib   # add this line near the other imports


# ----------------------------------------------------------
# 1.  PAGE SET-UP  (A4 portrait 210 × 297 mm)
# ----------------------------------------------------------
WIDTH, HEIGHT = 8.27, 11.69  # inches (A4)
fig = plt.figure(figsize=(WIDTH, HEIGHT), dpi=300)
ax = fig.add_axes([0, 0, 1, 1], xlim=(0, WIDTH), ylim=(0, HEIGHT))
ax.axis('off')

# ----------------------------------------------------------
# 2.  BANNER  +  TITLE
# ----------------------------------------------------------
ax.add_patch(Rectangle((0, HEIGHT-1.1), WIDTH, 1.1, facecolor='#004d99', zorder=2))
ax.text(WIDTH/2, HEIGHT-0.55, 'Dataset Card  –  blank template', color='white',
        ha='center', va='center', fontsize=20, weight='bold')

# ----------------------------------------------------------
# 3.  QR CODE  (example repo)
# ----------------------------------------------------------
qr_url = "https://github.com/your-org/dataset-card-example"
qr = qrcode.make(qr_url, box_size=8, border=1)
qr_buffer = BytesIO()
qr.save(qr_buffer, format='PNG')
qr_buffer.seek(0)
qr_array = plt.imread(qr_buffer, format='png')
qr_ax = fig.add_axes([7.1, HEIGHT-0.95, 0.8, 0.8], anchor='NE')
qr_ax.imshow(qr_array, interpolation='nearest')
qr_ax.axis('off')

# ----------------------------------------------------------
# 4.  FORM FIELDS  (left & right columns)
# ----------------------------------------------------------
left_fields = [
    "Dataset name / version", "Contact / owner", "Collection date(s)",
    "Licence & permitted uses", "Known biases / limitations",
    "Checksum (SHA-256)", "Train / Val / Test sizes", "Source URL"
]

right_fields = [
    "Feature descriptions & types", "Target variable definition",
    "Missing-value % per column", "Label inter-annotator κ",
    "Ethics / IRB approval", "Update frequency",
    "Retention / deletion date", "Other notes"
]

y_start = HEIGHT - 1.8
dy = 0.55
box_height = 0.45
box_width = 3.6

def draw_box(ax, x, y, label):
    box = FancyBboxPatch((x, y), box_width, box_height,
                         boxstyle="round,pad=0.03", ec='#666', fc='#f7f7f7', lw=0.8)
    ax.add_patch(box)
    ax.text(x + 0.05, y + box_height/2, label, va='center', ha='left', fontsize=9, weight='bold')

# left column
for i, fld in enumerate(left_fields):
    draw_box(ax, 0.4, y_start - i*dy, fld)

# right column
for i, fld in enumerate(right_fields):
    draw_box(ax, 4.2, y_start - i*dy, fld)

# ----------------------------------------------------------
# 5.  BOTTOM SIGN-OFF STRIP
# ----------------------------------------------------------
ax.add_patch(Rectangle((0, 0.2), WIDTH, 0.2, facecolor='#e0e0e0', zorder=1))
ax.text(0.4, 0.28, "QA sign-off: ______________________   Date: ____________", fontsize=10)
ax.text(0.4, 0.12, "Next review date: ____________   Version hash: ______________________", fontsize=10)

# ----------------------------------------------------------
# 6.  SAVE AS HIGH-RES JPG
# ----------------------------------------------------------
# plt.savefig("fig4_13_datacard.jpg", dpi=300, bbox_inches='tight')
# plt.close()
# print("Figure 4.13 saved → fig4_13_datacard.png")


fig.canvas.draw()                       # flush all patches to renderer
fig.canvas.draw()                       # double draw保险
plt.savefig("fig4_13_datacard1.png", dpi=300, bbox_inches='tight')
print("Figure 4.13 saved →", pathlib.Path("fig4_13_datacard1.png").absolute())