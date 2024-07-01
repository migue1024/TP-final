import tkinter as tk
from conexion import miconexion,micursor

def login():
    ventanalogin = tk.Tk()
    encabezadoLogin = tk.Label(ventanalogin,text="LOGIN",bg="red",fg = "white", font=("Arial",29))
    encabezadoLogin.pack()

    ingreso1 = tk.Label(ingreso1)


def log_in():
    ventana_emergente=tk.Tk()
    ventana_emergente.geometry("300x200+450+150")
    username=entry_username.get()
    password=entry_password.get()
    micursor.execute(f"select * from usuarios where nombre='{username}' and dni='{password}'")
    resultado=micursor.fetchall()
    if len(resultado)>0:
        #if username == password:
        cartel=tk.Label(ventana_emergente,text="Ingreso correcto")
        cartel.pack()
        print(resultado[0])
    else:
        cartel=tk.Label(ventana_emergente,text="Acceso denegado")
        cartel.pack()

def inicioDeSesion():
    ventana_iniciar_sesion = tk.Tk()
    ventana_iniciar_sesion.geometry("700x500+600+250")
    encabezado_inicio_de_sesion=tk.Label(ventana_iniciar_sesion,text="LOGIN",bg="blue",fg="white",font=("Arial",29))
    encabezado_inicio_de_sesion.pack()

    etiqueta_username=tk.Label(ventana_iniciar_sesion,text="Username")
    etiqueta_username.place(x=100, y=100)

    etiqueta_password=tk.Label(ventana_iniciar_sesion,text="Password")
    etiqueta_password.place(x=100, y=200)

    global entry_username
    entry_username=tk.Entry(ventana_iniciar_sesion)
    entry_username.place(x=200,y=100)

    global entry_password
    entry_password=tk.Entry(ventana_iniciar_sesion)
    entry_password.place(x=200,y=200)

    boton_ingresar=tk.Button(ventana_iniciar_sesion,text="Ingresar",command=log_in)
    boton_ingresar.place(x=300,y=300)





    '''entry_username=tk.Entry(ventana_iniciar_sesion)
    entry_username(x=200, y=100)
    entry_password=tk.Entry(ventana_iniciar_sesion)
    entry_password(x=200 ,y=200)'''

'''def match():
    ventanaingreso3 = tk.Tk()
    username=ventanaingreso.get()
    password=ventanaingreso2.get()
    
    if username==password:
        acceso_permitido=tk.Label(ventanaingreso3,text="Sesion iniciada")
        acceso_permitido.pack()
    else:
        acceso_denegado=tk.Label(ventanaingreso3,text="Acceso denegado")'''



ventana = tk.Tk()
ventana.title("Mi app")
ventana.geometry("800x600+600+250")

etiqueta_login= tk.Label(ventana,text = "Bienvenido a la aplicacion", bg = "green" ,fg = "white",font = ("Arial 1",30))
etiqueta_login.pack()

boton_inicio_de_sesion = tk.Button(ventana,text = "Iniciar sesion",command=inicioDeSesion)
boton_inicio_de_sesion.place(x=350,y=150)

boton_registrarse = tk.Button(ventana,text = "Registrarse")
boton_registrarse.place(x=355,y=250)

'''ventanaingreso = tk.Entry(width=40)
ventanaingreso.place(x=290,y=270)

ventanaingreso2 = tk.Entry(width=40)
ventanaingreso2.place(x=290,y=350)

username = tk.Label(ventana,text="Username:")
username.place(X=90,y=270)

password = tk.Label(ventana,text="Password:")
password.place(x=70,y=350)

boton = tk.Button(ventana,text="Ingresar",command=match)
boton.place(x=365,y=425)'''



ventana.mainloop()