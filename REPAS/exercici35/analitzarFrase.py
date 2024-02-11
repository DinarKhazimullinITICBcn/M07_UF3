def analitzaFrase(frase):
    paraules = frase.split()
    diccionari = {}
    for i in range(len(paraules)):
        paraula = paraules[i]
        diccionari[paraula] = len(paraula)
    return diccionari
