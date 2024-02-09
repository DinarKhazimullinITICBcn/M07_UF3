def crearCharacter(conectar) : 
    sql = """
            SELECT character_id
            FROM character
            ORDER BY character_id DESC
            LIMIT 1;
        """
    conectar.execute(sql)
    result = conectar.fetchall()
    
    sql = """INSERT INTO CHARACTER VALUES ({id}, 'Dinar', 20, 'S tier', 'USEC', 'Infantry')"""
