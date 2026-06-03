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
            img = Image.open(path)
            bbox = img.getbbox()
            if bbox:
                # If bbox is smaller than the image size, crop it
                if bbox != (0, 0, img.width, img.height):
                    cropped = img.crop(bbox)
                    cropped.save(path)
                    total_cropped += 1
                    print(f"Cropped {path} to {bbox}")

print(f"Total images cropped: {total_cropped}")
