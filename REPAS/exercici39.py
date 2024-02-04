n = int(input("Introdueix l’alçada del triangle (enter positiu): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")
#Errors:
  #El segon for tenia un problema amb range. El primer era que j no estaba definit perque ho definiem en el mateix for
  #El segon era el numero 1, que feia que el 1 no es mostres perque el for acababa quan arribaba a 1
  #EL tercer era que baixaba d'1 en 1, quan volem que vaigi 2 en 2