numerosUsuari = input('Introdueix 10 numeros separats per espai\n')
if numerosUsuari.count(' ') == 9:
    llistaNumeros= numerosUsuari.split(' ')
    for i in range(len(llistaNumeros)) :
        llistaNumeros[i] = int(llistaNumeros[i])
    total = sum(llistaNumeros)
    mitjana = total / len(llistaNumeros)
    print(f'Numeros del usuari: {llistaNumeros}')
    print(f'Suma total: {total}')
    print(f'Mitjana: {mitjana}')
else :
    print('Numero menor o major de 10')