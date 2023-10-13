#!/usr/bin/python3
import re

def le_assinatura():
  '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
  print("Bem-vindo ao detector automático de COH-PIAH.")

  wal = float(input("Entre o tamanho medio de palavra:"))
  ttr = float(input("Entre a relação Type-Token:"))
  hlr = float(input("Entre a Razão Hapax Legomana:"))
  sal = float(input("Entre o tamanho médio de sentença:"))
  sac = float(input("Entre a complexidade média da sentença:"))
  pal = float(input("Entre o tamanho medio de frase:"))

  return [wal, ttr, hlr, sal, sac, pal]
  
def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
        
    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    
    return len(freq)

def compara_assinatura(as_a, as_b):

    similaridade = 0
    for compara in range (0, 6):
        similaridade = similaridade + (abs(as_a[compara] - as_b[compara]))
    grau = similaridade / 6
    if grau < 0:
        grau = grau * (-1)
    return grau

def calcula_assinatura(texto):

    sentencas = separa_sentencas(texto)
    num_sentencas = 0
    soma_sentencas = 0

    frases = []
    for indice in range(len(sentencas)):
        frase_indice = separa_frases(sentencas[indice])
        frases.append(frase_indice)
        num_sentencas = num_sentencas + 1
        soma_sentencas = soma_sentencas + len(sentencas[indice])

    palavras = []
    num_frases = 0
    soma_frases = 0
    for linha in range(len(frases)):
        for coluna in range(len(frases[linha])):
            palavras_indice = separa_palavras(frases[linha][coluna])
            palavras.append(palavras_indice)
            num_frases = num_frases + 1
            soma_frases = soma_frases + len(frases[linha][coluna])

    matrix_lista = []

    for linha in range(len(palavras)):
        for coluna in range(len(palavras[linha])):
            matrix_lista.append(palavras[linha][coluna])
    palavras = matrix_lista[:]

    total_letras = 0
    total_palavras = len(palavras)

    for lin in range(len(palavras)):
        for col in range(len(palavras[lin])):
            total_letras = total_letras + len(str(palavras[lin][col]))
    
    media_palavra = total_letras / total_palavras
    type_Token = n_palavras_diferentes(palavras) / total_palavras
    hapax_Legomana = n_palavras_unicas(palavras) / total_palavras
    media_sentenca = soma_sentencas / num_sentencas
    complex_sentenca = num_frases / num_sentencas
    media_frase = soma_frases / num_frases
    
    return [round (media_palavra, 2), type_Token, hapax_Legomana, media_sentenca, complex_sentenca, media_frase]   

def avalia_textos(textos, ass_cp):

    indice = 1
    assinatura = calcula_assinatura(textos[indice])
    grau_similaridade = compara_assinatura(assinatura, ass_cp)
    
    grau_baixo = grau_similaridade
    infeccao = indice
    indice = indice+1
    while indice <(len (textos)):
        assinatura = calcula_assinatura(textos[indice])
        grau_similaridade = compara_assinatura(assinatura, ass_cp)
        if grau_similaridade < grau_baixo:
            grau_baixo = grau_similaridade
            infeccao = indice
        indice = indice+1
    print ("O autor do texto %d está infectado com COH-PIAH" %(infeccao))              
    return infeccao

def main():
    assinatura_cp = le_assinatura()
    textos_lidos = le_textos()
    avalia_textos(textos_lidos, assinatura_cp)

main()
