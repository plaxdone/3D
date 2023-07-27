from PIL import Image, ImageOps
import csv
import pathlib
from buscar import buscar

def resize(original, base):
    largura, altura = original.size
    vsize = int(largura * base/altura)
    hsize = int(altura * base/largura)
    if altura > largura:
        original = original.resize((vsize, base), Image.Resampling.LANCZOS)
    else:
        original = original.resize((base, hsize), Image.Resampling.LANCZOS)
    return original

def abrirImg(item, tamImg):
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

pxl = 11.810833333333333333333333333333

diretorio = pathlib.Path('C:\\Users\\Jorge\\Desktop\\mostruario')
escolha = input('digite o nome do pedido\n')
pedido = f'{diretorio}\\{escolha}.txt'
with open(pedido, 'r') as pedido:
    pedido = csv.reader(pedido, delimiter=',')
    lista = []
    for item in pedido:
        lista.append(buscar(item[0], item[1]))
    # for item in lista:
    #     print(item)
    
        
    for item in lista:
        #im = Image.new(mode="RGBA", size=(590,709), color = (0,0,0,0))
        im = Image.open('marcaNova3.png')
        opn1 = item[0]+item[1][0]
        opn2 = item[0]+item[1][1]

        img1 = abrirImg(opn1,int(item[2]))
        img2 = abrirImg(opn2,int(item[2]))

        c1 = 377
        c2 = 590
        l1 = 118
        l2 = 295
        l3 = 472

        im.paste(img1, (l1-(img1.size[0]//2), (c1-(img1.size[1]//2))), mask=img1)
        im.paste(img2, (l2-(img2.size[0]//2), (c1-(img2.size[1]//2))), mask=img2)
        im.paste(img1, (l3-(img1.size[0]//2), (c1-(img1.size[1]//2))), mask=img1)
        if item[0][2] == '0':
            img1 = ImageOps.mirror(img1)
        if item[0][3] == '0':
            img2 = ImageOps.mirror(img2)
        im.paste(img1, (l1-(img1.size[0]//2), (c2-(img1.size[1]//2))), mask=img1)
        im.paste(img2, (l2-(img2.size[0]//2), (c2-(img2.size[1]//2))), mask=img2)
        im.paste(img1, (l3-(img1.size[0]//2), (c2-(img1.size[1]//2))), mask=img1)
        im.save(f'C:/Users/Jorge/Desktop/mostruario/saida/{(item[1][0]).split()[0]}.png')