numeroUsuari = int(input('Insereix un numero entre 1 i 10\n'))
taulaMultiplicacio = []
if numeroUsuari > 0 and numeroUsuari < 11 :
    for i in range(1, 11) :
        taulaMultiplicacio.append(numeroUsuari * i)
print(taulaMultiplicacio)