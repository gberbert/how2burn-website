import os
from PIL import Image

dirs = [
    'assets/painel',
    'assets/registrar',
    'assets/jornadas',
    'assets/configuracoes'
]

total_cropped = 0

for d in dirs:
    if not os.path.exists(d):
        continue
    for f in os.listdir(d):
        if f.endswith('.png'):
            path = os.path.join(d, f)
            img = Image.open(path).convert('RGBA')
            w, h = img.size
            pixels = img.load()
            
            min_x, min_y, max_x, max_y = w, h, 0, 0
            for y in range(h):
                for x in range(w):
                    if pixels[x, y][3] > 100:
                        min_x = min(min_x, x)
                        min_y = min(min_y, y)
                        max_x = max(max_x, x)
                        max_y = max(max_y, y)
            
            # Crop using the found bounding box
            if min_x < max_x and min_y < max_y:
                bbox = (min_x, min_y, max_x, max_y)
                # open original image (without convert RGBA to preserve original mode if needed, though convert is fine for crop)
                original_img = Image.open(path)
                cropped = original_img.crop(bbox)
                cropped.save(path)
                total_cropped += 1
                if '9.png' in path and 'registrar' in path:
                    print(f"Cropped {path} to {bbox}, new size: {cropped.width}x{cropped.height}")

print(f"Total images cropped: {total_cropped}")
