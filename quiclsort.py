import time
import random

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivo = arr[0]
        menores = [i for i in arr[1:] if i <= pivo] # para todo i no range do array menor que o pivo 
        maiores = [i for i in arr[1:] if i > pivo] 
        return quicksort(menores) + [pivo] + quicksort(maiores) # repete a função até que chegue nos casos básicos

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

array1 = []
array2 = []

for i in range(100000):
    array1.append(random.randrange(1,1000000))
    array2.append(random.randrange(1,1000000))


start1 = time.time()
array1Ordenado = selectionSort(array1)
end1 = time.time()
print("\ntempo de execução selectionSort",end1-start1)

start2 = time.time()
array2Ordenado = quicksort(array2)
end2 = time.time()
print("tempo de execução quickSort: ",end2-start2)

