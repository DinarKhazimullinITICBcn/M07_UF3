passwd= input('Introdueix una contrasenya: ')
if passwd in ('Peliñ4nd0#'):
  print('Correcte')
else:
  print('Incorrecte')

#Errors:
  #El string de input estaba obert amb ' y tancat amb "
  #El condicional utilitzaba una variable no existent
  #La contrasenya obria amb [ i tancaba amb )
  #Else no tenia : despres de else