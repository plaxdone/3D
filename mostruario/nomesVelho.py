import os
from natsort import natsorted

path = input('Cole o caminho da pasta:')
letra = (os.path.splitdrive(os.getcwd())[0])
local = f'{letra}\\Users\\{os.getlogin()}\\Desktop'
if os.path.isdir(f'{local}\\indice'):
    pass
else:
    os.mkdir(f'{local}\\indice')
lista2 = [path]
lista = natsorted(os.listdir(path))
dado = 'nada'
for item in lista:
    if item.split()[0] in dado.split()[0]:
        dado = (f'{dado},{item},0,0')
        lista2.append(dado)
        dado = 'nada'
        continue
    if dado == 'nada':
        dado = item
        continue
    if item.split()[0] not in dado.split()[0]:
        dado = (f'{dado},{dado},0,0')
        lista2.append(dado)
        dado = item

print(lista2)
# with open(f'{local}\\indice\\{os.path.basename(path)} - listaOK.csv', 'w') as f:
#     for line in lista2:
#         f.write(line)
#         f.write('\n')