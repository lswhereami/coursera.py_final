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


def n_palavras(lista_palavras):
    x = len(lista_palavras)
    return x

def carac_palavra(texto):
    palavras = separa_palavras(pontuacao(texto))
    num_palavras = len(palavras)
    num_carac = 0
    for x in palavras:
        num_carac = num_carac + len(x)
    return num_carac/num_palavras

def type_token(texto):
    texto = pontuacao(texto)
    lista_palavras = separa_palavras(texto)
    return n_palavras_diferentes(lista_palavras)/n_palavras(lista_palavras)

def hapax (texto):
    texto = pontuacao(texto)
    lista_palavras = separa_palavras(texto)
    return n_palavras_unicas(lista_palavras)/n_palavras(lista_palavras)
    
def carac_sent(texto):
    sentencas= separa_sentencas(texto)
    num_sentencas = len(sentencas)
    num_carac = 0
    for x in sentencas:
        num_carac = num_carac + len(x)
    return num_carac/num_sentencas

def frase_sent(texto):
    sentencas = separa_sentencas(texto)
    soma = 0 
    for x in sentencas:
        frases = separa_frases(x)
        soma += len(frases)
    return soma/len(sentencas)

def carac_frase(texto):
    sentencas = separa_sentencas(texto)
    num_carac = 0
    num_frases = 0 
    for x in sentencas:
        frases = separa_frases(x)
        num_frases += len(frases)
        for y in frases:
            num_carac += len(y)
    return num_carac/num_frases

def pontuacao (texto):
    texto = re.sub('[!.,:@]', '', texto)
    return texto

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    a = carac_palavra(texto)
    b = type_token(texto)
    c = hapax (texto)
    d = carac_sent(texto)
    e = frase_sent(texto)
    f = carac_frase(texto)
    return [a, b, c, d, e, f]

def compara_assinatura(as_a, as_b):
    
    valorLinguistico = 0
    
    for i in range(0,6):
        valor = as_a[i] - as_b[i]
        
        if (valor < 0): 
            valor = valor * (-1)
            
        valorLinguistico = valorLinguistico + valor
    
    return valorLinguistico / 6

def avalia_textos(textos, ass_cp):
    
    assinaturas = []

    for tex in textos:
        assinaturas.append(calcula_assinatura(tex))

    grauSimilaridade = 1000.0
    numTex = -1
    
    for i in range( 0, len(assinaturas)):
        
        similaridade = compara_assinatura(ass_cp, assinaturas[i])
        
        if (similaridade < grauSimilaridade):
            grauSimilaridade = similaridade
            numTex = i + 1

    return numTex
    
def main():
    
    assinaturaPadrao = le_assinatura()
    
    textos = le_textos()

    numSimilar = avalia_textos(textos, assinaturaPadrao)
    
    print("O autor do texto {} esta infectado com COH-PIAH".format(numSimilar))
    
main()