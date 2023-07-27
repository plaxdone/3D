from PIL import Image, ImageDraw, ImageFont
import os
import re

t = 3000
t2 = ''
def resize(original, base):
    largura, altura = original.size
    vsize = int(largura * base/altura)
    original = original.resize((vsize, base), Image.Resampling.LANCZOS)
    return original

def obter():
    from natsort import natsorted

    lista = natsorted(os.listdir(path))

    return(lista)

def imagem():
    img = Image.new("RGB", (t2), color='#b3b3b3')
    return img
    
def marca():
    marca = Image.open('marca dagua cartelao.png')
    marca = resize(marca, t2[1])
    marca.putalpha(40)
    img.paste(marca, (0, 0), mask=marca)

path = input('Cole o caminho da pasta:')
if os.path.isdir(f'{path}/temp'):
    pass
else:
    os.mkdir(f'{path}/temp')
arquivos = obter()

for item in arquivos:
    res = os.path.splitext(item)
    if res[1] == '.png':
        temp = Image.open(item)
        temp = resize(temp, t)
        t2 = temp.size[0]+100, temp.size[1]+100
        img = imagem()
        pos1 = int((t2[0]-temp.size[0])/2)
        pos2 = int((t2[1]-temp.size[1])/2)
        img.paste(temp, (pos1, pos2), mask=temp)
        marca()
        leg = res[0].split('_')[0][0:]
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype(r'C:\Windows\Fonts\CONTRAI.ttf', 150)
        d.text((t2[0]/2, t2[1]/2),leg.upper(),fill='black' ,anchor="mm",font=font, stroke_width=5, stroke_fill='white')
        img.save(f'{path}/temp/{item}')

