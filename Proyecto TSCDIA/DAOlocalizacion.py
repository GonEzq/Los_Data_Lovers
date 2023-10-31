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
            pais = row['País']
            sql = f"INSERT INTO localizacion (radicacion, pais) VALUES ('{ciudad}', '{pais}')"
            self.insertarModificrEliminar(sql)
        
        self.desconectar()