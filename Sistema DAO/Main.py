from DAOempresas import DAOempresas



empresa = DAOempresas()

def MENU():
    
    print("/// MENU ///")
    print("1_ Insert")
    print("2_ Insert Exel")
    print("3_ Select")
    print("4_ Update")
    print("5_ Delete")
    print("6_ Salir")

    opc = int(input("Ingrese la opcion a seguir "))

    if opc == 1:

        empresa.INSERTManual()
        MENU()

    elif opc == 2:

        empresa.INSERTexle()
        MENU()

    elif opc == 3:

        print("/// MENU SELECT ///")
        print("1_ Mostrar todas las empresas")
        print("2_ Mostrar empresa con mayor valor en el mercado")
        print("3_ Mostrar la empresa con mayor cantidad de empleados")

        opc = int(input("Ingrece la opcion a seguir "))

        empresa.SELECT(opc)
        MENU()

    elif opc == 4:

        columna = input("Ingrese el nombre de la columna a cambiar en la tambla empresas: ")
        empresa.UPDATE(columna)
        MENU()

    elif opc == 5:
        
        empresa.DELETE()
        MENU()

    else:
        return None
    
MENU()
