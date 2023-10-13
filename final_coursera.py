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

    palavras_list = separa_palavras(texto)
    palavras_total = len(palavras_list)
    palavras_tamanho = 0
    for i in range (palavras_total):
        palavras_tamanho = palavras_tamanho + len(palavras_list[i])
    
    palavras_media = palavras_tamanho/palavras_total
    type_token = n_palavras_diferentes(texto)/palavras_total
    hapax_legomana = n_palavras_unicas(texto)/palavras_total
    sentencas_total = len(separa_sentencas(texto))
    frases_total = len(separa_frases(texto))
    sentencas_media = palavras_tamanho/sentencas_total
    sentenca_complex = frases_total/sentencas_total
    frases_media = palavras_tamanho/frases_total

    assinatura = [palavras_media, type_token, hapax_legomana, sentencas_media, sentenca_complex, frases_media]
    return assinatura

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
                  
    return infeccao
