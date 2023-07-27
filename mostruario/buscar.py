import os

def buscar(encomenda, tamanho, local):
    import csv
    import pathlib
    diretorio = pathlib.Path(f'{local}\\indice')
    arquivos = diretorio.glob('**\\*listaOK.csv')

    for arquivo in arquivos:
        #retorno = (str(arquivo).replace('listaOK.csv',""))
        with open(arquivo, 'r') as lista:
            lista = csv.reader(lista, delimiter=',')
            for idx, item in enumerate(lista):
                if idx == 0:
                    retorno = item[0]
                else:
                    for it in item:
                        if encomenda in it:
                            return retorno, item, tamanho
                            break