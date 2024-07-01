
from conexion import miconexion,micursor

import tkinter as tk
#import tkinter

from tkinter import messagebox as mb

ventana = tk.Tk()
ventana.geometry("600x500+600+200")
frame=tk.Frame(ventana)
frame.pack()
entrada1 = tk.Entry(width=30)
entrada2 = tk.Entry(width=30)

def inicio():
    boton1 = tk.Button(frame,text="Iniciar sesion",command=login)#asocio los botones al frame
    boton1.pack()

    boton2 = tk.Button(frame,text="Registrarse",command=registro)
    boton2.pack()

def menuInicio():
    encabezado=tk.Label(ventana,text="Bienvenido al Video club",bg="blue",fg="white")
    encabezado.pack()


def match():
    usuario=entrada1.get()
    contraseña=entrada2.get()
    micursor.execute(f"select*from usuarios where nombre='{usuario}' and dni='{contraseña}'")
    resultado=micursor.fetchall()
    if len(resultado)>0:
        cartel=tk.Label(ventana,text="Ingreso correcto")
        cartel.pack()
        #menuInicio()
        #print(resultado[0])
    else:
        mb.showerror("Acceso denegado")
        '''cartel=tk.Label(ventana,text="Acceso denegado")
        cartel.pack()'''

    entrada=tk.Label(ventana,text="")
    entrada.place()






def login():
    frame.destroy()#borra el frame(marco) de la ventana,botones de iniciar sesion y registrartse
    
    entrada1.place(x=200,y=100)

    
    entrada2.place(x=200,y=200)

    usuario=tk.Label(ventana,text="Usuario:")
    usuario.place(x=100,y=100)

    contrasena=tk.Label(ventana,text="Contraseña:")
    contrasena.place(x=100,y=200)

    boton_ingreso=tk.Button(ventana,text="ingresar",command=match)
    boton_ingreso.place(x=275,y=300)


def registro():
    frame.destroy()
    codigo_usuario=tk.Label(ventana,text="Ingrese su codigo")
    codigo_usuario.place(x=100,y=100)
    entrada1=tk.Entry(width=30)
    entrada1.place(x=300,y=100)

    nombre=tk.Label(ventana,text="Ingrese su nombre:")
    nombre.place(x=100,y=150)
    entrada2=tk.Entry(width=30)
    entrada2.place(x=300,y=150)
    
    dni=tk.Label(ventana,text="Ingrese su dni:")
    dni.place(x=100,y=200)
    entrada3=tk.Entry(width=30)
    entrada3.place(x=300,y=200)

    direccion=tk.Label(ventana,text="Ingrese su direccion:")
    direccion.place(x=100,y=250)
    entrada4=tk.Entry(width=30)
    entrada4.place(x=300,y=250)

    telefono=tk.Label(ventana,text="Ingrese su telefono:")
    telefono.place(x=100,y=300)
    entrada5=tk.Entry(width=30)
    entrada5.place(x=300,y=300)

    email=tk.Label(ventana,text="Ingrese su email:")
    email.place(x=100,y=350)
    entrada6=tk.Entry(width=30)
    entrada6.place(x=300,y=350)







inicio()





ventana.mainloop()

