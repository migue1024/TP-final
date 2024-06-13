from conexion import micursor,miconexion

class usuario:
    def __init__(self,codigousuario,nombre,dni,domicilio,telefono,email):
        self.__codigousuario = codigousuario
        self.__nombre = nombre
        self.__dni = dni
        self.__domicilio = domicilio
        self.__telefono = telefono
        self.__email = email
        self.__situacion = "L"
        self.__codigo = ""

    def get_codigousuario(self):
        return self.__codigousuario

    def set_codigousuario(self,newcodigousuario):
        self.__codigousuario = newcodigousuario

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self,newnombre):
        self.__nombre = newnombre

    def get_dni(self):
        return self.__dni

    def set_dni(self,newdni):
        self.__dni = newdni

    def get_domicilio(self):
        return self.__domicilio
    
    def set_domicilio(self,newdomicilio):
        self.__domicilio = newdomicilio
    
    def get_telefono(self):
        return self.__telefono

    def set_telefono(self,newtelefono):
        self.__telefono = newtelefono

    def get_email(self):
        return self.__email

    def set_email(self,newemail):
        self.__email = newemail

    def get_situacion(self):
        return self.__situacion
    
    def set_situacion(self,newsituacion):
        self.__situacion = newsituacion

    def get_codigo(self):
        return self.__codigo
    
    def set_codigo(self,newcodigo):
        self.__codigo = newcodigo

    def verdatos(self):
        micursor.execute(f"select * from usuarios where codigo_usuario = {self.get_codigousuario()}")
        dato = micursor.fetchone()
        for i in dato:
            print(i)
    
    
    def darsealta(self):
        pass

    def darsebaja(self):
        pass

    def modificardatos(self):
        pass

    def verpeliculas(self):
        pass

    def alquilarpeliculas(self):
        pass

    def devolverpeliculas():
        pass

user = usuario(109,"Miguel","112223333","Zuviria 5544",1212436,"migue@hotmail.com")


user.verdatos()