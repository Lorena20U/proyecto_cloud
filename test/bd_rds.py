import mysql.connector

config = {
    'user': 'admin',
    'password': 'admin123',
    'host': 'db.c9yjy3nmd8az.us-east-1.rds.amazonaws.com',
    'database': ''
}

try:

    conexion = mysql.connector.connect(**config)

    if conexion.is_connected():
        print("Conexión exitosa a la base de datos MySQL en AWS RDS")

    conexion.close()

except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
