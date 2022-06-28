from distutils.command.config import config
from tkinter import ttk 
from tkinter import *
import sqlite3
from turtle import width 
import tkinter as tk

class Programa(ttk.Frame):
    
    BD= "Grupos.db"

    def __init__(self,ventana):
        super().__init__(ventana)
        self.ven = ventana
        self.ven.title("Grupos electrógenos")
        self.ven["bg"] = "beige"

        frame = LabelFrame(self.ven, text = "Nuevo cliente",fg = "brown")
        frame.grid(row = 0, column = 0,columnspan = 3,pady = 20,padx = 20)

        #Ingreso del nombre
        Label(frame,text = "Nombre y apellido: ").grid(row = 1, column = 0)
        self.nombre = Entry(frame)
        self.nombre.focus()
        self.nombre.grid(row = 1, column = 1)

        #Ingreso de la dirección 
        Label(frame,text = "Dirección: ").grid(row = 2, column = 0)
        self.direccion = Entry(frame)
        self.direccion.grid(row = 2, column = 1,pady = 5)

        #Ingreso del celular 
        Label(frame, text = "Número de contacto: ").grid(row = 3, column = 0)
        self.celular = Entry(frame)
        self.celular.grid(row = 3, column = 1, pady = 5)

        #Ingreso del email 
        Label(frame, text = "Email: ").grid(row = 4, column = 0)
        self.email = Entry(frame)
        self.email.grid(row = 4, column = 1, pady = 5) 
        
        #Creando Boton
        boton = ttk.Button(frame,text = "Guardar").grid(row = 5,column = 0,columnspan=2,sticky = W + E)
        
        frame1 = LabelFrame(self.ven, text = "Listado Clientes",fg = "brown")
        frame1.grid(row = 0, column = 3,columnspan = 3,pady = 20,padx = 20)
        
        scrollbar = ttk.Scrollbar(frame1, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(frame1, yscrollcommand=scrollbar.set)
        self.listbox.grid(row = 0, column = 0, columnspan = 3,pady = 20,padx = 20)
        listaprueba = ("tkinter","sqlite3","pandas","matplotlib","pygame","datetime","librerias")
        self.listbox.insert(0, *listaprueba)

        













if __name__=='__main__':
    ventana = Tk()  
    programa = Programa(ventana)
    ventana.mainloop()


    """Button(self.EditarVentana, text = "Actualizar",command = lambda: self.EditarRegistros(NuevoNombre.get(),NuevaDireccion.get(),NuevoCelular.get(),NuevoEmail.get(),OLDNombre,OLDDireccion,OLDCelular,OLDEmail).grid(row = 4, column = 2, sticky = W)

    def EditarRegistros(self,NuevoNombre, NuevaDireccion,NuevoCelular,NuevoEmail,OLDNombre,OLDDireccion,OLDCelular,OLDEmail):
        consulta = """UPDATE Clientes SET NombreApellido = ?, Direccion = ?,Celular = ?,
         Email = ? WHERE NombreApellido = ? AND Direccion = ? AND Celular = ? AND Email = ?"""
        parametros = (NuevoNombre, NuevaDireccion,NuevoCelular,NuevoEmail,OLDNombre,OLDDireccion,OLDCelular,OLDEmail)
        self.ejecuta_consulta(consulta, parametros)
        self.EditarVentana.destroy()
        self.mensaje["text"] = f"Registro {NuevoN} ha sido actualizado"
        self.devuelve_consulta()
"""