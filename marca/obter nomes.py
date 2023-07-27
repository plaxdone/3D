import os
from natsort import natsorted

lista2 = []
lista = natsorted(os.listdir())
print(lista)
for item in lista:
    res = os.path.splitext(item)
    if res[1] == '.png':
        lista2.append(item)



print(lista2)