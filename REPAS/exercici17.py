inputUsuari = input('Insereix una frase\n')
fraseSplit = inputUsuari
fraseSenseRepetir = ''
for i in range(len(fraseSplit)):
    if fraseSplit[i] not in fraseSenseRepetir:
        fraseSenseRepetir += fraseSplit[i]
tuplaFrase = fraseSenseRepetir.split(' ')
print(tuplaFrase)
