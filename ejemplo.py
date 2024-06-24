#from conexion import miconexion,micursor

from conexion import miconexion,micursor



def iniciarSesion():
    nickname = str(input("ingrese su nickname(nombre) ")) #nombre
    password = int(input("ingrese su password(Dni) ")) #dni
    micursor.execute(f"select*from usuarios where nombre = '{nickname}' and dni = {password}") #'' comillas simples VARCHAR,sin comillas INT
    resultado = micursor.fetchall()
    #return resultado
    if len(resultado) != 0:
        print("Sesion iniciada correctamente")
    else:
        print("Acceso denegado")
        menu()

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
        menu()
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
        menuUsuario(u)
    
    elif opcion2 == 2:
        modificarDatos(u) #llamado a la funcion
        menuUsuario(u)

    elif opcion2 == 3:
        darseDeBaja(u)
        menu()#vuelve al menu de bienvenida
        
    elif opcion2 == 4:
        verPeliculas()
        menuUsuario(u)#vuelve al menu usuario
        
    elif opcion2 == 5:
        verDisponibles()
        menu()
        
    elif opcion2 == 6:
        alquilarPeliculas(u)
        menuUsuario(u)
        
    elif opcion2 == 7:
        devolverPeliculas(u)
        menuUsuario(u)
        
    elif opcion2 == 8:
        atras()
        menu()
        
    elif opcion2 == 9:
        salir()
        menu()
        #print("Gracias por usar la aplicacion")
        #quit()
    else:
        print("Ingrese una opcion correcta")
        

def verDatos(u):
    print(u)

def modificarDatos(u):
    opcion = int(input("ingrese:\n1,Modificar Telefonon\2,Modificar Direccion"))
    if opcion == 1:
        newtelefono = str(input("ingrese un nuevo numero de telefono"))
        micursor.execute(f"update usuarios set telefono = '{newtelefono}' where id_user = {u[0][0]}")
        miconexion.commit()
        print("el telefono ha sido modificado con exito")
    elif opcion == 2:
        newdireccion = str(input("Ingrese la nueva direcion"))
        micursor.execute(f"UPDATE usuarios set direccion = '{newdireccion}' where id_user = {u[0][0]}")
        miconexion.commit()
        print("La direccion ha sido modificada con exito")
    else:
        print("Ingrese una opcion valida")

def darseDeBaja(u):
    opcion =  int(input("¿Esta seguro que quiere darse de baja?\n1,Si\n2,No\n"))
    if opcion == 1:
        micursor.execute(f"DELETE from usuarios where id_user = {u[0][0]}")
        miconexion.commit()
        print("Usuario dado de bajja correctamente")
    else:
        menuUsuario()
    
def verPeliculas():
    micursor.execute("SELECT * from Peliculas")
    resultado = micursor.fetchall()
    for i in resultado:
        print(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10])


def verDisponibles():
    micursor.execute("SELECT * from Peliculas where situacion = 'L'" )
    resultado = micursor.fetchall()
    for i in resultado:
        print(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10])

def alquilarPeliculas(u):
    codigo_pelicula = int(input("Ingrese el codigo de la pelicula que quiere alquilqr"))
    micursor.execute(f"UPDATE usuarios set situacion = 'A' where id_user = {u[0][0]}")
    micursor.execute(f"UPDATE usuarios set codigo_pelicula = {codigo_pelicula} where id_user {u[0][0]}")
    micursor.execute(f"UPDATE peliculas set situacion = 'A' where codigo = {codigo_pelicula}")
    micursor.execute(f"UPDATE peliculas set codigo_usuario = '{u[0][1]}' where codigo = {codigo_pelicula}")
    miconexion.commit()
    print("Pelicula alquilada")

def devolverPeliculas(u):
    codigo_pelicula = int(input("Ingresae el codigo de la pelicula que quiere devolver"))
    micursor.execute(f"UPDATE peliculas set situacion = 'L'  where codigo = {codigo_pelicula}")
    micursor.execute(f"UPDATE peliculas set codigo_usuario = null where codigo = {codigo_pelicula}")
    micursor.execute(f"UPDATE usuarios set situacion = 'L' where id_user = {u[0][0]}")
    micursor.execute(f"UPDATE usuarios set codigo_pelicula = null where id_user = {u[0][0]}")
    miconexion.commit()
    print("Pelicula devuelta")

def atras():
    menu()


def salir():
    print("Gracias por usar la aplicacion")
    quit()
    

menu()










