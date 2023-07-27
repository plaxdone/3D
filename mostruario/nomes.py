import os
from natsort import natsorted

path = input('Cole o caminho da pasta:')
letra = (os.path.splitdrive(os.getcwd())[0])
local = f'{letra}\\Users\\{os.getlogin()}\\Desktop'
arquivo = f'{local}\\indice\\{os.path.basename(path)} - listaOK.csv'
lista2 = []
if os.path.isdir(f'{local}\\indice'):
    pass
else:
    os.mkdir(f'{local}\\indice')

if os.path.exists(arquivo):
    with open(arquivo, 'r') as lista:
        for item in lista:
            item2 = item.replace('\n',"")
            lista2.append(item2)
else:
    lista2 = [path]
# # for item in lista2:
# #     print(item.split()[0])

def incluir(dado):
    for item in lista2:
        if item.startswith(dado.replace('.', ' ').replace('(', ' ').split(' ')[0]):
            return False
    lista2.append(dado)
        


lista = natsorted(os.listdir(path))
dado = 'nada'
for item in lista:
    if item.replace('.', ' ').replace('(', ' ').split(' ')[0] in dado.replace('.', ' ').replace('(', ' ').split(' ')[0]:
        dado = (f'{dado},{item},0,0')
        incluir(dado)
        dado = 'nada'
        continue
    if dado == 'nada':
        dado = item
        continue
    if item.replace('.', ' ').replace('(', ' ').split(' ')[0] not in dado.replace('.', ' ').replace('(', ' ').split(' ')[0]:
        dado = (f'{dado},{dado},0,0')
        incluir(dado)
        dado = item


with open(arquivo, 'w') as f:
    for line in lista2:
        f.write(line)
        f.write('\n')