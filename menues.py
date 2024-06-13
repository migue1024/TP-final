from claseUsuario import usuario
from conexion import micursor,miconexion

on = 1
while on == 1:
    print("\nHola bienvenido a la aplicacion de videoclub")
    try:
        opcion = int(input("Por favor ingrese:\n1. Si quiere menu Usuario.\n2. Si quiere menu pelicula.\n3. Salir.\n"))
        if opcion == 1:
            on2 = 1
            while on2 == 1:
                print("\nEste es el menu de usuario")
                try:
                    opcion2 = int(input("Por favor ingrse:\n1. Ver datos.\n2. Modificar datos.\n3. Darse de alta.\n4. Darse de baja.\n5. Atras.\n6. Salir\n"))
                    if opcion2 == 1:
                        numcod = int(input("¿cual es su codigo?"))
                        micursor.execute (f"select * from usuarios where codigo_usuario = {numcod}")
                        datos = micursor.fetchall()
                        user1 = usuario(datos[0][1],datos[0][2],datos[0][3],datos[0][4],datos[0][5],datos[0][6])                                     
                        user1.verdatos()
                        # accion de ver datos (sentencia sql que trae los datos del usuario)
                    elif opcion2 == 2:
                        pass
                        # accion de modificar datos (sentencia sql que modifica los datos del usuario)
                    elif opcion2 == 3:
                        pass
                    elif opcion2 == 4:
                        pass
                    elif opcion2 == 5: # VOLVER PARA ATRAS
                        on2 = 0
                        #volver para atras
                    elif opcion2 == 6:
                        print("Gracias usar la apliacion")
                        #quit()
                        on2 = 0
                        on = 0
                    else:
                        print("Opcion incorrecta")
                except ValueError:
                    print("ingrese un numero entero")
        elif opcion == 2:
            print("Este es el menu de peliculas")
        elif opcion == 3:
            print("Gracias por usar la aplicacion")
            on = 0
        else:
            print("Opcion incorrecta")
    except ValueError:
        print("Debe ingresar un numero entero")