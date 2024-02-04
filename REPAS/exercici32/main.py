import llista
while True:
    numerosUsuari = input('Introdueix 10 numeros separats per espai\n')
    if numerosUsuari.count(' ') == 9:
        numeros = list(map(int, numerosUsuari.split(' ')))
        numerosAmbQuadrat = llista.quadrats(numeros)
        print(numerosAmbQuadrat)
        break
    else:
        print('Has posat un numero de numeros menor o major de 10')
