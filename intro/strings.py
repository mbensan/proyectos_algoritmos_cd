def num2roman(num):
    # M D C L X V I (3789) => MMMDCCLXXXIX
    # 1. Vemos cuantos miles tengo
    miles = num // 1000
    miles_rom = 'M' * miles

    resto = num - (miles * 1000)
    centenas = resto // 100

    centenas_rom = ''
    if centenas <= 3:
        centenas_rom = 'C' * centenas
    elif centenas == 4:
        centenas_rom = 'CD'
    elif centenas <= 8:
        centenas_rom = 'D' + ('C' * (centenas - 5))
    else:
        centenas_rom = 'CM'
    
    resto = resto - (centenas * 100)
    decenas = resto // 10

    decenas_rom = ''
    if decenas <= 3:
        decenas_rom = 'X' * decenas
    elif decenas == 4:
        decenas_rom = 'XL'
    elif decenas <= 8:
        decenas_rom = 'L' + ('X' * (decenas - 5))
    else:
        decenas_rom = 'XC'
    
    unidades = resto - (decenas * 10)
    unidades_rom= ''

    if unidades <= 3:
        unidades_rom = 'I' * unidades
    elif unidades == 4:
        unidades_rom = 'IV'
    elif unidades <= 8:
        unidades_rom = 'V' + ('I' * (unidades - 5))
    else:
        unidades_rom = 'IX'

    # C CC CCC CD D DC DCC DCCC CM 

    return miles_rom + centenas_rom + decenas_rom + unidades_rom

print(num2roman(3789))

def roman2num(roman):
    # MMMCMLXXXIX
    if len(roman) == 0:
        return 0
    # detectar si hay miles
    miles = 0
    if roman[0] == 'M':    
        for letra in roman:
            if letra != 'M':
                break
            miles += 1
    resto = roman[miles:]

    centenas = 0
    if len(resto) > 0 and (resto[0] == 'C' or resto[0] == 'D'):
        centenas_rom = ''
        for letra in resto:
            if letra != 'C' and letra != 'D' and letra != 'M':
                break
            centenas_rom += letra
        
        if 'D' not in centenas_rom and 'M' not in centenas_rom:
            centenas = len(centenas_rom)
        elif centenas_rom == 'CD':
            centenas = 4
        elif 'D' in centenas_rom: #D DC DCC DCCC
            centenas = len(centenas_rom) + 4
        else:
            centenas = 9
    
        resto = resto[len(centenas_rom):]

    decenas = 0
    if len(resto) > 0 and (resto[0] == 'X' or resto[0] == 'L'):
        decenas_rom = ''
        for letra in resto:
            if letra != 'X' and letra != 'L' and letra != 'C':
                break
            decenas_rom += letra
        
        if 'L' not in decenas_rom and 'C' not in decenas_rom:
            decenas = len(decenas_rom)
        elif decenas_rom == 'XL':
            decenas = 4
        elif 'L' in decenas_rom: #L LX LXX LXXX
            decenas = len(decenas_rom) + 4
        else:
            decenas = 9
        
        resto = resto[len(decenas_rom):]
    
    unidades = 0

    
    
    return (miles * 1000) + (centenas * 100) + (decenas * 10)


print(roman2num('MMMDCCLXXXIX'))


texto1 = '''El British Aircraft Corporation TSR-2 (en inglés: Tactical Strike and Reconnaisance, [Mach 2]; traducido al español: «Bombardero Táctico y de Reconocimiento, Mach 2») fue un proyecto desarrollado por la British Aircraft Corporation (BAC) para un bombardero táctico y avión de [{reconocimiento}] que estaba <previsto> que entrase en servicio con la Real Fuerza Aérea, pero que fue cancelado a mediados de los años 1960.'''

texto2 = ''' 
(defun should-be-constant ()
  '(one two three))

(let ((stuff (should-be-constant)))
  (setf (third stuff 'bizarre))

(should-be-constant)
'''

texto3 = "Para este ejercicio, debemos procurar que cierren todos (todos) los paréntesis, llaves {}, y corchetes []. También debemos cerrar las comillas simples y dobles. Y que queden bien anidadas. (Por ejemplo, esto está mal: [{hola]})"

calces = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
}

def parentesis(texto):
    aperturas = '([{<'
    cierres = ')]}>'

    pila = []
    
    for letra in texto:
        if letra in aperturas:
            pila.append(letra)
        elif letra in cierres:
            if len(pila) == 0:
                return False
            ultima_apertura = pila.pop()

            if calces[ultima_apertura] != letra:
                return False
    
    return len(pila) == 0

import pdb; pdb.set_trace()


    
