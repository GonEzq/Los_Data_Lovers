import pandas as pd;
import DAO;

class DAOlocalizacion(DAO.DAO):

    def __init__(self):
        super().__init__()
        self.localizacion = 'Localización'

    def INSERTexel(self, rutaExel):

        self.conectar()

        df = pd.read_excel(rutaExel, sheet_name = self.localizacion) # Cargo la hoja Localización 
        for index, row in df.iterrows():
            #El id es autoincremental
            ciudad = row['Localización']
            sql = f"INSERT INTO localizacion (estado) VALUES ('{ciudad}')"
            self.insertarModificrEliminar(sql)
        
        self.desconectar()

    def INSERT(self, estado):

        self.conectar()

        sql = f"INSERT INTO localizacion (estado) VALUES ('{estado}')"

        self.insertarModificrEliminar(sql)

        self.desconectar()

        return estado