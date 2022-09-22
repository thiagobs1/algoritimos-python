def SomaArrayRecursivo(arr, n, soma):
    if n == 0:
        soma += arr[0]
        return soma
    else:
        soma = arr[n] + SomaArrayRecursivo(arr, n-1, soma)
        return soma

arr = [3,4,6,1, 9, 8]
soma = 0
print(SomaArrayRecursivo(arr, len(arr)-1, soma))