inputUsuari = input("Introdueix de 1 a 3 paraules\n")
paraules = inputUsuari.split(' ')
if len(paraules) > 0 and len(paraules) < 4 :
    for paraula in paraules :
        print(f'La paraula es: {paraula}')
        print(f'La longitud es: {len(paraula)}')
        print(f'El primer caracter es: {paraula[0]}')
        print(f'El ultim caracter es: {paraula[-1]}')