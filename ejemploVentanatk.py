import tkinter as tk# si da error hacer pip install tkinter

def match():
    ventana3 = tk.Tk()
    username=entrada.get()
    password=entrada2.get()
    if username == password:
        Acceso_P = tk.Label(ventana3,text = "Sesion Iniciada")
        Acceso_P.pack()
        #print("Ok")
        #ventanita = tk.Tk()
        #ventanita.geometry("500x50+50+50")
        #ventanita = tk.Label(ventanita,text = "Sesion iniciada")
        #ventanita.pack()
        
    else:
        Acceso_D = tk.Label(ventana3,text = "Acceso denegado")
        Acceso_D.pack()
        #print("Nope")
        #ventanita2 = tk.Tk()
        #ventanita2.geometry("500x50+50+50")
        #ventanita2 = tk.Label(ventanita2,text = "Acceso denegado")
        #ventanita2.pack()
        

ventana = tk.Tk()#Tk() convierte la variable en un objeto
ventana.title("Mi app") #cambia el titulo Tk por defecto en la ventana
ventana.geometry("800x600+600+250") #valores en la multiplicacion ancho y alto,valores en la suma coordenadas en la pantalla,x e y

etiqueta1 = tk.Label(ventana,text = "LOGIN",bg = "Yellow",fg = "red",font = ("Sans Serif",28)) #bg=background fg=color de la letra font=fuente
etiqueta1.pack()#place(x=300,y=70)

etiqueta2 = tk.Label(ventana,text = "Bienvenido a mi primer app")
etiqueta2.place(x=325,y=125)

entrada = tk.Entry(width=40)
entrada.place(x=300,y=200)#pack()

entrada2 = tk.Entry(width=40)
entrada2.place(x=300,y=300)#pack()

username = tk.Label(ventana,text = "Username:" )
username.place(x=70,y=200)

password = tk.Label(ventana,text = "Password:")
password.place(x=70,y=300)

boton = tk.Button(ventana,text="Ingresar",command=match)
boton.place(x=400,y=400)




ventana.mainloop()
