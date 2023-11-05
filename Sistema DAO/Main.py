from DAOempresas import DAOempresas



empresa = DAOempresas()

def MENU():
    
    print("/// MENU ///")
    print("1_ Crear La Base de Datos (Se debe hacer una sola vez)")
    print("2_ Insert")
    print("3_ Insert Exel")
    print("4_ Select")
    print("5_ Update")
    print("6_ Delete")
    print("7_ Salir")

    opc = int(input("Ingrese la opcion a seguir "))

    if opc == 1:

        empresa.crearDataBase()
        print("Base de Datos creada")
        MENU()

    elif opc == 2:

        empresa.INSERTManual()
        MENU()

    elif opc == 3:

        empresa.INSERTexle()
        MENU()

    elif opc == 4:

        print("/// MENU SELECT ///")
        print("1_ Mostrar todas las empresas")
        print("2_ Mostrar empresa con mayor valor en el mercado")
        print("3_ Mostrar la empresa con mayor cantidad de empleados")

        opc = int(input("Ingrece la opcion a seguir "))

        empresa.SELECT(opc)
        MENU()

    elif opc == 5:

        columna = input("Ingrese el nombre de la columna a cambiar en la tambla empresas: ")
        empresa.UPDATE(columna)
        MENU()

    elif opc == 6:
        
        empresa.DELETE()
        MENU()

    else:
        return None
    
MENU()
