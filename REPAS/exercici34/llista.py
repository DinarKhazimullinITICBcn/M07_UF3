def quadrat(num):
    return num ** 2
def aplica_funcio_a_llista(quadrat, llista):
    nova_llista = []
    for i in range(len(llista)) :
        nova_llista.append(quadrat(llista[i]))
    return nova_llista