import llista
llista_compra = {100: 10, 250: 5, 1500: 30}
iva = int(input('Insereix l\'iva (4, 10, 21)'))
print(llista.calcular_total_compra(llista_compra, iva))
