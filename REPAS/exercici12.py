mesos = ('gener', 'febrer', 'marc', 'abril', 'maig', 'juliol', 'juny', 'agost', 'septembre', 'octubre', 'novembre', 'decembre')
while True :
    numeroUsuari = int(input('Insereix el numero del mes del 1 al 12. 0 per sortir del programa\n'))
    if numeroUsuari == 0 :
        break
    print(f'El mes amb el numero {numeroUsuari} es: {mesos[numeroUsuari-1]}')