from PIL import Image
from resize import resize

def abrirImg(item, tamImg):
    pxl = 11.810833333333333333333333333333
    img = Image.open(item)
    if img.size[1]>img.size[0]:
        prop = img.size[0]/img.size[1]
    else:
        prop = img.size[1]/img.size[0]
    if prop > 0.9:
        img = resize(img, (int((tamImg-2)*pxl)))
    else:
        img = resize(img, (int((tamImg)*pxl)))
    return img