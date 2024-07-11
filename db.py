import sqlite3

def create_new_database(db_name):
    try:
        conn = sqlite3.connect(f'{db_name}.db')
        print("Base de datos creada con éxito")
    except sqlite3.Error as e:
        print("Base de datos no existe, se creará una nueva base de datos con el nombre especificado, error: ", e)
    finally:
        if conn:
            conn.close()


def get_db(db_name):
    conn = sqlite3.connect(DATABASE_NAME)
    print("Conexión a la base de datos establecida")
    return conn

def create_tables(db_name):
    db = get_db(db_name)
    cursor = db.cursor()
    
    try:
        with open('tables.sql', 'r') as file:
            sql_script = file.read()
        
        cursor.executescript(sql_script)
        print("Tablas creadas con éxito.")
    except Exception as e:
        print("Error al crear las tablas: ", e)
    finally:
        db.commit()
        db.close()


# Main
DATABASE_NAME = "tarea3emergentes"
create_new_database(DATABASE_NAME)

# Verificacion de la creacion de la base de datos
get_db(DATABASE_NAME)