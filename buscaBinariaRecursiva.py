from asyncio.windows_events import NULL


def pesquisa_binaria(lista, item, baixo, alto):

    # while (baixo <= alto):
    #     meio = (baixo + alto)//2
    #     chute = lista[meio]

    #     if(chute == item):
    #         return meio
    #     if(chute > item):
    #         alto = meio - 1
    #     if(chute < item):
    #         baixo = meio + 1
    if(baixo > alto):
        return NULL
    else:
        meio = (alto + baixo)//2
        if(item == lista[meio]):
            return meio
        else:
            if(item > lista[meio]):
                return pesquisa_binaria(lista, item, baixo + 1, alto)
            if(item < lista[meio]):
                return pesquisa_binaria(lista, item, baixo, alto - 1)
    return None

lista = [2,4,5,10,12, 15, 20, 22]
baixo = 0
alto = len(lista) - 1
item = 22
indexOfSearch = pesquisa_binaria(lista, item, baixo, alto)

if(indexOfSearch != NULL):
    print("elemento {} esta na posicao {}".format(item, indexOfSearch) )
else:
    print('elemento nao encontrado na lista'.format(item))