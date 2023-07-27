from PIL import Image, ImageDraw, ImageFont
from resize import resize
import os, sys

tam = 556,900
centro = 278,450

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def CartelaoV5Marca(im1, nome, defTam, local):
    
    im = Image.new(mode="RGB", size=(tam), color = '#ffffff')
    im.paste(im1, (centro[0]-(im1.size[0]//2), centro[1]-(im1.size[1]//2)), mask=im1)
    marca = Image.open(resource_path('marca.png'))
    marca = resize(marca, 600)
    mCentro = centro[0]-(marca.size[0]//2), centro[1]-(marca.size[1]//2)
    im.paste(marca, (mCentro), mask=marca)

    codigo = Image.new('RGBA', (500,500), (0,0,0,0))
    d = ImageDraw.Draw(codigo)
    font = ImageFont.truetype(r'C:\Windows\Fonts\CONTRAI.ttf', 50)
    d.text((0,0),nome,fill='black',font=font, stroke_width=5, stroke_fill='white')
    codigo = codigo.rotate(90)
    codigo = codigo.crop(codigo.getbbox())
    im.paste(codigo, ((65-(codigo.size[0]//2)),(448-(codigo.size[1]//2))), codigo)
    # This method will show image in any image viewer
    #im.show()
    im.save(f'{local}\\temp\\{nome}_{defTam}.png')