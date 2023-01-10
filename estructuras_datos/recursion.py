# 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21 - 34 - 55 - 89 - 144
# 1   2   3   4   5   6    7    8    9   10   11    12
# Fib(1) => 1
# FIb(2) => 1
# Fib(N) => Fib(N - 1) + Fib(N - 2)

def fib(pos):
    # casos base
    print(f'llamando al fibonacci de {pos}')
    if (pos <= 2):
        return 1
    
    return fib(pos - 1) + fib(pos - 2)

# 24356
def palabras_telef(num):
    # 63 => ['MD', 'ND', 'OD', 'ME', 'NE', 'OE', 'MF', 'NF', 'OF']
    num = str(num)
    
    if num == '':
        return ['']
    
    primer_digito = num[0]
    resto = num[1:]

    lista_restante = palabras_telef(resto)

    letras = {
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'Q', 'R'],
        '8': ['T', 'U', 'V'],
        '9': ['X', 'Y', 'Z'],
        '0': ['', '', ''],
        '1': ['', '', '']
    }[primer_digito]
    
    letra1 = letras[0]
    letra2 = letras[1]
    letra3 = letras[2]


    comb_1 = [letra1 + palabra for palabra in lista_restante]
    comb_2 = [letra2 + palabra for palabra in lista_restante]
    comb_3 = [letra3 + palabra for palabra in lista_restante]

    return comb_1 + comb_2 + comb_3


def hanoi(num_discos, origen='A', destino='C'):
    assert isinstance(num_discos, int)
    assert num_discos > 0

    medio = 'ABC'.replace(origen, '').replace(destino, '')

    if num_discos == 1:
        return [f'1 -> {destino}']
    
    elif num_discos == 2:
        return [f'1 -> {medio}', f'2 -> {destino}', f'1 -> {destino}']
    
    return hanoi(num_discos - 1, origen, medio) + [f'{num_discos} -> {destino}'] + hanoi(num_discos - 1, medio, destino)



def uvas(bolsitas): # [20, 22, 1, 1, 4]
    indices = set([i for i in range(len(bolsitas))])
    intentos = [intentar(bolsitas, i, indices) for i in range(len(bolsitas))]
    return max(intentos)

def combinaciones(elementos):
    if len(elementos) == 1:
        return [[elementos[0]], []]
    
    primero = elementos[0]
    elementos_cpy = list(elementos[1:])
    
    sin_primero = combinaciones(elementos_cpy)
    con_primero = []
    for elem in sin_primero:
        elem.append(primero)
        con_primero.append(elem)
    
    final = sin_primero + con_primero
    return set(final)

    


import pdb; pdb.set_trace()

