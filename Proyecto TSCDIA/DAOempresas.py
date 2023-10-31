import pandas as pd;
import DAO, DAOindustria, DAOsubindustria, DAOlocalizacion;

class DAOempresas(DAO.DAO):
    def __init__(self):
        super().__init__()
        self.rutaExel = 'LISTA DE EMPRESAS DEL SP500.xls'
        self.empresas = 'Composición SP500'

    def INSERTexle(self):

        self.conectar()
        
        print("Leyendo Exel")
        #Industria
        industria = DAOindustria()
        industria.INSERTexel(self.rutaExel)
        
        #SubIndustria
        subIndustria = DAOsubindustria()
        subIndustria.INSERTexel(self.rutaExel)

        #Localizacion
        localizacion = DAOlocalizacion()
        localizacion.INSERTexel(self.rutaExel)

        df = pd.read_excel(self.rutaExel, sheet_name = self.empresas) # Cargo la hoja Composición SP500
        for index, row in df.iterrows():
            #El id es autoincremental
            empresa = row['Empresa']
            industria = row['Industria']
            subIndustria = row['Sub_industria']
            localizacion = row['Localización']
            sql = f"INSERT INTO empresas (nombre_empresa, Industria_Tipo_de_industria,Subindustria_idSubindustria,Localizacion_idLocalizacion) VALUES ('{empresa}', '{industria}', '{subIndustria}', '{localizacion}')"
            self.insertarModificrEliminar(sql)

        self.desconectar()

    def INSERTManual(self):

        self.conectar()

        print("Ingrese los datos")
        empresa = input("Nombre de la Empresa: ")
        industria = input("ID_Industria: ")
        subIndustria = input("ID_Sub industria: ")
        localizacion = input("ID_Localidad: ")
        sql = f"INSERT INTO empresas (nombre_empresa, Industria_Tipo_de_industria,Subindustria_idSubindustria,Localizacion_idLocalizacion) VALUES ('{empresa}', {industria}, {subIndustria}, {localizacion})"
        self.insertarModificrEliminar(sql)
        opc = input("¿Desea ingresar otra empresa?: ")
        if opc.upper() == "Y":
            self.cargaManual()
        
        self.desconectar()

    def DELETE(self):

        self.conectar()

        id_Empresa = input("Ingrese El ID de la empresa a borrar: ")
        sql = f"DELETE FROM empresas WHERE id_empresa = '{id_Empresa}'"

        self.desconectar()

    def UPDATE(self,columna):
        
        self.conectar()

        id_empresa = input("Ingrese el ID de la empresa a mopdificar: ")
        cambio = input("Cambiar por: ")
        if cambio.isnumeric():
            num = int(cambio)
            sql = f"UPDATE empresas SET {columna} = {num} WHERE id_empresa = {id_empresa}"
        else:
            sql = f"UPDATE empresas SET {columna} = '{cambio}' WHERE id_empresa = {id_empresa}"
        
        self.insertarModificrEliminar(sql)

        self.desconectar()

    def SELECT(self):

        self.conectar()

        sql = "SELECT * FROM empresas"

        self.desconectar()


        



