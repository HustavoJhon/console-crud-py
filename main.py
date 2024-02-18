

def menuPrincipal():
    continuar=True
    while (continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("MENU PRINCIPAL")
            print("""
                1.- Listar Cursos
                2.- Registrar curso
                3.- Actualizar curso
                4.- ELiminar curso
                5.- Salir""")
            print("------------------------")
            option = int(input(">>>"))

            if option < 1 or option > 5:
                print("optionc Incorrecta, ingrese nuevamente")
            elif option == 5:
                continuar=False
                print("gracias por usar el sistema")
                break
            else:
                opcionCorrecta=True
                ejecutarOpcion(option)

def ejecutarOpcion(option):
    print(option)

menuPrincipal()