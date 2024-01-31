numeroUsuari = int(input('Insereix un numero del 10 al 100\n'))
if numeroUsuari > 9 and numeroUsuari < 101 :
    tupla = tuple(range(1, numeroUsuari + 1))
    print(tupla)
else :
    print('Has insetir un numero fora del rang')