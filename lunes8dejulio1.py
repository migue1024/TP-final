import tkinter
import tkinter.messagebox
import mysql.connector
import random

class App():
    def _init_(self):
        self.conexion = mysql.connector.connect(host="localhost", user="root", password="", database="tienda")
        self.cursor = self.conexion.cursor()
        self.ventana = tkinter.Tk()
        self.main()

    def refresh(self):
        for i in self.ventana.pack_slaves():
            i.destroy()
        for i in self.ventana.place_slaves():
            i.destroy()
        for i in self.ventana.grid_slaves():
            i.destroy()

    def main(self):
        self.refresh()
        self.boton_iniciarSesion = tkinter.Button(self.ventana, text="Iniciar Sesion", command=self.iniciarSesion)
        self.boton_iniciarSesion.pack()
        self.boton_registrarse = tkinter.Button(self.ventana, text="Registrarse", command=self.register)
        self.boton_registrarse.pack()

    def iniciarSesion(self):
        self.refresh()
        self.label_user = tkinter.Label(self.ventana, text="User")
        self.label_user.grid(row=0, column=0)
        self.entry_user = tkinter.Entry(self.ventana)
        self.entry_user.grid(row=0, column=1)
        self.label_password = tkinter.Label(self.ventana, text="Password")
        self.label_password.grid(row=1, column=0)
        self.entry_password = tkinter.Entry(self.ventana)
        self.entry_password.grid(row=1, column=1)
        self.boton_cancelar = tkinter.Button(self.ventana, text="Cancel", command=self.main)
        self.boton_cancelar.grid(row=2, column=0)
        self.boton_entrar = tkinter.Button(self.ventana, text="Entrar", command=self.entrar)
        self.boton_entrar.grid(row=2, column=1)

    def entrar(self):
        self.cursor.execute(f"select * from users where nickname = '{self.entry_user.get()}' and pasword = '{self.entry_password.get()}'")
        self.datos = self.cursor.fetchall()
        if len(self.datos) > 0:
            self.menu()
        else:
            tkinter.messagebox.showerror("Error", "Usuario y/o Password incorrecto/s")
    
    def menu(self):
        self.refresh()
        self.frame_datos = tkinter.Frame(self.ventana)
        self.frame_datos.grid(row=0, column=0)
        self.datos_codigo = tkinter.Label(self.frame_datos, text=f"Codigo: {self.datos[0][1]}").pack()
        self.datos_nickname = tkinter.Label(self.frame_datos, text=f"Nickname: {self.datos[0][2]}").pack()
        self.datos_telefono = tkinter.Label(self.frame_datos, text=f"Telefono: {self.datos[0][4]}")
        self.datos_telefono.pack()
        self.boton_modificar_tel = tkinter.Button(self.frame_datos, text="Modificar", command=self.modificar_tel).pack()
        self.datos_direccion = tkinter.Label(self.frame_datos, text=f"Direccion: {self.datos[0][5]}")
        self.datos_direccion.pack()
        self.boton_modificar_dir = tkinter.Button(self.frame_datos, text="Modificar", command=self.modificar_dir).pack()
        self.datos_situacion = tkinter.Label(self.frame_datos, text=f"Situacion: {self.datos[0][6]}").pack()
        self.boton_ver_peli = tkinter.Button(self.frame_datos, text="¿Que peli alquile?", command=self.verPeli).pack()

        self.frame_acciones = tkinter.Frame(self.ventana)
        self.frame_acciones.grid(row=0, column=1)
        self.boton_vertodas = tkinter.Button(self.frame_acciones, text="Ver Todas").grid(row=0, column=0)
        self.boton_verdispo = tkinter.Button(self.frame_acciones, text="Ver Dispo").grid(row=0, column=1)
        self.boton_alquilar = tkinter.Button(self.frame_acciones, text="Alquilar").grid(row=0, column=2)
        self.boton_devolver = tkinter.Button(self.frame_acciones, text="Devolver").grid(row=0, column=3)
        self.lista_pelis = tkinter.Listbox(self.frame_acciones, width=40).grid(row=1, column=0, columnspan=4)

    def verPeli(self):
        self.ventana_emergente_peli = tkinter.Tk()
        self.label_pelicula_alquilada = tkinter.Label(self.ventana_emergente_peli)
        if self.datos[0][6] == "L":
            self.label_pelicula_alquilada.config(text="No tenes nada alquilado capo")
        else:
            self.cursor.execute(f"select nombre from pelis where codigo = '{self.datos[0][7]}'")
            self.label_pelicula_alquilada.config(text=f"Alquilaste: {self.cursor.fetchall()[0][0]}")
        self.label_pelicula_alquilada.pack()
        self.boton_ok_verpeli = tkinter.Button(self.ventana_emergente_peli, text="Ok", command=self.ventana_emergente_peli.destroy).pack()

    def modificar_tel(self):
        self.ventana_emergente_tel = tkinter.Tk()
        self.input_newtel = tkinter.Entry(self.ventana_emergente_tel)
        self.input_newtel.pack()
        self.boton_ok_tel = tkinter.Button(self.ventana_emergente_tel, text="Ok", command=self.update_tel).pack()

    def update_tel(self):
        self.cursor.execute(f"update users set telefono = '{self.input_newtel.get()}' where nickname = '{self.datos[0][2]}'")
        self.conexion.commit()
        self.datos_telefono.config(text=f"Telefono: {self.input_newtel.get()}")
        self.ventana_emergente_tel.destroy()

    def modificar_dir(self):
        self.ventana_emergente_dir = tkinter.Tk()
        self.input_newdir = tkinter.Entry(self.ventana_emergente_dir)
        self.input_newdir.pack()
        self.boton_ok_dir = tkinter.Button(self.ventana_emergente_dir, text="Ok", command=self.update_dir).pack()

    def update_dir(self):
        self.cursor.execute(f"update users set direccion = '{self.input_newdir.get()}' where nickname = '{self.datos[0][2]}'")
        self.conexion.commit()
        self.datos_direccion.config(text=f"Direccion: {self.input_newdir.get()}")
        self.ventana_emergente_dir.destroy()

    def register(self):
        self.refresh()
        self.label_nickname = tkinter.Label(self.ventana, text="Nickname")
        self.label_nickname.grid(row=0, column=0)
        self.entry_nickname = tkinter.Entry(self.ventana)
        self.entry_nickname.grid(row=0, column=1)
        self.label_pass = tkinter.Label(self.ventana, text="Password")
        self.label_pass.grid(row=1, column=0)
        self.entry_pass = tkinter.Entry(self.ventana)
        self.entry_pass.grid(row=1, column=1)
        self.label_telefono = tkinter.Label(self.ventana, text="Telefono")
        self.label_telefono.grid(row=2, column=0)
        self.entry_telefono = tkinter.Entry(self.ventana)
        self.entry_telefono.grid(row=2, column=1)
        self.label_direccion = tkinter.Label(self.ventana, text="Direccion")
        self.label_direccion.grid(row=3, column=0)
        self.entry_direccion = tkinter.Entry(self.ventana)
        self.entry_direccion.grid(row=3, column=1)
        self.boton_cancelar2 = tkinter.Button(self.ventana, text="Cancel", command=self.main)
        self.boton_cancelar2.grid(row=4, column=0)
        self.boton_registrar = tkinter.Button(self.ventana, text="Ok", command=self.insert)
        self.boton_registrar.grid(row=4, column=1)

    def insert(self):
        self.cursor.execute(f"select * from users where nickname = '{self.entry_nickname.get()}'")
        result = self.cursor.fetchall()
        if len(result) > 0:
            tkinter.messagebox.showerror("Error", "El usuario ya existe !")
        else:
            sql = "insert into users (codigo, nickname, pasword, telefono, direccion, situacion) values (%s,%s,%s,%s,%s,%s)"
            val = ("c"+str(random.randint(0,9))+str(random.randint(0,9)), self.entry_nickname.get(), self.entry_pass.get(), self.entry_telefono.get(), self.entry_direccion.get(), "L")
            self.cursor.execute(sql, val)
            self.conexion.commit()
            self.iniciarSesion()

app = App()
app.ventana.mainloop()