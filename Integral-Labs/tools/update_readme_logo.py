from PIL import Image, ImageDraw, ImageFont
import os

ROOT = os.path.dirname(os.path.dirname(__file__))
ASSETS = os.path.join(ROOT, 'assets', 'images')
README_IMG = os.path.join(ROOT, 'readme-images', 'desktop.png')
BACKUP_IMG = os.path.join(ROOT, 'readme-images', 'desktop.original.png')
LOGO_PNG = os.path.join(ASSETS, 'logo-integral.png')

# Backup original README image
if not os.path.exists(BACKUP_IMG):
    if os.path.exists(README_IMG):
        Image.open(README_IMG).save(BACKUP_IMG)

# Create a simple PNG logo
logo_w, logo_h = 160, 50
logo = Image.new('RGBA', (logo_w, logo_h), (0,0,0,0))
d = ImageDraw.Draw(logo)
# Draw gold circle
d.ellipse((4,6,44,46), fill=(228,197,144,255))
# Draw text
try:
    font_large = ImageFont.truetype('arial.ttf', 18)
    font_small = ImageFont.truetype('arial.ttf', 10)
except Exception:
    font_large = ImageFont.load_default()
    font_small = ImageFont.load_default()

# White 'INTEGRAL'
d.text((52,10), 'INTEGRAL', font=font_large, fill=(255,255,255,255))
# Gold 'RESTAURANT'
d.text((52,28), 'RESTAURANT', font=font_small, fill=(228,197,144,255))

logo.save(LOGO_PNG)
print('Created', LOGO_PNG)

# Overlay onto README screenshot
if os.path.exists(README_IMG):
    bg = Image.open(README_IMG).convert('RGBA')
    # Paste position similar to screenshot (approx top-left)
    pos = (24, 24)
    bg.paste(logo, pos, logo)
    bg.save(README_IMG)
    print('Updated README screenshot:', README_IMG)
else:
    print('README image not found to update:', README_IMG)
