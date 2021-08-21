# Compilador
Atividade feita por Matheus Almeida, Fransueldes, Carlos Bruno e Rivaldo Nascimento para a matéria de Compiladores, dos de Tecnologia da Informação do CEULP/ULBRA, período 2021/2.

# Dicionário
<em>função</em> - Ex: <em>procurar</em>  
Método - Ex: Find

# A atividade
Considere uma linguagem com as seguintes características:  
<strong>palavras reservadas:</strong> while, do  
<strong>operadores: </strong> <, =, +  
<strong>terminador:</strong> ;  
<strong>identificadores:</strong> i, j  
<strong>constantes:</strong> sequência de números (um ou mais números)  
<strong>números:</strong> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9  
Implemente um analisador léxico (parser) que recebe uma string de entrada representando um código-fonte nessa linguagem e gera a tabela de tokens e a tabela de símbolos. O analisador léxico deve gerar a tabela de tokens e a tabela de símbolos em arquivo (um ou dois arquivos, a depender do formato escolhido, por exemplo, dois arquivos CSV ou um arquivo JSON). Ao realizar a análise léxica da string de entrada o analisador léxico também deve verificar a existência de erros, ou seja, se encontrar um token (ou símbolo) que não pertence à linguagem, deve gerar e apresentar uma mensagem de erro e encerrar o processamento. A mensagem de erro deve indicar o token desconhecido e a posição em que ele se encontra na string de entrada (linha, coluna). O analisador léxico pode ser implementado em qualquer linguagem de programação. 

# O código
O código foi desenvolvido em Python, pois era a linguagem mais familiar entre os membros do grupo.  
Foram criados Arrays com as entidades léxicas para que facilitasse a construção do algoritmo. A função <em>traduz</em> cria um Array gerado à partir de um split na string fornecida à mesma; cria/abre um arquivo de nome tabelas.csv, e inicia a veriicação. A estrutura da tabela é:  
TOKEN | IDENTIFICACAO | TAMANHO | POSICAO .  
O Token da tabela é o próprio item do loop.  
A Identificacao é feita por uma função chamada <em>procura</em>, que retorna a identificação do item.  
O Tamanho é a quantidade de letras na string.
A Posicao é a posição do item na string original, obtida por um Find à partir da posição do item anterior.  
Logo após, os dados obtidos são escritos no arquivo tabelas.csv e o loop se repete com todos os outros itens até terminar.
Ao fim, obtemos a Tabela de Símbolos e a Tabela de Identificação.
