from PIL import Image, ImageDraw, ImageFont

bg_path = "assets/bg-hero.png"
logo_path = "assets/logo.png"
out_path = "assets/og-image.jpg"

# Open original background
bg = Image.open(bg_path).convert("RGBA")

# Resize to width 600 to keep it lightweight for WhatsApp
bg_w, bg_h = bg.size
ratio = 600 / float(bg_w)
new_h = int(float(bg_h) * float(ratio))
bg = bg.resize((600, new_h), Image.Resampling.LANCZOS)

# Create a dark overlay to make logo pop
overlay = Image.new('RGBA', bg.size, (0,0,0, 100))
bg = Image.alpha_composite(bg, overlay)

# Load logo
logo = Image.open(logo_path).convert("RGBA")

# Resize logo
logo_size = 140
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

# Composite logo
bg_w, bg_h = bg.size
logo_x = (bg_w - logo_size) // 2
logo_y = (bg_h - logo_size) // 2 - 40
bg.paste(logo, (logo_x, logo_y), mask=logo)

# Add text
draw = ImageDraw.Draw(bg)
text = "How2Burn"
try:
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 54)
except:
    font = ImageFont.load_default()

bbox = draw.textbbox((0, 0), text, font=font)
text_w = bbox[2] - bbox[0]
text_x = (bg_w - text_w) // 2
text_y = logo_y + logo_size + 20

# Text shadow
draw.text((text_x+2, text_y+2), text, font=font, fill=(0, 0, 0, 180))
draw.text((text_x, text_y), text, font=font, fill=(255, 255, 255, 255))

# Save
bg = bg.convert("RGB")
bg.save(out_path, format="JPEG", quality=65)
print(f"Saved {out_path}")
