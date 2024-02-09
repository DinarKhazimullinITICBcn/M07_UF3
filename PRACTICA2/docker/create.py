import connection
def consulta() :
    sql = '''CREATE TABLE CHARACTER(
                    character_id SERIAL PRIMARY KEY,
                    character_name VARCHAR(255) NOT NULL,
                    character_age VARCHAR(255) NOT NULL,
                    character_power VARCHAR(255) NOT NULL,
                    character_faction VARCHAR(255) NOT NULL,
                    character_class VARCHAR(255)
    )'''
    connection.conectar.execute(sql)
    connection.conn.commit()