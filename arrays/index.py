edad = 30
lista = [-4, 3, 6, 10, 1]

def suma10(edad):
    edad += 10
    print(f'El edadero es {edad}')

def burbuja(arr):
    if len(arr) <= 1:
        return

    for tope in range(len(arr) - 1, 0, -1):
        for i in range(tope):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    print(arr)

nombres = ['Carlos', 'Xavi', 'Xavi', 'Sole', 'Sole', 'Sole', 'Kayla', 'Yojan', 'Yohan']

def eliminarDup(arr):
    nueva = [arr[0]]
    for i in range(len(arr)):
        if arr[i] == nueva[-1]:
            pass
        else:
            nueva.append(arr[i])
    return nueva

def minComienzo(arr):
    if len(arr) <= 1:
        return arr
    
    min = arr[0]
    pos_min = 0

    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            pos_min = i
    
    for i in range(pos_min - 1, 0, -1):
        arr[i+1] = arr[i]
    
    arr[0] = min
    return arr


# [-2, 2] => [0, 0]
def distancia(p1, p2):
    dist_x = abs(p1[0] - p2[0])
    dist_y = abs(p1[1] - p2[1])
    
    d_total = dist_x + dist_y
    return d_total

def camion(cliente1, cliente2, cliente3):
    # 1. Saco los bordes del cuadrado que engloba los 3 clientes
    x_inicio = min(cliente1[0], cliente2[0], cliente3[0])
    x_fin = max(cliente1[0], cliente2[0], cliente3[0])
    y_inicio = min(cliente1[1], cliente2[1], cliente3[1])
    y_fin = max(cliente1[1], cliente2[1], cliente3[1])

    # 2. Asumimos que el punto de abajo a la izquierda es el minimo
    dist_minima = distancia(cliente1, [x_inicio, y_inicio]) + distancia(cliente2, [x_inicio, y_inicio]) + distancia(cliente3, [x_inicio, y_inicio])
    punto_minimo = [x_inicio, y_inicio]

    # 3. Recorro todos los puntos internos de ese cuadrado, intentando encontrar el punto con la distancia total minima
    for x in range(x_inicio, x_fin + 1):
        for y in range(y_inicio, y_fin + 1):
            dist_ahora = distancia(cliente1, [x, y]) + distancia(cliente2, [x, y]) + distancia(cliente3, [x, y])
            if dist_ahora < dist_minima:
                dist_minima = dist_ahora
                punto_minimo = [x, y]
    
    print(f'La disntacia mínima es {dist_minima}')
    return punto_minimo





import pdb; pdb.set_trace()
