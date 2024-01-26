import random
numeroAEndevinar = random.randint(0, 100)
intents = 1
numeroPetit = 0
numeroGran = 100
while True :
    numero = float(input('Insereix un numero\n'))
    if numero == numeroAEndevinar :
        break
    elif numero < numeroAEndevinar :
        numeroPetit = numero
    else :
        numeroGran = numero
    intents += 1
    print(f'El numero esta entre el rang de {numeroPetit} i {numeroGran}')
print(f'Has endevinat.\nEl numero de intents es: {intents}')
