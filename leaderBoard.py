import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from assets.student_data import get_data
from datetime import datetime

# ==========================
# Load and Prepare Data
# ==========================
data = get_data()
print("📊 Raw data:", data)   # Debugging
df = pd.DataFrame(data)

df = df.sort_values(by="Solved this week", ascending=False).reset_index(drop=True)
df["Rank"] = df.index + 1

# (Optional) only take top 10 students
df = df.head(10)

print("✅ DataFrame Loaded:")
print(df)

# ==========================
# Setup Background Image
# ==========================
bg_img_path = "assets/background.png"
img = Image.open(bg_img_path).convert("RGBA")
draw = ImageDraw.Draw(img)

# ==========================
# Font Loader Helper
# ==========================
def load_font(fonts, size):
    """Try multiple font options and fall back to default if unavailable."""
    for f in fonts:
        try:
            return ImageFont.truetype(f, size)
        except:
            continue
    return ImageFont.load_default()

# Fonts
rank_font   = load_font(["arialbd.ttf", "DejaVuSans-Bold.ttf"], 30)
name_font   = load_font(["arial.ttf", "DejaVuSans.ttf"], 28)
score_font  = load_font(["consola.ttf", "DejaVuSansMono.ttf"], 26)
label_font  = load_font(["arial.ttf", "DejaVuSans.ttf"], 18)
header_font = load_font(["arialbd.ttf", "DejaVuSans-Bold.ttf"], 34)
badge_font  = load_font(["arialbd.ttf", "DejaVuSans-Bold.ttf"], 20)

# ==========================
# Gradient Parallelogram Box
# ==========================
def draw_gradient_parallelogram(base_img, x, y, w, h, offset, color1, color2):
    """Draw a gradient parallelogram background for leaderboard entries."""
    gradient = Image.new("RGB", (w, h), color=0)
    for i in range(h):
        ratio = i / h
        r = int(color1[0]*(1-ratio) + color2[0]*ratio)
        g = int(color1[1]*(1-ratio) + color2[1]*ratio)
        b = int(color1[2]*(1-ratio) + color2[2]*ratio)
        for j in range(w):
            gradient.putpixel((j, i), (r, g, b))

    # Mask parallelogram shape
    mask = Image.new("L", (w, h), 0)
    mask_draw = ImageDraw.Draw(mask)
    pts = [(offset, 0), (w, 0), (w-offset, h), (0, h)]
    mask_draw.polygon(pts, fill=255)

    base_img.paste(gradient, (x, y), mask)
    return [(x+offset, y), (x+w, y), (x+w-offset, y+h), (x, y+h)]

# ==========================
# Layout Configurations
# ==========================
container_w = 620
container_h = 80
offset = 30
row_gap_y = 30
start_y = 250
left_x = 90
right_x = 750
c1, c2 = (0, 90, 200), (120, 180, 255)  # gradient colors

# ==========================
# Header
# ==========================
header_text = "Data Structure and Algorithm"
img_w, img_h = img.size
draw.text((img_w/2, 190), header_text, font=header_font, fill="black", anchor="mm")

# ==========================
# Leaderboard Entries
# ==========================
for i, row in df.iterrows():
    col = 0 if i < 5 else 1
    pos_in_col = i if i < 5 else i-5
    x = left_x if col == 0 else right_x
    y = start_y + pos_in_col * (container_h + row_gap_y)
    
    # Draw entry background
    pts = draw_gradient_parallelogram(img, x, y, container_w, container_h, offset, c1, c2)
    draw.polygon(pts, outline="black")
    
    # --- Add special label for first card in each column ---
    if (col == 0 and i == 0) or (col == 1 and i == 5):
        badge_text = "solved this week / solved so far"

        # ✅ Use font.getbbox instead of draw.textsize
        bbox = badge_font.getbbox(badge_text)
        badge_w = bbox[2] - bbox[0]
        badge_h = bbox[3] - bbox[1]

        badge_x = x + container_w - 20
        badge_y = y - 5

        # Background rectangle
        draw.rectangle(
            (badge_x - badge_w - 15, badge_y, badge_x, badge_y + badge_h + 8),
            fill=(255, 215, 0), outline="black", width=2
        )

        # Text inside badge
        draw.text(
            (badge_x - 8, badge_y + badge_h/2 + 2),
            badge_text, font=badge_font, fill="black", anchor="rm"
        )
    
    # Text details
    rank_text   = f"#{row['Rank']}"
    name_text   = f"{row['Student']}"
    batch_text  = f"[{row['Batch']}]"
    score_text  = f"{row['Solved this week']} / {row['Total solved']}"
    
    # Text placements
    draw.text((x+55, y+container_h/2), rank_text, font=rank_font, fill="black", anchor="lm")
    draw.text((x+130, y+container_h/2), name_text, font=name_font, fill="black", anchor="lm")
    draw.text((x+330, y+container_h/2), batch_text, font=name_font, fill="black", anchor="lm")
    
    # Score with label (stacked, aligned right)
    draw.text((x+container_w-60, y+container_h/2), score_text, font=score_font, fill="black", anchor="rm")

# ==========================
# Save Output
# ==========================
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

date_str = datetime.now().strftime("%Y-%m-%d")
output_path = os.path.join(output_dir, f"DSA_Leaderboard_{date_str}_CodingAge.png")

img.save(output_path)
print(f"✅ Leaderboard saved at: {output_path}")
