import mysql.connector

miconexion = mysql.connector.connect(host = "localhost",user= "root",password = "")#,database = "Videoclub")
micursor = miconexion.cursor()
#crear base de datos
micursor.execute("drop database if exists Videoclub")
micursor.execute("create database Videoclub")
micursor.execute("use Videoclub")
#crear tablas
micursor.execute("create table Usuarios(id int primary key auto_increment,codigo_usuario int,nombre text,dni int,domicilio text,telefono int,email text,situacion text,codigo text null)")
micursor.execute("create table Peliculas(id int primary key auto_increment,codigo_pelicula int,nombre text,genero text,situacion text,codigo text null)")

sql ="insert into usuarios (codigo_usuario,nombre,dni,domicilio,telefono,email,situacion,codigo) values (%s,%s,%s,%s,%s,%s,%s,%s)"
val = [
        (101,"Andres",12243648,"Aruba 1236",13263953,"andres@hotmail.com","L",None),
        (102,"Damian",28466992,"Formosa 2345",21356789,"damian@hotmail.com","L",None),
        (103,"Ariel",14568925,"Leon 345",19846573,"ariel@gmail.com","L",None),
        (104,"Mariela",29456789,"Suarez 1234",11626364,"mariela@yahoo.com.ar","L",None),
        (105,"Gabriel",19243551,"Aruba 649",15262953,"gabriel@hotmail.com","L",None),
        (106,"Alan",23466447,"Formosa 1624",14356689,"alan@hotmail.com","L",None),
        (107,"Nerea",29564328,"Leon 2205",19845120,"nerea@gmail.com","L",None),
        (108,"Giana",23450549,"Suarez 856",1149800755,"giana@yahoo.com.ar","L",None),
        (109,"Andrea",12242347,"Aruba 1809",14093752,"andrea@hotmail.com","L",None),
        (110,"Julieta",25166992,"Formosa 2346",12094736,"damian@hotmail.com","L",None)
]

micursor.executemany(sql,val)

miconexion.commit()

sql = "insert into peliculas(codigo_pelicula,nombre,genero,situacion,codigo) values (%s,%s,%s,%s,%s)"
val = [
        (101,"Arma mortal","accion","L",None),
        (102,"Lado dulce","romantica","L",None),
        (103,"durmiendo con el enemigo","drama","L",None),
        (104,"star wars","ciencia ficcion","L",None),
        (105,"star trek"," ciencia ficcion","L",None),
        (106,"Arma mortal 2","accion","L",None),
        (107,"ghost","romantica","L",None),
        (108,"durmiendo con el enemigo","drama","L",None),
        (109,"galactica","ciencia ficcion","L",None),
        (110,"espacio interior"," ciencia ficcion","L",None)
]

micursor.executemany(sql,val)

miconexion.commit()



