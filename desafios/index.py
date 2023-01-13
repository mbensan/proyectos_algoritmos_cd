import itertools

def discos_duros(num_dds, num_comps, dds):
    posiciones_primarios = [primario for (primario, backup) in dds]
    posiciones_backups = [backup for (primario, backup) in dds]
    posiciones_dds = posiciones_primarios + posiciones_backups
    #+ [backup for (primario, backup) in dds]
    min_pos = min(posiciones_dds)
    max_pos = max(posiciones_dds)

    posiciones_comps = [comb for comb in itertools.combinations([elem for elem in range(min_pos, max_pos)], num_comps)]

    distancia = 10000000
    for combinacion in posiciones_comps:
        nueva_distancia = calcular_distancia(combinacion, dds)
        if nueva_distancia < distancia:
            distancia = nueva_distancia
    return distancia

     
def calcular_distancia(combinacion, dds):
    #[3, 5]
    distancias = 0
    for dd in dds:
        distancia_dd = 100000
        for comp in combinacion:
            distancia_dd_comp = abs(dd[0] - comp) + abs(dd[1] - comp)
            if distancia_dd_comp < distancia_dd:
                distancia_dd = distancia_dd_comp
        distancias += distancia_dd 

    return distancias   


        

fin = discos_duros(5, 2, [(6, 7), (-1, 1), (0, 1), (5, 2), (7, 3)])
import pdb; pdb.set_trace()

