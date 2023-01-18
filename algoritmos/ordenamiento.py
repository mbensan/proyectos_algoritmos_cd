import json

miarr = [5, 1, -2, 8, 4, 6]

pokefile = open('pokemon.json', 'r')
pokedict = json.load(pokefile)
pokelist = [elem['name'] for elem in pokedict['results']]

# insertsort
def fuerza_bruta(arr):
    comparaciones = 0

    if len(arr) <= 1:
        return
    
    ordenados = 0
    while ordenados < len(arr) - 1:
        # pescar el menor de todos, y cambiarlo por el primero de los que aún no están ordenados
        i_menor = ordenados
        for i in range(ordenados + 1, len(arr)):
            comparaciones += 1
            if arr[i] < arr[i_menor]:
                i_menor = i
        
        # ahora que encontré el índice del elemento más pequeño de los que aún están desordenados, lo cambio por el elemento inicial (de los desordenados)
        aux = arr[ordenados]
        arr[ordenados] = arr[i_menor]
        arr[i_menor] = aux

        ordenados += 1
    print(f'Se han realizado {comparaciones} comparaciones')

fuerza_bruta(miarr)

global comparaciones_qs
comparaciones_qs = 0

def quicksort(arr):
    global comparaciones_qs
    if len(arr) <= 1:
        return arr
    
    # 1. elegir un pivote
    pivote = arr[0]
    izq = []
    der = []
    # 2. Dejar todos los elementos menores, a la izquierda
    # 3. Dejar todos los elementos mayores, a la derecha
    for i in range(1, len(arr)):
        comparaciones_qs += 1
        if arr[i] > pivote:
            der.append(arr[i])
        else:
            izq.append(arr[i])

    # 4. Ordenar recursivamente ambas partes
    return quicksort(izq) + [pivote] + quicksort(der)



import pdb; pdb.set_trace()
    


            
        
