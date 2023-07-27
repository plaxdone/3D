from PIL import Image
import csv
path = input('Cole o caminho da pasta:\n')

with open(f'{path}\\listaOK.csv', 'r') as arquivo_referencia:
    tabela = csv.reader(arquivo_referencia, delimiter=',')
    for idx, item in enumerate(tabela):
        img1 = Image.open(f'{path}\\{item[0]}')
        if img1.size[1]>img1.size[0]:
            prop = img1.size[0]/img1.size[1]
        else:
            prop = img1.size[1]/img1.size[0]
        print(f"{idx+1} - {prop}")
