import mysql.connector

class  DAO:

    def __init__(self):
        self.conn = None
        self.connected = False

    # Coneccion
    def conectar(self):
        if not self.connected:
            self.conn = mysql.connector.connect(user='root', password = 'root', host = 'localhost', database = 'mydb', port = '3306' )
            self._cursor = self.conn.cursor()
            if self.conn.is_connected():
                self.connected = True
    #--------------------------------------------------
    # Desconeccion
    def desconectar(self):
        self.connected = False
        self.conn.close()
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
    #----------------------------------------------------
    # Creacion de una Base de Datos
    def crearDataBase(self,sql):
        self.conn = mysql.connector.connect(user='root', password = 'root', host = 'localhost', port = '3306' ) # Para crear una Base de Datos me debo conectar a MySQL, la diferencia radica que no me conecto a un schema en particular
        self._cursor = self.conn.cursor() 
        sentencias = sql.split(';') # Al esperar multi sentencias genero una lista de estas haciendo que el ";" me marque el ritmo
        for sentencias in sentencias:
            if sentencias.strip():
                self._cursor.execute(sentencias)
        self.conn.commit()