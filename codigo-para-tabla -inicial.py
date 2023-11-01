import sqlite3

mi_conexion = sqlite3.connect("normativas")
mi_cursor = mi_conexion.cursor()

sql = "CREATE TABLE IF NOT EXISTS Normativa ( id_Normativa INT, TipoNormativa VARCHAR, NroNormativa INT, Fecha VARCHAR, Nombre VARCHAR, Descripcion VARCHAR, Categoria VARCHAR, Jurisdiccion VARCHAR, OrganoLegislativo VARCHAR, PalabrasClave VARCHAR)"
mi_conexion.execute(sql)
mi_cursor.execute('''
    INSERT INTO Normativa (id_Normativa, TipoNormativa, NroNormativa, Fecha, Nombre, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabrasClave)
    VALUES (1, "Ley", 20744, "13/05/1976", "Ley de Contrato de Trabajo", "Legisla sobre toda actividad lícita que se preste en favor de quién tiene la
    facultad de dirigirla, mediante el pago de una renumeración", "Laboral", "Nacional", "Congreso",
    "Trabajo - Contrato - Trabajador-Dependencia-Empleador")
    ''')

mi_cursor.execute('''
    INSERT INTO Normativa (id_Normativa, TipoNormativa, NroNormativa, Fecha, Nombre, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabrasClave)
    VALUES (2, "Ley", 27555, "5/2/2021", "Regimen de Teletrabajo", "Legisla acerca del contrato de trabajo cuando el mismo se realiza, total o
    parcialmente en el domicilio del trabajador o en lugares diferentes al del establecimiento del empleador,
    mediante la utilización de TIC (tecnologías de la información y comunicación).", "Laboral", "Nacional", "Congreso",
    "Distancia- Teletrabajo - TIC")
    ''')

mi_cursor.execute('''
    INSERT INTO Normativa (id_Normativa, TipoNormativa, NroNormativa, Fecha, Nombre, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabrasClave)
    VALUES (3, "Ley", 7462, "10/1/1988", "Ejercicio Profesional de la Infórmatica en Córdoba", "Establece la creación, funciones y atribuciones del CPCIPC,
    como así también los derechos, deberes y obligaciones de estos profesionales para con sus colegas,
    clientes y público en general", "Laboral", "Provincial", "Legislatura",
    "CPCIPC - Ética-Derechos-Obligaciones")
    ''')

mi_cursor.execute('''
    INSERT INTO Normativa (id_Normativa, TipoNormativa, NroNormativa, Fecha, Nombre, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabrasClave)
    VALUES (4, "Ley", 14250, "13/10/1953", "Convenciones Colectivas de Trabajo", "Legisla sobre las convenciones colectivas de trabajo que se celebren entre una
    asociación profesional de empleadores, un empleador o un grupo de empleadores, y una
    asociación profesional de trabajadores con personalidad gremial.","Gremial", "Nacional", "Congreso",
    "CCT - Paritarias - Trabajo")
    ''')

mi_cursor.execute('''
    INSERT INTO Normativa (id_Normativa, TipoNormativa, NroNormativa, Fecha,  Nombre, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabrasClave)
    VALUES (5, "Ley", 19550, "30/3/1984", "Sociedades Comerciales", "Establece los distintos tipos societarios admitidos en el  Código Civil
    y Comercial de la Nación, como así también los derechos y las obligaciones que se derivan del contrato
    para los socios y la estructura de la sociedad.", "Comercial", "Nacional", "Congreso",
    "Socio- Sociedades - Societario")
    ''')

mi_cursor.execute('''
    INSERT INTO Normativa (id_Normativa, TipoNormativa, NroNormativa, Fecha, Nombre, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabrasClave)
    VALUES (6, "Ley", 24241, "14/4/1988", "Sistema Integrado de Jubiliaciones y Pensiones", "Dispone la creación del Sistema Integrado de Jubilaciones y
    Pensiones (SIJP), coexisten dos regímenes: uno de reparto,
    administrado por el Estado a través de la Administración Nacional de
    la Seguridad Social (ANSeS), y otro de capitalización, administrado
    por sociedades de capital privado o público, denominadas
    Administradoras de Fondos de Jubilaciones y Pensiones (AFJP).", "Previsional", "Nacional", "Congreso",
    "SIJP-Reparto-ANSES- AFJP.")
    ''')

mi_cursor.execute('''
    INSERT INTO Normativa (id_Normativa, TipoNormativa, NroNormativa, Fecha, Nombre, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabrasClave)
    VALUES (7, "Ley", 24557, "3/10/1995", "Riesgos del Trabajo", "Legisla sobre la prevención de los riesgos del trabajo. Contingencias
    y situaciones cubiertas. Prestaciones dinerarias y en especie. Determinación y revisión
    de las incapacidades. Régimen financiero. Gestión de las prestaciones. Derechos,
    deberes y prohibiciones. Fondos de Garantía y de Reserva. Entes de Regulación y
    Supervisión. Responsabilidad Civil del Empleador.", "Laboral", "Nacional", "Congreso",
    "ART- Incapacidad- Prestaciones.")
    ''')
mi_cursor.execute('''
    INSERT INTO Normativa (id_Normativa, TipoNormativa, NroNormativa, Fecha, Nombre, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabrasClave)
    VALUES (8, "Ley", 23592, "23/8/1988", "Actos Discriminatorios", "Establece en qué casos se considera que alguién arbitrariamente impide, obstruye, restringe o de algún modo
    menoscaba el pleno ejercicio de otra sobre bases igualitarias de los derechos y garantías
    fundamentales reconocidos en la Constitución Nacional, estableciendo la reparación
    del daño moral y/o material ocasionados.", "Civil", "Nacional", "Congreso",
    "Discriminación- Daños- Reparación")
    ''')
mi_cursor.execute('''
    INSERT INTO Normativa (id_Normativa, TipoNormativa, NroNormativa, Fecha, Nombre, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabrasClave)
    VALUES (9, "Ley", 23551, "14/4/1988", "Asociaciones Sindicales", "Regula los tipos de asociaciones sindicales. Afiliación y desafiliación. Estatutos. Dirección
    y administración. Asambleas o congresos. Inscripción. Derechos y
    obligaciones de las asociaciones sindicales. Asociaciones sindicales con
    personería gremial. Federaciones y confederaciones. Representación sindical
    en la empresa. Tutela sindical. Prácticas desleales.", "Gremial", "Nacional", "Congreso",
    "Sindicato- Afiliado - Gremios ")
    ''')
sql = "CREATE TABLE IF NOT EXISTS TipoNormativa ( id_TipoNormativa INT, Tipo_Normativa VARCHAR)"
mi_conexion.execute(sql)
mi_cursor.execute('''
    INSERT INTO TipoNormativa ( id_TipoNormativa, Tipo_Normativa)
    VALUES (1, "Ley")
    ''')

sql = "CREATE TABLE IF NOT EXISTS Categoria ( id_Categoria INT, Categoria VARCHAR)"
mi_conexion.execute(sql)
mi_cursor.execute('''
    INSERT INTO Categoria ( id_Categoria, Categoria)
    VALUES (1, "Laboral")
    ''')
mi_cursor.execute('''
    INSERT INTO Categoria ( id_Categoria, Categoria)
    VALUES (2, "Gremial")
    ''')
mi_cursor.execute('''
    INSERT INTO Categoria ( id_Categoria, Categoria)
    VALUES (3, "Comercial")
    ''')
mi_cursor.execute('''
    INSERT INTO Categoria ( id_Categoria, Categoria)
    VALUES (4, "Previsional")
    ''')
mi_cursor.execute('''
    INSERT INTO Categoria ( id_Categoria, Categoria)
    VALUES (5, "Civil")
    ''')

sql = "CREATE TABLE IF NOT EXISTS Jurisdiccion ( id_Jurisdiccion INT, Jurisdiccion VARCHAR)"
mi_conexion.execute(sql)
mi_cursor.execute('''
    INSERT INTO Jurisdiccion ( id_Jurisdiccion, Jurisdiccion)
    VALUES (1, "Nacional")
    ''')
mi_cursor.execute('''
    INSERT INTO Jurisdiccion ( id_Jurisdiccion, Jurisdiccion)
    VALUES (2, "Provincial")
    ''')

sql = "CREATE TABLE IF NOT EXISTS OrganoLegislativo ( id_OrganoLegislativo INT, OrganoLegislativo VARCHAR)"
mi_conexion.execute(sql)
mi_cursor.execute('''
    INSERT INTO OrganoLegislativo ( id_OrganoLegislativo, OrganoLegislativo)
    VALUES (1, "Congreso")
    ''')
mi_cursor.execute('''
    INSERT INTO OrganoLegislativo ( id_OrganoLegislativo, OrganoLegislativo)
    VALUES (2, "Legislatura")
    ''')

mi_conexion.commit()
mi_conexion.close()
