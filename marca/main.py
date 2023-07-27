from PIL import Image, ImageDraw, ImageFont
from time import sleep
import os
import sys

t = 3000
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def resize(original, base):
    largura, altura = original.size
    vsize = int(largura * base/altura)
    original = original.resize((vsize, base), Image.Resampling.LANCZOS)
    return original

def obter(caminho):
    from natsort import natsorted

    lista = natsorted(os.listdir(caminho))

    return(lista)

def imagem(tam):
    img = Image.new("RGB", (tam), color='#b3b3b3')
    return img
    
def marca(img, tam):
    marca = Image.open(resource_path('marca2.png'))
    # marca = Image.open(resource_path('marca.png'))
    marca = resize(marca, tam[1])
    marca.putalpha(40)
    img.paste(marca, (-600, 0), mask=marca)
    # img.paste(marca, (0, 0), mask=marca)
    return img

def main():
    path = input('Cole o caminho da pasta:')

    if os.path.isdir(f'{path}/temp'):
        pass
    else:
        os.mkdir(f'{path}/temp')

    arquivos = obter(path)

    for item in arquivos:
        res = os.path.splitext(item)
        if res[1] == '.png':
            temp = Image.open(f'{path}/{item}')
            temp = resize(temp, t)
            t2 = temp.size[0]+100, temp.size[1]+100
            img = imagem(t2)
            pos1 = int((t2[0]-temp.size[0])/2)
            pos2 = int((t2[1]-temp.size[1])/2)
            img.paste(temp, (pos1, pos2), mask=temp)
            marca(img, t2)
            leg = res[0].split('_')[0][0:]
            leg = leg.upper()
            leg = 'Cartelão ' + leg
            d = ImageDraw.Draw(img)
            font = ImageFont.truetype(r'C:\Windows\Fonts\CONTRAI.ttf', 150)
            d.text((t2[0]/2, t2[1]/2),leg,fill='black' ,anchor="mm",font=font, stroke_width=5, stroke_fill='white')
            img = resize(img, 800)
            img.save(f'{path}/temp/{item}')
            print(f'Arquivo {leg} finalizado\naguarde')
    print(f'Todos os arquivos finalizados\ntchau')
    sleep(120)


if __name__ == "__main__":
	
    main()


# pyinstaller --onefile --add-data "marca2.png;." cartelaoV5.py