def buscar(conectar) :
    sql = '''SELECT * FROM character;'''
    conectar.execute(sql)
    characters = conectar.fetchall()
    print('Characters:')
    for character in characters :
        print(character)