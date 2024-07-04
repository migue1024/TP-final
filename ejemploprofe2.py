import mysql.connector
import random
import tkinter
from tkinter import messagebox as mb

conexion = mysql.connector.connect(host="localhost", user="root", password="", database="tienda")
cursor = conexion.cursor()

ventana = tkinter.Tk()
entry_user = tkinter.Entry(ventana)
entry_passw = tkinter.Entry(ventana)
entry_nickname = tkinter.Entry(ventana)
entry_password = tkinter.Entry(ventana)
entry_telefono = tkinter.Entry(ventana)
entry_direccion = tkinter.Entry(ventana)

def refresh():
    for i in ventana.pack_slaves():
        i.destroy()

def modificarTelefono():
    pass

def modificarDireccion():
    pass

def menu(datos):
    refresh()
    frame_datos = tkinter.Frame(ventana)
    frame_datos.pack()
    label_codigo = tkinter.Label(frame_datos, text="Codigo:")
    label_codigo.pack()
    label_codigo_d = tkinter.Label(frame_datos, text=f"{datos[1]}")
    label_codigo_d.pack()
    label_nickname = tkinter.Label(frame_datos, text="Nickname:")
    label_nickname.pack()
    label_nickname_d = tkinter.Label(frame_datos, text=f"{datos[2]}")
    label_nickname_d.pack()
    label_password = tkinter.Label(frame_datos, text="Password:")
    label_password.pack()
    label_password_d = tkinter.Label(frame_datos, text=f"{datos[3]}")
    label_password_d.pack()
    label_telefono = tkinter.Label(frame_datos, text="Telefono:")
    label_telefono.pack()
    label_telefono_d = tkinter.Label(frame_datos, text=f"{datos[4]}")
    label_telefono_d.pack()
    boton_modif_telefono = tkinter.Button(frame_datos, text="Modificar", command=modificarTelefono)
    boton_modif_telefono.pack()
    label_direccion = tkinter.Label(frame_datos, text="Direccion:")
    label_direccion.pack()
    label_direccion_d = tkinter.Label(frame_datos, text=f"{datos[5]}")
    label_direccion_d.pack()
    boton_modif_direccion = tkinter.Button(frame_datos, text="Modificar", command=modificarDireccion)
    boton_modif_direccion.pack()
    label_situacion = tkinter.Label(frame_datos, text="Situacion:")
    label_situacion.pack()
    label_situacion_d = tkinter.Label(frame_datos, text=f"{datos[6]}")
    label_situacion_d.pack()
    label_codigo_peli = tkinter.Label(frame_datos, text="Pelicula Alquilada:")
    label_codigo_peli.pack()
    label_codigo_peli_d = tkinter.Label(frame_datos, text=f"{datos[7]}")
    label_codigo_peli_d.pack()

def insertar():
    codigo = "c"+str(random.randint(00,99))
    nickname = entry_nickname.get()
    password = entry_password.get()
    telefono = entry_telefono.get()
    direccion = entry_direccion.get()
    sql = "insert into users (codigo, nickname, pasword, telefono, direccion, situacion) values (%s, %s, %s, %s, %s, %s)"
    val = (codigo, nickname, password, telefono, direccion, "L")
    cursor.execute(sql,val)
    conexion.commit()
    login()

def ingresar():
    user = entry_user.get()
    passw = entry_passw.get()
    cursor.execute(f"select * from users where nickname = '{user}' and pasword = '{passw}'")
    result = cursor.fetchall()
    if len(result) > 0:
        menu(result[0])
    else:
        mb.showerror("error")

def inicio():
    refresh()
    boton_iniciarSesion = tkinter.Button(ventana, text="Iniciar sesion", command=login)
    boton_iniciarSesion.pack()
    boton_registrarse = tkinter.Button(ventana, text="Registrarse", command=register)
    boton_registrarse.pack()

def login():
    refresh()
    label_user = tkinter.Label(ventana, text="username")
    label_user.pack()
    entry_user.pack()
    label_passw= tkinter.Label(ventana, text="Password")
    label_passw.pack()
    entry_passw.pack()
    boton_ingresar = tkinter.Button(ventana, text="Ingresar", command=ingresar)
    boton_ingresar.pack()
    boton_cancelar = tkinter.Button(ventana, text="Cancelar", command=inicio)
    boton_cancelar.pack()

def register():
    label_nickname = tkinter.Label(ventana, text="Nickname")
    label_nickname.pack()
    entry_nickname.pack()
    label_password = tkinter.Label(ventana, text="Password")
    label_password.pack()
    entry_password.pack()
    label_telefono = tkinter.Label(ventana, text="Telefono")
    label_telefono.pack()
    entry_telefono.pack()
    label_direccion = tkinter.Label(ventana, text="Direccion")
    label_direccion.pack()
    entry_direccion.pack()
    boton_ingresar = tkinter.Button(ventana, text="Ingresar", command=insertar)
    boton_ingresar.pack()
    boton_cancelar = tkinter.Button(ventana, text="Cancelar", command=inicio)
    boton_cancelar.pack()

inicio()
ventana.mainloop()