import psycopg2

try:
    connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='12345',
        database='base_app_pulmones'
    )
    print("nice")
    cursor=connection.cursor()
    cursor.execute("SELECT version()")
    row=cursor.fetchone()
    print(row)
    cursor.execute("SELECT * FROM registros")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("fin connection")