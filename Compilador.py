import csv


linha = 'while i < 100 do i = i + j;'

reservadas = ['while', 'do']
operadores = ['<', '=', '+']
terminador = ';'
identificadores = ['i', 'j']


def procura(item):
    if item in reservadas:
        return 'Palavra reservada'
    elif item in operadores:
        return 'Operador'
    elif item in terminador:
        return 'Terminador'
    elif item in identificadores:
        return 'Identificador'
    else:
        return 'Constante'

def pesquisa(token, lista):
    for item in lista:
        if token in item:
            return True
    return False

def traduz(linha):
    itens = linha.replace(';', '').split(' ')
    arq = open('tabelas.csv', 'w', newline='', encoding='utf-8')
    w = csv.writer(arq)
    w.writerow(['TOKEN', 'IDENTIFICACAO', 'TAMANHO', 'POSICAO'])

    listaIdent = []
    listaAtual = []
    for i in range(len(itens)):
        token = itens[i]
        identificacao = procura(itens[i])
        if identificacao == 'Constante' or identificacao == 'Identificador':
            if not pesquisa(token, listaIdent):
                listaIdent.append([token, identificacao])
                identificacao = [identificacao, len(listaIdent)]
            else:
                for i, item in enumerate(listaIdent):
                    if item[1] == identificacao and item[0] == token:
                        identificacao = [item[1], i+1]
        tamanho = len(itens[i])
        posicao = 0
        if listaAtual:
            if len(listaAtual) == 1:
                posicao = linha.find(token, len(listaAtual[0])+1)
            else:
                posicao = linha.find(token, listaAtual[-1][1]+1)
        listaAtual.append([token, posicao])
        if token == '=':
            w.writerow(["'"+token, identificacao, tamanho, '(0,{})'.format(posicao)])
        else:
            w.writerow([token, identificacao, tamanho, '(0,{})'.format(posicao)])
    w.writerow([linha[-1], 'Terminador', 1, '(0,{})'.format(len(linha)-1)])
    w.writerow([])
    w.writerow(['INDICE', 'SiMBOLO'])
    for item in listaIdent:
        w.writerow([listaIdent.index(item)+1, item[0]])

    arq.close() 

traduz(linha)
