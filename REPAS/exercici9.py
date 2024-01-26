inputUsuari = input('Insereix dos paraules\n')
paraules = inputUsuari.split(' ')
if len(paraules) > 0 and len(paraules) < 3 :
    print(paraules[1][0:2] + paraules[0][2:], paraules[0][0:2] + paraules[1][2:])