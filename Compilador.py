import csv


linha = 'while ; x i < 10i0 do i = i + j;'

reservadas = ['while', 'do']
operadores = ['<', '=', '+']
terminador = ';'
identificadores = ['i', 'j']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def valida(item):
    for letra in item:
        if not letra in numeros:
            return False
    return True
def procura(item):
    if item in reservadas:
        return 'Palavra reservada'
    elif item in operadores:
        return 'Operador'
    elif item in terminador:
        return 'Terminador'
    elif item in identificadores:
        return 'Identificador'
    elif item in numeros or valida(item):
        return 'Constante'
    else:
        return 'ERRO'

def pesquisa(token, lista):
    for item in lista:
        if token in item:
            return True
    return False

def formata(linha):
    itens = linha.split(' ')
    for i, item in enumerate(itens):
        if procura(item) == 'ERRO':
            itens[i] = item.replace('j', ' j ').replace('i', ' i ').replace(';', ' ; ').replace('+', ' + ').replace('=', ' = ').replace('do', ' do ').replace('while', ' while ').replace('<', ' < ')
    lista = ' '.join(itens).split(' ')
    lista = [x for x in lista if x]
    return lista

def verifica(item):
    if item in reservadas or item in operadores or item in terminador or item in identificadores or valida(item):
        return True
    return False

def traduz(linha):
    itens = formata(linha)
    arq = open('tabelas.csv', 'w', newline='', encoding='utf-8')
    w = csv.writer(arq)
    w.writerow(['TOKEN', 'IDENTIFICACAO', 'TAMANHO', 'POSICAO'])

    listaIdent = []
    listaAtual = []
    
    for i in range(len(itens)):
        token = itens[i]
        if not verifica(itens[i]):
            print('ERRO! Elemento "{}" não conhecidos pelo analisador léxico!'.format(token))
            break
        identificacao = procura(itens[i])
        if identificacao == 'Identificador' or identificacao == 'Constante':
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
    arq.close()
    arq = open('simbolos.csv', 'w', newline='', encoding='utf-8')
    w = csv.writer(arq)
    w.writerow(['INDICE', 'SiMBOLO'])
    for item in listaIdent:
        w.writerow([listaIdent.index(item)+1, item[0]])

    arq.close() 

traduz(linha)
