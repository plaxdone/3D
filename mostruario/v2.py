import csv
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def resize(original, base):
    largura, altura = original.size
    vsize = int(largura * base/altura)
    hsize = int(altura * base/largura)
    if altura > largura:
        original = original.resize((vsize, base), Image.Resampling.LANCZOS)
    else:
        original = original.resize((base, hsize), Image.Resampling.LANCZOS)
    return original

def abrirImg(item):
    img = Image.open(f'{path}\\{item}')
    if img.size[1]>img.size[0]:
        prop = img.size[0]/img.size[1]
    else:
        prop = img.size[1]/img.size[0]
    if prop > 0.9:
        img = resize(img, (int((tamImg-2)*pxl)))
    else:
        img = resize(img, (int((tamImg-2)*pxl)))
    return img

pxl = 11.810833333333333333333333333333
tam = 556,900
centro = 278,450


path = input('Cole o caminho da pasta:\n')
if os.path.isdir(f'{path}/temp'):
    pass
else:
    os.mkdir(f'{path}/temp')

tamImg = int(input('Qual o tamanho do mostruario?\n'))

with open(f'{path}\\listaOK.csv', 'r') as arquivo_referencia:
    tabela = csv.reader(arquivo_referencia, delimiter=',')
    for item in tabela:
        im = Image.new(mode="RGB", size=(tam), color = '#ffffff')

        img1 = abrirImg(item[0])
        img2 = abrirImg(item[1])

        c1 = 201
        c2 = 378
        l1 = 100
        l2 = 277
        l3 = 454
        l4 = 631
        l5 = 808

        im.paste(img1, ((c1-(img1.size[0]//2)), l1-(img1.size[1]//2)), mask=img1)
        im.paste(img2, ((c1-(img2.size[0]//2)), l2-(img2.size[1]//2)), mask=img2)
        im.paste(img1, ((c1-(img1.size[0]//2)), l3-(img1.size[1]//2)), mask=img1)
        im.paste(img2, ((c1-(img2.size[0]//2)), l4-(img2.size[1]//2)), mask=img2)
        im.paste(img1, ((c1-(img1.size[0]//2)), l5-(img1.size[1]//2)), mask=img1)
        if item[2] == '0':
            img1 = ImageOps.mirror(img1)
        if item[3] == '0':
            img2 = ImageOps.mirror(img2)
        im.paste(img1, ((c2-(img1.size[0]//2)), l1-(img1.size[1]//2)), mask=img1)
        im.paste(img2, ((c2-(img2.size[0]//2)), l2-(img2.size[1]//2)), mask=img2)
        im.paste(img1, ((c2-(img1.size[0]//2)), l3-(img1.size[1]//2)), mask=img1)
        im.paste(img2, ((c2-(img2.size[0]//2)), l4-(img2.size[1]//2)), mask=img2)
        im.paste(img1, ((c2-(img1.size[0]//2)), l5-(img1.size[1]//2)), mask=img1)

        marca = Image.open(resource_path('marca.png'))
        marca = resize(marca, 600)
        mCentro = centro[0]-(marca.size[0]//2), centro[1]-(marca.size[1]//2)
        im.paste(marca, (mCentro), mask=marca)

        nome = item[0].replace(' ', '.').split('.')[0]
        codigo = Image.new('RGBA', (500,500), (0,0,0,0))
        d = ImageDraw.Draw(codigo)
        font = ImageFont.truetype(r'C:\Windows\Fonts\CONTRAI.ttf', 50)
        d.text((0,0),nome,fill='black',font=font, stroke_width=5, stroke_fill='white')
        codigo = codigo.rotate(90)
        codigo = codigo.crop(codigo.getbbox())
        im.paste(codigo, ((65-(codigo.size[0]//2)),(448-(codigo.size[1]//2))), codigo)
        # This method will show image in any image viewer
        #im.show()
        im.save(f'{path}/temp/{nome}.png')