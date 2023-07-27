from buscar import buscar
import csv

def encomenda(local, escolha):
    pedido = f'{local}\\Encomendas\\{escolha}.txt'
    with open(pedido, 'r') as pedido:
        pedido = csv.reader(pedido, delimiter=',')
        lista = []
        for item in pedido:
            lista.append(buscar(item[0], item[1], local))
    return lista