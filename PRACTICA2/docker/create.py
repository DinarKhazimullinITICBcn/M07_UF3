def crearCharacter(conn, conectar) : 
    #Agafar la ultima id de la nostra base de dades ja que no tinc id auto incremental
    sql = """
            SELECT character_id
            FROM character
            ORDER BY character_id DESC
            LIMIT 1;
        """
    #Executar aquesta query
    conectar.execute(sql)
    #Agafem unicament un, pero de tota manera en el sql ho limitem a 1
    result = conectar.fetchone()
    #Asignem el id en cas de que no estigui buit
    if result :
        id = result[0]
    else:
        id = None
    #En cas de que no estigui buit li sumem +1 i afegim la informacio necesaria a la nostra base de dades
    if id is not None :
        id += 1
        sql = f"""INSERT INTO CHARACTER VALUES (%s, 'Dinar', 20, 'S tier', 'USEC', 'Infantry')"""
        #Executem la query amb el sql i la id que substitueix %s
        conectar.execute(sql, (id,))
        #Guarda les dades a la base
        conn.commit()
    else :
        print("Error afegint usuari")
