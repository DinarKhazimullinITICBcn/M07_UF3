def crearCharacter(conn, conectar) : 
    sql = """
            SELECT character_id
            FROM character
            ORDER BY character_id DESC
            LIMIT 1;
        """
    conectar.execute(sql)
    result = conectar.fetchone()
    if result :
        id = result[0]
    else:
        id = None
    if id is not None :
        id += 1
        sql = f"""INSERT INTO CHARACTER VALUES (%s, 'Dinar', 20, 'S tier', 'USEC', 'Infantry')"""
        conectar.execute(sql, (id,))
        conn.commit()
    else :
        print("Error afegint usuari")
