from PIL import Image, ImageDraw, ImageFont, ImageOps

def resize(original, base):
    largura, altura = original.size
    vsize = int(largura * base/altura)
    original = original.resize((vsize, base), Image.Resampling.LANCZOS)
    return original

pxl = 11.810833333333333333333333333333
tam = 556,900
centro = 278,450
im = Image.new(mode="RGB", size=(tam), color = '#ffffff')

img1 = Image.open('33001.png')
img1 = resize(img1, (int(12*pxl)))
img2 = img1
c1 = 201
c2 = 378
l1 = 100
l2 = 277
l3 = 454
l4 = 631
l5 = 808

im.paste(img1, ((c1-(img1.size[0]//2)), l1-(img1.size[1]//2)), mask=img1)
im.paste(img2, ((c1-(img1.size[0]//2)), l2-(img1.size[1]//2)), mask=img2)
im.paste(img1, ((c1-(img1.size[0]//2)), l3-(img1.size[1]//2)), mask=img1)
im.paste(img2, ((c1-(img1.size[0]//2)), l4-(img1.size[1]//2)), mask=img2)
im.paste(img1, ((c1-(img1.size[0]//2)), l5-(img1.size[1]//2)), mask=img1)
img1 = ImageOps.mirror(img1)
img2 = ImageOps.mirror(img2)
im.paste(img1, ((c2-(img1.size[0]//2)), l1-(img1.size[1]//2)), mask=img1)
im.paste(img2, ((c2-(img1.size[0]//2)), l2-(img1.size[1]//2)), mask=img2)
im.paste(img1, ((c2-(img1.size[0]//2)), l3-(img1.size[1]//2)), mask=img1)
im.paste(img2, ((c2-(img1.size[0]//2)), l4-(img1.size[1]//2)), mask=img2)
im.paste(img1, ((c2-(img1.size[0]//2)), l5-(img1.size[1]//2)), mask=img1)


marca = Image.open('marca.png')
marca = resize(marca, 600)
mCentro = centro[0]-(marca.size[0]//2), centro[1]-(marca.size[1]//2)
im.paste(marca, (mCentro), mask=marca)


codigo = Image.new('RGBA', (500,500), (0,0,0,0))
d = ImageDraw.Draw(codigo)
font = ImageFont.truetype(r'C:\Windows\Fonts\CONTRAI.ttf', 50)
d.text((0,0),'DC1236',fill='black',font=font, stroke_width=5, stroke_fill='white')
codigo = codigo.rotate(90)
codigo = codigo.crop(codigo.getbbox())
print(codigo.size)
im.paste(codigo, ((65-24),(448-90)), codigo)
# This method will show image in any image viewer
im.show()


# , anchor='mm'

