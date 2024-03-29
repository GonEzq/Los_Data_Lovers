import pandas as pd;
import DAO;

class DAOindustria(DAO.DAO):

    def __init__(self):
        super().__init__()
        self.industria = 'Industria'

    def INSERTexel(self, rutaExel):

        self.conectar()

        df = pd.read_excel(rutaExel, sheet_name =  self.industria) # Cargo la hoja Industria
        for index, row in df.iterrows():
            #El id es autoincremental
            nombreIndustria = row['Industria']
            sql = f"INSERT INTO industria (Mercado) VALUES ('{nombreIndustria}');"
            self.insertarModificrEliminar(sql)
        
        self.desconectar()

    def INSERT(self, Mercado):

        self.conectar()

        sql = f"INSERT INTO industria (Mercado) VALUES ('{Mercado}')"

        self.insertarModificrEliminar(sql)

        self.desconectar()

        return Mercado