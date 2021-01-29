from connection import connect

def create_db(db_name):
    sql = f"""
    CREATE DATABASE {db_name}
    """
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
    except:
        return 'This database name is already in use'
    conn.close()

def create_table(table_name, columns_names_types):
    sql = f"""
        CREATE TABLE {table_name} ({columns_names_types})
        """

    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
    except:
        return 'This table name is already in use'
    conn.close()

