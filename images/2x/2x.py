from PIL import Image
import os

for parent, dirnames, filenames in os.walk('.'):
    for f in filenames:
        if f.endswith('png'):
            img = Image.open(f)
            if img.mode == 'CMYK':
                img_L = img.convert('RGB')
            W, H = img.size
            img_L = img.resize((W * 2, H * 2), Image.ANTIALIAS)
            img_L.save('OUTPUT/%s' % f)
