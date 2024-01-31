while True:
    numerosUsuari = input('Introdueix 10 numeros separats per espai\n')
    if numerosUsuari.count(' ') == 9:
        tupla = tuple(map(int, numerosUsuari.split(' ')))
        tupla = tuple(sorted(tupla))
        print(tupla)
        break
    else:
        print('Has posat un numero de numeros menor o major de 10')
