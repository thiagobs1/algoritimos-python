def buscaMenor(arr):
    menor = arr[0]
    indiceMenor = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            indiceMenor = i
    return indiceMenor

def selectionSort(arr):
    novoArr = []
    for i in range (len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor)) # adiciona o menor ao novoo array ao mesmo tempo em que exclui o menor do array anterior
    return novoArr

print(selectionSort([5,3,6,2, 10, 1, 9, 20])) # tempo de execução = O(n^2) pois precisamos percorrer n elementos n vezes, desconsiderando a contante 1/2