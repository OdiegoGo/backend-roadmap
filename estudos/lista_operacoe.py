def somar_lista(lista_1,lista_2):
    listas_somadas=[]

    if len(lista_1)==len(lista_2):
        for i in range(len(lista_1)):
            listas_somadas.append(lista_1[i]+lista_2[i])
    
    if len(lista_1)>len(lista_2):
        for i in range(len(lista_2)):
            listas_somadas.append(lista_1[i]+lista_2[i])
        for k in range(i+1,len(lista_1)):
            listas_somadas.append(lista_1[k])

    if len(lista_2)>len(lista_1):
        for i in range(len(lista_1)):
            listas_somadas.append(lista_1[i]+lista_2[i])
        for k in range(i+1,len(lista_2)):
            listas_somadas.append(lista_2[k])
    
    return listas_somadas



    
def maior_numero(lista):
    maior = lista[0]

    for i in lista:
        if i > maior:
            maior = i

    return maior

def menor_numero(lista):
    menor = lista[0]

    for i in lista:
        if i < menor:
            menor = i

    return menor


def numeros_pares(lista):
    pares=[]

    for i in lista:
        if i % 2 == 0:
            pares.append(i)

    return pares