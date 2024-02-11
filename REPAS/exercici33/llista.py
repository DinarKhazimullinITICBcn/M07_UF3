def calcular_total_compra(llista_compra, iva):
    total = 0
    resultats = []
    for i, (preu, descompte) in enumerate(llista_compra.items(), start=1):
        preuDescomptat = preu - (preu * descompte / 100)
        total += preuDescomptat
        preuIva = preuDescomptat + (preuDescomptat * iva / 100)
        resultats.append(f'Producte {i}: {preuIva}')
    totalIva = total + (total * iva / 100)
    resultats.append(f'Total: {totalIva}')
    return '\n'.join(resultats)