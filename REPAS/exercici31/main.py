import iva
preu = float(input("Insereix un preu en euros\n"))
iva_rate = float(input("Insereix el IVA(4, 10, 21)\n"))
resultat = iva.calcular_iva(preu, iva_rate)
print(resultat)
