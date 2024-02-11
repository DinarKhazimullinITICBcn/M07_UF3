def buscar(conectar) :
    #Query sql que selecciona tot de la taula character
    sql = '''SELECT * FROM character;'''
    #Executa la variable
    conectar.execute(sql)
    #COm ens donara mes d'una fila probablement, utilitzem fetchall
    characters = conectar.fetchall()
    print('Characters:')
    #Fem un for que recorrer tots el personatges
    for character in characters :
        print(character)