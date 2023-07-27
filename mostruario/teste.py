import csv

path = input('Cole o caminho da pasta:')
lista = []

with open(f'{path}\\listaOK.csv', 'r') as arquivo_referencia:
    tabela = csv.reader(arquivo_referencia, delimiter=',')
    for item in tabela:
        print(item)


# #     print(tabela)   

# # temp = open('listaOK.txt','r').read().split('\n')
# # # for item in temp:
# # #     print(item)

# import csv

# # 1. abrir o arquivo
# with open('lista.csv', encoding='utf-8') as lista:

#   # 2. ler a tabela
#   tabela = csv.reader(lista, delimiter=',')

#   # 3. navegar pela tabela
#   for l in tabela:
#     id_autor = l[0]
    
#     nome = l[1]
#     nome2 = l[2]
#     nome3 = l[3]


#     print(id_autor, nome, nome2, nome3) # 191149, Diego C B Mariano