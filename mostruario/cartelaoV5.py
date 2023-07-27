from PIL import Image
from encomenda import encomenda
from pares5 import pares5
import sys, os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pxl = 11.810833333333333333333333333333
tam = 184,302 #largura x altura


# t = time.localtime()
# timestamp = time.strftime('%Y%m%d_%H%M%S', t)
letra = (os.path.splitdrive(os.getcwd())[0])
local = f'{letra}\\Users\\{os.getlogin()}\\Desktop'
if os.path.isdir(f'{local}\\temp'):
    pass
else:
    os.mkdir(f'{local}\\temp')

while pxl != "seila":
    
    escolha = input('digite o nome do pedido:\n')
    retorno = encomenda(local, escolha)
    pedido = []
    x = var = 0
    for num in retorno:
        x += 1
        pedido.append(num)
        if len(pedido) == 24 or x == len(retorno):
            var += 1
            im = Image.new(mode="RGBA", size=(int(tam[0]*pxl),int(tam[1]*pxl)), color = (0,0,0,0))
            colCont = linCont = 0
            col = int(15*pxl)
            lin = int(37*pxl)
            for item in pedido:
                if colCont == 6:
                    colCont = 0
                    col = int(15*pxl)
                    linCont += 1
                    lin += int(76*pxl)
                if linCont == 5:
                    break
                img1 = pares5(item, local)
                im.paste(img1, (col-(img1.size[0]//2), (lin-(img1.size[1]//2))), mask=img1)
                colCont += 1
                col += int(31*pxl)
            im.save(f'{local}\\temp\\{escolha}_{var}.png', dpi=(300, 300))
            pedido = []
    print('Acabou!\n\n')