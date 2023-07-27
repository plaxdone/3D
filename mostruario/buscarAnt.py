def buscar(encomenda, tamanho):
    import csv
    import pathlib
    diretorio = pathlib.Path('C:\\Users\\Jorge\\Desktop\\mostruario')
    arquivos = diretorio.glob('**\listaOK.csv')

    for arquivo in arquivos:
        with open(arquivo, 'r') as lista:
            lista = csv.reader(lista, delimiter=',')
            for item in lista:
                for it in item:
                    if encomenda in it:
                        return item, tamanho
                        break