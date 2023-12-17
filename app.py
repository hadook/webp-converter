import os
from webptools import cwebp

dir_in = "D:\\tmp\\in\\"
dir_out = "D:\\tmp\\out\\"

for filename in os.listdir(dir_in):
    f = os.path.join(dir_in, filename)
    if os.path.isfile(f):
        if f.endswith('.png') or f.endswith('.jpg'):
            split_tup = os.path.splitext(filename)

            base = split_tup[0]
            ext = split_tup[1]

            img_in = dir_in + base + ext
            img_out = dir_out + base + '.webp'

            cwebp(input_image=img_in, output_image=img_out, option='-q 90')
            print(img_out)
