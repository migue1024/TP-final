import mysql.connector

miconexion = mysql.connector.connect(host = "localhost",user= "root",password = "",database = "Videoclub")
micursor = miconexion.cursor()
#crear base de datos
#micursor.execute("drop database if exist Videoclub")
#micursor.execute("create database Videoclub")
#micursor.execute("use Videoclub")
#crear tablas
#micursor.execute("create table Usuarios(id int primary key auto_increment,codigo usuario int,nombre text,dni int,domicilio text,telefono int,email text,situacion text,codigo text null)")
#micursor.execute()

sql ="insert into usuarios(codigo_usuario,nombre,dni,domicilio,telefono,email,situacion,codigo) values (%s,%s;%s,%s,%s,%s,%s,%s)"
val =[
    ("001","Andres","12243648";"Aruba 1236","13263953",)
]