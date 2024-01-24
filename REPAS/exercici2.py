preu = float(input("Insereix un preu en euros\n"))
iva = float(input("Insereix el IVA(4, 10, 21)"))
ivaCalcul = 0
if iva == 4:
    ivaCalcul = preu * 0.04
elif iva == 10:
    ivaCalcul = preu * 0.10
elif iva == 21:
    ivaCalcul = preu * 0.21
if ivaCalcul != 0:
    print('El preu del usuari es:', preu)
    print('El calcul del iva es: ', ivaCalcul)
    print('El preu total es:     ', preu + ivaCalcul)
else:
    print('Iva incorrecte')