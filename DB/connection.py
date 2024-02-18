import mysql.connector
from mysql.connector import Error

class DAO(): # Data Access Object
    def __init__(self) -> None:
        try: 
            self.conexion=mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="123456",
                db="universidad"
            )
        except Error as ex:
            print("Error al intentar la conexion: {0}".format(ex))
            
    def listarCursos(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM curso ORDEN BY nombre ASC")
                resultados=cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))