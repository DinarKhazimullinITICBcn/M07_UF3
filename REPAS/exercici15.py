while True:
    numerosUsuari = input('Introdueix numeros separats per espai. Per acabar, escriu un 0\n')
    if numerosUsuari.count(' 0') == 1:
        numeros = numerosUsuari.split(' 0')[0]
        tupla = tuple(map(int, numeros.split(' ')))
        tupla = tuple(sorted(tupla))
        print(tupla)
        break
    else:
        print('No has posat un 0')