import pandas as pd
from DAO import DAO
from DAOindustria import DAOindustria
from DAOsubindustria import DAOsubindustria
from DAOlocalizacion import DAOlocalizacion

class DAOempresas(DAO):
    def __init__(self):
        super().__init__()
        self.rutaExel = 'Sistema DAO\\LISTA DE EMPRESAS DEL SP500.xls'
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
            if index >= len(df):
                break
            #El id es autoincremental
            empresa = row['Empresa']
            industria = row['Industria']
            subIndustria = row['Sub_industria']
            localizacion = row['Localización']
            empleados = row['Cant. Empleos']
            capitalizacion = row['Valor de Mercado']
           
            id_industria = f"select i.id_tipoindustria from industria i where i.Mercado = '{industria}'"
            id_industria = self.consultar(id_industria)[0][0]

            id_subindustria = f"select s.id_subindustria from subindustria s where s.Especializacion = '{subIndustria}'"
            id_subindustria = self.consultar(id_subindustria)[0][0]
 
            
            id_localizacion = f"select l.id_localizacion from localizacion l where l.estado = '{localizacion}'"
            id_localizacion = self.consultar(id_localizacion)[0][0]

            
            sql = f"INSERT INTO empresas (nombre_empresa,tipoindustria,subindustria,localizacion,Capitalizacion,Empleados) values (\"{empresa}\",{id_industria},{id_subindustria},{id_localizacion},{capitalizacion},{empleados})"
            
            # Es muy importante mencionar que "\" hace una excepcion a la regla (ESCAPAR) 
            # Dando la posibilidad de hacer esto: \"McDonad's\" sin que ' me de problemas

            self.insertarModificrEliminar(sql)

            print("Carga exitosa")

        self.desconectar()

    def INSERTManual(self):

        self.conectar()

        print("Ingrese los datos")
        empresa = input("Nombre de la Empresa: ")

        industria = input("Industria: ")
        self.confirmacion(industria,0)

        subIndustria = input("Sub Industria: ")
        self.confirmacion(subIndustria,1)

        localizacion = input("Estado/Pais: ")
        self.confirmacion(localizacion,2)

        empleados = input("Cantidad de Empleados: ")
        capitalizacion = input("Ingrese el valor del mercado actual: ")

        id_industria = f"select i.id_tipoindustria from industria i where i.Mercado = '{industria}'"
        id_industria = self.consultar(id_industria)[0][0]

        id_subindustria = f"select s.id_subindustria from subindustria s where s.Especializacion = '{subIndustria}'"
        id_subindustria = self.consultar(id_subindustria)[0][0]

        id_localizacion = f"select l.id_localizacion from localizacion l where l.estado = '{localizacion}'"
        id_localizacion = self.consultar(id_localizacion)[0][0]

        sql = f"INSERT INTO empresas (nombre_empresa,tipoindustria,subindustria,localizacion,Capitalizacion,Empleados) VALUES (\"{empresa}\", {id_industria}, {id_subindustria}, {id_localizacion}, {capitalizacion}, {empleados})"
        self.insertarModificrEliminar(sql)

        opc = input("¿Desea ingresar otra empresa?: ")
        if opc.upper() == "Y":
            self.INSERTManual()
        
        self.desconectar()

    def DELETE(self):

        self.conectar()

        id_Empresa = input("Ingrese El ID de la empresa a borrar: ")
        sql = f"DELETE FROM empresas WHERE id_empresa = '{id_Empresa}'"
        self.insertarModificrEliminar(sql)

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

    def SELECT(self, opc):

        self.conectar()

        if opc == 1: # Seleccionar todo
            
            sql = """SELECT e.nombre_empresa AS Nombre, i.Mercado AS Industria, s.Especializacion AS Sub_Industia, l.estado AS Estado, FORMAT(e.Capitalizacion, 0) AS Valor_de_Mercado, FORMAT(e.Empleados, 0) AS Empleados 
            FROM empresas e, industria i, subindustria s,localizacion l
            WHERE e.tipoindustria = i.id_tipoindustria AND e.subindustria = s.id_subindustria AND e.localizacion = l.id_localizacion ORDER BY e.Capitalizacion DESC"""

            print("Nombre | Industria | Sub_Industria | Estado | Valor_del_Mercado | Empleados")

            for columna in self.consultar(sql):
                print(f"{columna[0]} | {columna[1]} | {columna[2]} | {columna[3]} | {columna[4]} | {columna[5]}")

        elif opc == 2: # Seleccionar empresa mas Valiosa

            sql = """SELECT e.nombre_empresa AS Nombre, i.Mercado AS Industria, s.Especializacion AS Sub_Industia, l.estado AS Estado, FORMAT(e.Capitalizacion, 0) AS Valor_de_Mercado, FORMAT(e.Empleados, 0) AS Empleados
            FROM empresas e, industria i, subindustria s,localizacion l 
            WHERE e.tipoindustria = i.id_tipoindustria AND e.subindustria = s.id_subindustria AND e.localizacion = l.id_localizacion ORDER BY e.Capitalizacion DESC LIMIT 1"""

            print("Nombre | Industria | Sub_Industria | Estado | Valor_del_Mercado | Empleados")

            for columna in self.consultar(sql):
                print(f"{columna[0]} | {columna[1]} | {columna[2]} | {columna[3]} | {columna[4]} | {columna[5]}")

        elif opc == 3: # Empresa con más Empleados

            sql = """SELECT e.nombre_empresa AS Nombre, i.Mercado AS Industria, s.Especializacion AS Sub_Industia, l.estado AS Estado, FORMAT(e.Capitalizacion, 0) AS Valor_de_Mercado, FORMAT(e.Empleados, 0) AS Empleados
            FROM empresas e, industria i, subindustria s,localizacion l 
            WHERE e.tipoindustria = i.id_tipoindustria AND e.subindustria = s.id_subindustria AND e.localizacion = l.id_localizacion ORDER BY e.Empleados DESC LIMIT 1"""

            print("Nombre | Industria | Sub_Industria | Estado | Valor_del_Mercado | Empleados")

            for columna in self.consultar(sql):
                print(f"{columna[0]} | {columna[1]} | {columna[2]} | {columna[3]} | {columna[4]} | {columna[5]}")
        
        self.desconectar()

    def confirmacion(self,verificar,linea):

        print("Estoy despues de Conectarme")

        industria = DAOindustria()
        subIndustria = DAOsubindustria()
        localizacion = DAOlocalizacion()

        if linea == 0:

            sql = "SELECT Mercado FROM industria"
            tindu = self.consultar(sql) # Tabla industria
            print(tindu)
            print(verificar)

            if verificar not in [row[0] for row in tindu]:
               print(f"La Industria ingresada no se encuentra en la Tabla industria {verificar}, sera agregada.")
               industria.INSERT(verificar)

        elif linea == 1:

            sql = "SELECT Especializacion FROM subindustria"
            tsubindu = self.consultar(sql) # Tabla subindustria

            if verificar not in [row[0] for row in tsubindu]:
                print(f"La Sub_Industria ingresada no se encuentra en la Tabla subindustria {verificar}, sera agregada.")
                subIndustria.INSERT(verificar)

        elif linea == 2:

            sql = "SELECT estado FROM localizacion"
            tlocal = self.consultar(sql) # Tabla localizacion

            if verificar not in [row[0] for row in tlocal]:
                print(f"La Localizacion ingresada no se encuentra en la Tabla localizacion {verificar}, sera agregada.")
                localizacion.INSERT(verificar)

    def crearDataBase(self):
        sql = """-- MySQL Workbench Forward Engineering

        SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
        SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
        SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

        -- -----------------------------------------------------
        -- Schema mydb
        -- -----------------------------------------------------

        -- -----------------------------------------------------
        -- Schema mydb
        -- -----------------------------------------------------
        CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
        USE `mydb` ;

        -- -----------------------------------------------------
        -- Table `mydb`.`Industria`
        -- -----------------------------------------------------
        CREATE TABLE IF NOT EXISTS `mydb`.`Industria` (
            `id_tipoindustria` INT NOT NULL AUTO_INCREMENT,
            `Mercado` VARCHAR(100) NOT NULL,
            PRIMARY KEY (`id_tipoindustria`))
        ENGINE = InnoDB;


        -- -----------------------------------------------------
        -- Table `mydb`.`Subindustria`
        -- -----------------------------------------------------
        CREATE TABLE IF NOT EXISTS `mydb`.`Subindustria` (
            `id_subindustria` INT NOT NULL AUTO_INCREMENT,
            `Especializacion` VARCHAR(100) NOT NULL,
            PRIMARY KEY (`id_subindustria`))
        ENGINE = InnoDB;


        -- -----------------------------------------------------
        -- Table `mydb`.`Localizacion`
        -- -----------------------------------------------------
        CREATE TABLE IF NOT EXISTS `mydb`.`Localizacion` (
            `id_localizacion` INT NOT NULL AUTO_INCREMENT,
            `estado` VARCHAR(100) NOT NULL,
            PRIMARY KEY (`id_localizacion`))
        ENGINE = InnoDB;


        -- -----------------------------------------------------
        -- Table `mydb`.`Empresas`
        -- -----------------------------------------------------
        CREATE TABLE IF NOT EXISTS `mydb`.`Empresas` (
            `id_empresa` INT NOT NULL AUTO_INCREMENT,
            `nombre_empresa` VARCHAR(100) NOT NULL,
            `tipoindustria` INT NOT NULL,
            `subindustria` INT NOT NULL,
            `localizacion` INT NOT NULL,
            `Capitalizacion` FLOAT NOT NULL,
            `Empleados` INT NOT NULL,
            PRIMARY KEY (`id_empresa`, `tipoindustria`, `subindustria`, `localizacion`),
            INDEX `fk_Empresas_Industria1_idx` (`tipoindustria` ASC) VISIBLE,
            INDEX `fk_Empresas_Subindustria1_idx` (`subindustria` ASC) VISIBLE,
            INDEX `fk_Empresas_Localizacion1_idx` (`localizacion` ASC) VISIBLE,
            CONSTRAINT `fk_Empresas_Industria1`
                FOREIGN KEY (`tipoindustria`)
                REFERENCES `mydb`.`Industria` (`id_tipoindustria`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
            CONSTRAINT `fk_Empresas_Subindustria1`
                FOREIGN KEY (`subindustria`)
                REFERENCES `mydb`.`Subindustria` (`id_subindustria`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
            CONSTRAINT `fk_Empresas_Localizacion1`
                FOREIGN KEY (`localizacion`)
                REFERENCES `mydb`.`Localizacion` (`id_localizacion`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION)
        ENGINE = InnoDB;


        SET SQL_MODE=@OLD_SQL_MODE;
        SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
        SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;"""

        super().crearDataBase(sql)
        
