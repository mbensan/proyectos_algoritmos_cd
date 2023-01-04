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



import pdb; pdb.set_trace()

