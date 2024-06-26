import tkinter as tk

def login():
    ventanalogin = tk.Tk()
    encabezadoLogin = tk.Label(ventanalogin,text="LOGIN",bg="red",fg = "white", font=("Arial",29))
    encabezadoLogin.pack()

    ingreso1 = tk.Label(ingreso1)








ventana = tk.Tk()
ventana.title("Mi app")
ventana.geometry("800x600+600+250")

etiqueta_login= tk.Label(ventana,text = "Bienvenido a la aplicacion", bg = "green" ,fg = "white",font = ("Arial 1",30))
etiqueta_login.pack()

boton = tk.Button(ventana,text = "Iniciar sesion",command=login)
#boton.pack()
boton.place(x=350,y=100)

boton2 = tk.Button(ventana,text = "Registrarse",command=login)
boton2.place(x=350,y=200)

ventana_ingreso = tk






ventana.mainloop()