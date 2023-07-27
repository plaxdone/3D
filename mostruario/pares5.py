from PIL import Image, ImageOps, ImageDraw, ImageFont
from abrirImg import abrirImg
from cartelaoV5Marca import CartelaoV5Marca

pxl = 11.810833333333333333333333333333
tam = 29,74 #largura x altura
c1 = int(7*pxl)
c2 = int(22*pxl)
l1 = int(7*pxl)
l2 = int(22*pxl)
l3 = int(37*pxl)
l4 = int(52*pxl)
l5 = int(67*pxl)


def pares5(item, local):
    im = Image.new(mode="RGBA", size=(int(tam[0]*pxl),int(tam[1]*pxl)), color = (0,0,0,0))
    opn1 = item[0]+'\\'+item[1][0]
    opn2 = item[0]+'\\'+item[1][1]

    img1 = abrirImg(opn1,int(item[2]))
    img2 = abrirImg(opn2,int(item[2]))
    
    im.paste(img1, (c1-(img1.size[0]//2), (l1-(img1.size[1]//2))), mask=img1)
    im.paste(img2, (c1-(img2.size[0]//2), (l2-(img2.size[1]//2))), mask=img2)
    im.paste(img1, (c1-(img1.size[0]//2), (l3-(img1.size[1]//2))), mask=img1)
    im.paste(img2, (c1-(img2.size[0]//2), (l4-(img2.size[1]//2))), mask=img2)
    im.paste(img1, (c1-(img1.size[0]//2), (l5-(img1.size[1]//2))), mask=img1)
    if item[1][2] == '0':
        img1 = ImageOps.mirror(img1)
    if item[1][3] == '0':
        img2 = ImageOps.mirror(img2)
    im.paste(img1, (c2-(img1.size[0]//2), (l1-(img1.size[1]//2))), mask=img1)
    im.paste(img2, (c2-(img2.size[0]//2), (l2-(img2.size[1]//2))), mask=img2)
    im.paste(img1, (c2-(img1.size[0]//2), (l3-(img1.size[1]//2))), mask=img1)
    im.paste(img2, (c2-(img2.size[0]//2), (l4-(img2.size[1]//2))), mask=img2)
    im.paste(img1, (c2-(img1.size[0]//2), (l5-(img1.size[1]//2))), mask=img1)

    nome = item[1][0].replace(' ', '.').split('.')[0]
    CartelaoV5Marca(im, nome, item[2], local)
    codigo = Image.new('RGBA', (500,500), (0,0,0,0))
    d = ImageDraw.Draw(codigo)
    font = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 30)
    d.text((0,0),nome,fill='black',font=font)
    codigo = codigo.crop(codigo.getbbox())
    im.paste(codigo, ((int(14.5*pxl)-(codigo.size[0]//2)),(int(29.5*pxl)-(codigo.size[1]//2))), codigo)

    return im

# from encomenda import encomenda
# pedido = encomenda()
# for item in pedido:
#     img = pares5(item)
# img.show()