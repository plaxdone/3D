import os

lista = [
    'natsort',
    'numpy',
    'pandas',
    'matplotlib',
    'scikit-image',
    'pillow',
    'requests',
    'mysql-connector-python',
    'flask',
    'scikit-learn',
    'pyinstaller'
    ]

def verifica():
    path = f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\Programs\\Python'
    versao = os.listdir(path)
    lista = []
    for it in versao:
        lista.append('py'+' -'+it[-3]+'.'+it[-2:])
    return lista

def opcoes(versao):
    print('Verifique e escolha a versão do seu sistema(confira no canto inferior direito):\n')
    for idx, opc in enumerate(versao):
        print(f'{idx+1} - {opc[-4:]}')
    opcao = input()# 1 ou 2
    try:
        val = int(opcao)
    except ValueError:
        print("erroooooou")
    if val < 1 or val > idx+1:
        print("erroooooou")
    check_pip(val)
    return val

def check_pip(val):
    retorno = os.system(versao[val-1] + ' -m pip --version')
    if retorno == 1:
        os.system(versao[val-1] + ' -m ensurepip --upgrade')
        os.system(versao[val-1] + ' -m pip install pip --upgrade')
    pass

def ins_des():
    opcao = input('Escolha o que deseja fazer:\n1 - Instalar/Atualizar\n2 - Desistalar\n')
    try:
        val = int(opcao)
    except ValueError:
        print("erroooooou")
    if val not in (1, 2):
        print("errrrou")
    if val == 1:
        return ' -m pip install --upgrade '
    if val == 2:
        return ' -m pip uninstall -y '

def exec(comand, val):
    for it in lista:
        comando = versao[val-1] + comand + it
        ret = os.system(comando)



versao = verifica() #['py -3.10', 'py -3.11']
escolha = opcoes(versao)#retorna 1 ou 2
padrao = ins_des()#retorna 1 ou 2
comando = exec(padrao, escolha)
