agendaContactes = {}
while True :
    nomContacte = input('Insereix un nom (Si vols para escriu No)\n')
    if nomContacte == 'No' :
        break
    edadUsuari = int(input('Insereix una edad\n'))
    if nomContacte not in agendaContactes :
        agendaContactes[nomContacte] = edadUsuari
    else :
        print("Aquest valor ja esta en la agenda")
print(agendaContactes)