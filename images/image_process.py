from PIL import Image
import os

root = r'.\2XL'
for parent, dirnames, filenames in os.walk(root):
    for f in filenames:
        if f.endswith('png'):
            img = Image.open(f)
            W, H = img.size
            img_L = img.resize((32, 32), Image.ANTIALIAS)
            if img_L.mode == 'CMYK':
                img_L = img_L.convert('RGB')
            img_L.save('%s\\OUTPUT\\%s' % (root, f))
