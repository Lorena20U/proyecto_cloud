import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost", 
        user="root",
        password="hola", 
        database="coandco"
    )

    if conn.is_connected():
        print("Conexión exitosa a la base de datos.")

    conn.close()

except mysql.connector.Error as e:
    print("Error al conectar a la base de datos:", e)
