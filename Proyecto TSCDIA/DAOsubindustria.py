import pandas as pd;
import DAO;

class DAOsubindustria(DAO.DAO):
    
    def __init__(self):
        super().__init__()
        self.subIndustria = 'Sub_industria'

    def INSERTexel(self, rutaExel):

        self.conectar()

        df = pd.read_exel(rutaExel, sheet_name = self.subIndustria) # Cargo la hoja Sub_industria
        for index, row in df.iterrows():
            #El id es autoincremental
            nombreSubIndustria = row['Sub_industria']
            sql = f"INSERT INTO subindustria (Especializacion) VALUES ('{nombreSubIndustria}')"
            self.insertarModificrEliminar(sql)

        self.desconectar()