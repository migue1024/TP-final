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

def devolver():
    cursor.execute(f"select situacion, codigo_pelicula from users where nickname = '{user}'")
    result = cursor.fetchall()
    situacion = result[0][0]
    codigo_peli = result[0][1]
    if situacion == "L":
        mb.showerror("No tenes nada alquilado")
    else:
        cursor.execute(f"update users set situacion = 'L', codigo_pelicula = null where nickname = '{user}'")
        cursor.execute(f"update pelis set situacion = 'L', codigo_user = null where codigo = '{codigo_peli}'")
        conexion.commit()
        label_situacion_d.config(text="L")
        label_codigo_peli_d.config(text="None")
        verDispo()

def alquilar():
    seleccinado = lista_pelis.curselection()
    if seleccinado:
        cursor.execute(f"select situacion from users where nickname = '{user}'")
        result = cursor.fetchall()
        if result[0][0] == "L":
            tupla_peli = lista_pelis.get(seleccinado)
            cursor.execute(f"select codigo from users where nickname = '{user}'")
            result = cursor.fetchall()
            #print(tupla_peli[0], type(tupla_peli[0]))
            cursor.execute(f"update pelis set situacion = 'A', codigo_user = '{result[0][0]}' where codigo = '{tupla_peli[0]}'")
            cursor.execute(f"update users set situacion = 'A', codigo_pelicula = '{tupla_peli[0]}' where nickname = '{user}'")
            conexion.commit()
            label_situacion_d.config(text="A")
            label_codigo_peli_d.config(text=f"{tupla_peli[0]}")
            verDispo()
        else:
            mb.showerror("No podes alquilar")
    else:
        mb.showerror("Elejí una capo")

def verDispo():
    lista_pelis.delete(0, tkinter.END)
    boton_alquilar.config(state="normal")
    cursor.execute("select codigo, nombre, genero from pelis where situacion = 'L'")
    result = cursor.fetchall()
    for i in result:
        lista_pelis.insert(tkinter.END, i)

def verTodas():
    lista_pelis.delete(0, tkinter.END)
    boton_alquilar.config(state="disabled")
    cursor.execute("select codigo, nombre, genero from pelis")
    result = cursor.fetchall()
    for i in result:
        lista_pelis.insert(tkinter.END, i)

def update_tel():
    new_dato = entry_newdato.get()
    cursor.execute(f"update users set telefono = {new_dato} where nickname = '{user}'")
    conexion.commit()
    cursor.execute(f"select telefono from users where nickname = '{user}'")
    result = cursor.fetchall()
    label_telefono_d.config(text=f"{result[0][0]}")
    ventana_emergente.destroy()
    
def modificarTelefono():
    global ventana_emergente
    ventana_emergente = tkinter.Tk()
    global entry_newdato
    entry_newdato = tkinter.Entry(ventana_emergente)
    entry_newdato.pack()
    boton_ok = tkinter.Button(ventana_emergente, text="Ok", command=update_tel)
    boton_ok.pack()

def modificarDireccion():
    pass

def menu(datos):
    refresh()
    frame_datos = tkinter.Frame(ventana)
    frame_datos.grid(row=0, column=0)
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
    global label_telefono_d
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
    global label_situacion_d
    label_situacion_d = tkinter.Label(frame_datos, text=f"{datos[6]}")
    label_situacion_d.pack()
    label_codigo_peli = tkinter.Label(frame_datos, text="Pelicula Alquilada:")
    label_codigo_peli.pack()
    global label_codigo_peli_d
    label_codigo_peli_d = tkinter.Label(frame_datos, text=f"{datos[7]}")
    label_codigo_peli_d.pack()

    frame_acciones = tkinter.Frame(ventana)
    frame_acciones.grid(row=0, column=1)
    boton_verTodas = tkinter.Button(frame_acciones, text="Ver Todas", command=verTodas)
    boton_verTodas.grid(row=0, column=0)
    boton_verDispo = tkinter.Button(frame_acciones, text="Ver Disponibles", command=verDispo)
    boton_verDispo.grid(row=0, column=1)
    global boton_alquilar
    boton_alquilar = tkinter.Button(frame_acciones, text="Alquilar", state="disabled", command=alquilar)
    boton_alquilar.grid(row=0, column=2)
    boton_devolver = tkinter.Button(frame_acciones, text="Devolver", command=devolver)
    boton_devolver.grid(row=0, column=3)

    global lista_pelis
    lista_pelis = tkinter.Listbox(frame_acciones, width=40)
    lista_pelis.grid(row=1, column=0, columnspan=4)


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
    global user
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
    label_passw= tkinter.Label(ventana, text="password")
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