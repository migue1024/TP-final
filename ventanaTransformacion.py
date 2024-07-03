
from conexion import miconexion,micursor

import tkinter as tk
#import tkinter

from tkinter import messagebox as mb

ventana = tk.Tk()
ventana.geometry("600x500+600+200")
#frame=tk.Frame(ventana)
#frame.pack()
entrada1 = tk.Entry(width=30) #login
entrada2 = tk.Entry(width=30) #login
entrada_codigo=tk.Entry(width=30)
entrada_ingreso_nombre=tk.Entry(width=30)
entrada_ingreso_dni=tk.Entry(width=30)
entrada_ingreso_direccion=tk.Entry(width=30)
entrada_ingreso_telefono=tk.Entry(width=30)
entrada_ingreso_email=tk.Entry(width=30)

def inicio():
    refresh()
    boton1 = tk.Button(ventana,text="Iniciar sesion",command=login)#asocio los botones al frame
    boton1.pack()

    boton2 = tk.Button(ventana,text="Registrarse",command=registro)
    boton2.pack()

def menuInicio(resultado):
    refresh()
    encabezado=tk.Label(ventana,text="Bienvenido al Video club",bg="blue",fg="white")
    encabezado.pack()
    marco_datos=tk.Frame()
    marco_datos.pack()

    etiqueta_nombre_logueado=tk.Label(marco_datos,text="nombre")
    etiqueta_nombre_logueado.pack()

    nombre_usuario=tk.Label(marco_datos,texto=(f'{resultado[1]}'))
    nombre_usuario.pack()

    etiqueta_telefono_logueado=tk.Label(marco_datos,text="telefono")
    etiqueta_telefono_logueado.pack()
    
    etiqueta_telefono_usuario=tk.Label(marco_datos,text=(f'{resultado[2]}'))
    etiqueta_telefono_usuario.pack()

    telefono_usuario=tk.Label(marco_datos,text=(f'{resultado[3]}'))
    telefono_usuario.pack()

    boton_modificar_telefono=tk.Button(marco_datos,text="Modifiocar telefono")
    boton_modificar_telefono.pack()

    '''boton_modificar_domicilio=tk.Button(marco_datos;text="Modificar domicilio")
    boton_modificar_domicilio.pack()'''


def match():
    usuario=entrada1.get()
    contraseña=entrada2.get()
    micursor.execute(f"select*from usuarios where nombre='{usuario}' and dni='{contraseña}'")
    resultado=micursor.fetchall()
    if len(resultado)>0:
        print("Ok")

        #cartel=tk.Label(ventana,text="Ingreso correcto")
        #cartel.pack()
        #menuInicio()
        #print(resultado[0])
    else:
        mb.showerror("Usuario o Contraseña incorrecta")

        '''cartel=tk.Label(ventana,text="Acceso denegado")
        cartel.pack()'''

    entrada=tk.Label(ventana,text="")
    entrada.place()

def refresh(): #elimina los datos de la ventana
    for i in ventana.pack_slaves():
        i.destroy()

    for i in ventana.place_slaves():
        i.destroy()

def insertar(): #Inserta los datos en la base de datos
    codigo=entrada_codigo.get()
    nombre=entrada_ingreso_nombre.get()
    dni=entrada_ingreso_dni.get()
    direccion=entrada_ingreso_direccion.get()
    telefono=entrada_ingreso_telefono.get()
    email=entrada_ingreso_email.get()

    sql="insert into usuarios(codigo_usuario,nombre,dni,domicilio,telefono,email) values(%s,%s,%s,%s,%s,%s)"
    val=(codigo,nombre,dni,direccion,telefono,email)
    micursor.execute(sql,val)
    miconexion.commit()
    


def login():
    refresh()
    #frame.destroy()#borra el frame(marco) de la ventana,botones de iniciar sesion y registrartse
    
    entrada1.place(x=200,y=100)

    
    entrada2.place(x=200,y=200)

    usuario=tk.Label(ventana,text="Usuario:")
    usuario.place(x=100,y=100)

    contrasena=tk.Label(ventana,text="Contraseña:")
    contrasena.place(x=100,y=200)

    boton_ingreso=tk.Button(ventana,text="ingresar",command=match)
    boton_ingreso.place(x=275,y=300)

    boton_cancelar=tk.Button(ventana,text="Cancelar",command=inicio)
    boton_cancelar.place(x=275,y=350)


def registro():
    #frame.destroy()
    refresh()
    codigo_usuario=tk.Label(ventana,text="Ingrese su codigo:")
    codigo_usuario.place(x=100,y=100)
    
    entrada_codigo.place(x=300,y=100)
    

    nombre=tk.Label(ventana,text="Ingrese su nombre:")
    entrada_ingreso_nombre.place(x=300,y=150)

    nombre.place(x=100,y=150)
    
    dni=tk.Label(ventana,text="Ingrese su dni:")
    dni.place(x=100,y=200)
    
    entrada_ingreso_dni.place(x=300,y=200)

    direccion=tk.Label(ventana,text="Ingrese su direccion:")
    direccion.place(x=100,y=250)
    
    entrada_ingreso_direccion.place(x=300,y=250)

    telefono=tk.Label(ventana,text="Ingrese su telefono:")
    telefono.place(x=100,y=300)
    
    entrada_ingreso_telefono.place(x=300,y=300)

    email=tk.Label(ventana,text="Ingrese su email:")
    email.place(x=100,y=350)
    
    entrada_ingreso_email.place(x=300,y=350)

    boton_ok=tk.Button(ventana,text="Ok",command=insertar)
    boton_ok.place(x=350,y=400)

    boton_cancelar=tk.Button(ventana,text="Cancelar",command=inicio)
    boton_cancelar.place(x=335,y=450)



inicio()

ventana.mainloop()

