def amb_iva(ftotal, iva):
    ftotal += (ftotal * iva) / 100   
    return ftotal 
ftotal = int(input('Introdueix el preu de tot el carrito: '))
iva = 21
print(amb_iva(ftotal, iva))
#Errors:
  #En python les funcions s'han de declarar abans de ser cridades
  #El input hauria de ser int o sino les operacions matematiques repeteixen el string
  #La variable iva tenia que ser declarada abans de poder ser utilitzada com a parametre
  #Donar-li valor al iva desde els parametres no fa res
  #La operacio matematica per calcular l'iva no era la correcta