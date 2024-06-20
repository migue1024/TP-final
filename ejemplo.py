from conexion import miconexion,micursor



def iniciarSesion():
    nickname = str(input("ingrese su nickname(nombre) ")) #nombre
    password = int(input("ingrese su password(Dni) ")) #dni
    micursor.execute(f"select*from usuarios where nombre = '{nickname}' and dni = {password}") #'' comillas simples VARCHAR,sin comillas INT
    resultado = micursor.fetchall()
    return resultado

    '''if micursor.fetchall():
       resultado = micursor.fetchall()
       print(resultado)
       return resultado
    else:
        print("acceso denegado")'''


def menu():
    print("Bienvenido a la app A")
    opcion = int(input("ingrese 1: iniciar sesion,\ningrese 2:Registrarse,\ningrese 3:Salir\n"))
    if opcion == 1:
        datos = iniciarSesion()
        menuUsuario(datos)
    elif opcion == 2:
        registrarse()
    elif opcion == 3:
        print("gracias por usar la aplicacion")
        quit()
    else:
        print("elija una opcion correcta")

def registrarse():#darDEAlta
    #codigo_usuario = int(input("ingrese su codigo"))
    nombre = str(input("ingrese su nombre "))
    domicilio = str(input("ingrese su domicilio "))
    dni = int(input("ingrese su dni "))
    tel = int(input("ingrese su nro de telefono "))
    email = str(input("ingrese su email "))

    sql = ("insert into usuarios (codigo_usuario,nombre,dni,domicilio,telefono,email,situacion) values(%s,%s,%s,%s,%s,%s,%s)")
    val = (111,nombre,dni,domicilio,tel,email,"L")#codigo lo agrego a continuacion de 110
    micursor.execute(sql,val)
    miconexion.commit()

def menuUsuario(u):#u parametro comodin
    print("Bienvenido al menu usuario")
    opcion2 = int(input("ingrese 1 : si quiere ver sus datos,\n ingrese 2 : modificar sus datos,\n ingrese 3 : darse de baja.,\n ingrese 4 : ver todas las peliculas,\n ingrese 5 : ver disponibles,\n ingrese 6 : alquilar peliculas,\n ingrese 7 : devolver peliculas,\n ingrese 8 : atras,\n ingrese 9 : salir\n"))
    if opcion2 == 1:
        verDatos(u)

        
    elif opcion2 == 2:
        #modificarDatos() #llamado a la funcion
        pass
    elif opcion2 == 3:
        #darseDeBaja()
        pass
    elif opcion2 == 4:
        #verPeliculas()
        pass
    elif opcion2 == 5:
        #verDisponibles()
        pass
    elif opcion2 == 6:
        #alquilarPeliculas()
        pass
    elif opcion2 == 7:
        #devolverPeliculas()
        pass
    elif opcion2 == 8:
        #atras()
        pass
    elif opcion2 == 9:
        #salir()
        print("Gracias por usar la aplicacion")
        quit()
    else:
        print("Ingrese una opcion correcta")
        pass

def verDatos(u):
    print(u)






menu()