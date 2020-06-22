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
    print()
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
        print()
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

def compara_assinatura(ass, calculo_ass):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    lista=[]
    similar=0
    for i in range (0,len(calculo_ass)):
        valor1=calculo_ass[i]
        valor2=ass[i]
        similar = similar + abs(float(valor1-valor2))
        #compara_assinatura

    return similar/6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_assinatura = []
    text=[]
    text.append(texto)
    n=len(text)
    for i in range(0,len(text)):
        conteudo = text[i]
        lista_coluna=[]
        lista_coluna.append(tamanho_palavra(conteudo))
        lista_coluna.append(Type_Token(conteudo))
        lista_coluna.append(hapax_legomana(conteudo))
        lista_coluna.append(tamanho_medio_sentença(conteudo))
        lista_coluna.append(complexibilidade(conteudo))
        lista_coluna.append(tamanho_médio_frase(conteudo))
        lista_assinatura.append(lista_coluna)

    return lista_assinatura

def avalia_textos(texto, grau_similaridade):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    valor_similaridade=grau_similaridade
    lista_menor=[]
    for i in range(0,len(valor_similaridade)):
        similaridade_geral=valor_similaridade[i]
        lista_menor.append([similaridade_geral,i+1])
        lista_menor.sort()
    valor=lista_menor[0]
    resposta=valor[1]
    return resposta

def tamanho_palavra(texto):
    '''ok'''
    total_palavras = len(separa_palavras(texto))
    texto = texto.replace(" ", "")
    tampalavra=len(texto)
    media_tamanho=tampalavra/total_palavras
    return media_tamanho

def Type_Token(texto):
    ''' ok '''
    palavras_diferentes=palavras_não_repetem(texto)
    total_palavras=numero_palavras(texto)
    return len(palavras_diferentes)/len(total_palavras)

def hapax_legomana(texto):
    ''' ok '''
    base=numero_palavras(texto)
    palavras_unicas = n_palavras_unicas(base)
    total_palavras = numero_palavras(texto)
    return palavras_unicas / len(total_palavras)

def tamanho_medio_sentença(texto):
    '''ok'''
    sentença_separada = separa_sentencas(texto)
    texto = texto.replace(".", "")
    return len(texto)/len(sentença_separada)

def complexibilidade(texto):
    ''' ok '''
    lista_sentença=separa_sentencas(texto)
    num_sentença=len(lista_sentença)
    novo=0
    for i in range(0,len(separa_sentencas(texto))):
        frase_list=lista_sentença[i]
        lista_frase_separada=separa_frases(frase_list)
        num_frase=len(lista_frase_separada)
        novo=num_frase+novo
    relação_complexa=novo/num_sentença
    return relação_complexa

def tamanho_médio_frase(texto):
    '''ok'''
    return num_caracter(texto)/num_frase(texto)

def num_caracter(texto):
    '''ok'''
    texto = texto.lower()
    texto = texto.replace(",", "")
    texto = texto.replace(".", "")
    contar_caracter = len(texto)
    return contar_caracter

def num_frase(texto):
    '''ok'''
    texto = texto.lower()
    lista_sentença_separada = separa_sentencas(texto)
    total_frase = 0
    for i in range(0, len(lista_sentença_separada)):
        sentença = lista_sentença_separada[i]
        frase = separa_frases(sentença)
        novo1 = len(frase)
        total_frase = novo1 + total_frase
    return total_frase

def numero_frase(texto):#retorna frase separadas
    frase=[]
    sentença_list=separa_sentencas(texto)
    x=0
    while x < len(sentença_list):
        frase.extend(separa_frases(sentença_list[x]))
        x=x+1
    return frase

def numero_palavras(texto):#retorna palavras separadas
    palavras=[]
    frases = numero_frase(texto)
    x = 0
    while x < len(frases):
        palavras.extend(separa_palavras(frases[x]))
        x = x + 1
    return palavras

def palavras_não_repetem(texto):
    texto=texto.lower()
    valor1=numero_palavras(texto)
    return set(valor1)

def main():
    ass=le_assinatura()
    print()
    texto=le_textos()
    for i in range(0,len(calcular_ass)):
        calculo_ass=calcular_ass[i]
        similaridade=compara_assinatura(ass, calculo_ass)
        grau_similaridade.append(similaridade)
    resposta_exercicio=avalia_textos(texto,grau_similaridade)
    print("O autor do texto {} está infectado com COH-PIAH".format(resposta_exercicio))

if __name__ == "__main__":
    main()