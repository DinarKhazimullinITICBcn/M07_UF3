inputUsuari = input('Insereix dos paraules\n')
contadorDict = {}
contador = 0
if inputUsuari.count(' ') == 1 :
    tuplaInput = inputUsuari.split(' ')
    for i in range(len(tuplaInput[0])) :
        contador = 0
        if tuplaInput[0][i] in tuplaInput[1] :
            contador += 1
        contadorDict[tuplaInput[0][i]] = contador
print(contadorDict)
