import tkinter
from tkinter import messagebox as mb

ventana = tkinter.Tk()
entry1 = tkinter.Entry(ventana)
entry2 = tkinter.Entry(ventana)

def refresh():
    for i in ventana.pack_slaves():
        i.destroy()

def menu():
    refresh()
    label = tkinter.Label(ventana, text="JEJE")
    label.pack()

def ingresar():
    user = entry1.get()
    passw = entry2.get()
    if user == passw:
        print("ok")
        menu()

    else:
        print("no")
        mb.showerror("error")

def login():
    label1 = tkinter.Label(ventana, text="username")
    label1.pack()
    entry1 = tkinter.Entry(ventana)
    entry1.pack()
    label2= tkinter.Label(ventana, text="Password")
    label2.pack()
    entry2 = tkinter.Entry(ventana)
    entry2.pack()

def inicio():
    boton1 = tkinter.Button(ventana, text="Iniciar sesion", command=login)
    boton1.pack()
    boton2 = tkinter.Button(ventana, text="Registrarse", command=register)
    boton2.pack()

def login():
    refresh()
    label1 = tkinter.Label(ventana, text="username")
    label1.pack()
    
    entry1.pack()
    label2= tkinter.Label(ventana, text="Password")
    label2.pack()
    
    entry2.pack()
    boton1 = tkinter.Button(ventana, text="Ingresar", command=ingresar)
    boton1.pack()

def register():
    pass

inicio()
ventana.mainloop()