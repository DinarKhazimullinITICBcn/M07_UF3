def calcular_iva(preu, iva):
    ivaCalcul = 0
    if iva == 4:
        ivaCalcul = preu * 0.04
    elif iva == 10:
        ivaCalcul = preu * 0.10
    else:
        ivaCalcul = preu * 0.21 
    if ivaCalcul != 0:
        return f'El preu del usuari es: {preu}\nEl calcul del iva es: {ivaCalcul}\nEl preu total es: {preu + ivaCalcul}'
