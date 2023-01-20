from PIL import Image

def cenit_polar(palabra):
    res = ''
    for letra in palabra:
        if letra not in 'cenitpolar':
            res += letra
        else:
            res += {
                'c': 'p',
                'e': 'o',
                'n': 'l',
                'i': 'a',
                't': 'r',
                'p': 'c',
                'o': 'e',
                'l': 'n',
                'a': 'i',
                'r': 't'
            }[letra]
    return res

def text2binary(palabra):
    return ''.join(format(ord(i), '08b') for i in palabra)


def descifrar(ruta_imagen):
    finalizador = '00110000'
    intentos = 10

    imagen = Image.open(ruta_imagen)
    pixel_map = imagen.load()
    pixel_start = 100

    letras_bin = []
    
    while True:
        letra_bin = ''
        for i in range(8):
            green = pixel_map[pixel_start + i, 100][1]
            print(green)
            if green % 2 == 0:
                letra_bin += '0'
            else:
                letra_bin += '1'
        
        if letra_bin == finalizador or intentos == 0:
            break
        letras_bin.append(letra_bin)
        intentos -= 1
        pixel_start += 8

    print(letras_bin)
    return letras_bin

    


def cifrar(mensaje, ruta_imagen):
    mensaje_bin = text2binary(mensaje + '0')
    print('mensaje binario' + mensaje_bin)

    imagen = Image.open(ruta_imagen)

    pixel_map = imagen.load()

    # for j in range(100, 150):
    #     for k in range(100, 150):
    #         red = pixel_map[j, k][0]
    #         green = pixel_map[j, k][1]
    #         blue = pixel_map[j, k][2]
    #         alpha = pixel_map[j, k][3]
    #         pixel_map[j,k] = (255, 0,0,alpha)

    pixel_start = 100
    for letra in mensaje_bin:
        red = pixel_map[pixel_start, 100][0]
        green = pixel_map[pixel_start, 100][1]
        blue = pixel_map[pixel_start, 100][2]
        alpha = pixel_map[pixel_start, 100][3]
        
        if letra == '0':
            if green % 2 != 0:
                green -= 1
        
        else: # letra == '1'
            if green % 2 == 0:
                green += 1
        
        pixel_map[pixel_start, 100] = (red, green, blue, alpha)
        pixel_start += 1
    
    imagen.save('mensaje.png', format='png')

    #import pdb; pdb.set_trace()
    ## 100x100 => (35, 42, 37, 255)

#cifrar('hello','bosque.png')
descifrar('mensaje.png')



