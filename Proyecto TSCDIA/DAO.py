import mysql.connector

class  DAO:

    def __init__(self):
        self.conn = None
        self.conectar()
        self.connected = False

    # Coneccion
    def conectar(self):
        if not self.connected:
            self.conn = mysql.connector.connect(user='root', password = 'root', host = 'localhost', database = 'mydb', port = '3306' )
            self._cursor = self.conn.cursor()
            if self.conn.is_connected():
                print("Conectando")
                self.connected = True
    #--------------------------------------------------
    # Desconeccion
    def desconectar(self):
        self.connected = False
        self.conn.close()
        if self.conn:
            print("Desconectado")
    #------------------------------------------------------
    # Cosultas a la Base de Datos
    def consultar(self, sql):
        self._cursor.execute(sql)
        resultado = self._cursor.fetchall()
        return resultado
    #----------------------------------------------------
    # Alteracion a la Base de Datos
    def insertarModificrEliminar(self,sql):
        self._cursor.execute(sql)
        self.conn.commit() #Confirmacion de la acción