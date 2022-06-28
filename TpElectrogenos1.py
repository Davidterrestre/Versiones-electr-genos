import tkinter as tk
from tkinter import messagebox as msg
from tkinter.ttk import Notebook
from tkinter import ttk 
from tkinter import *
import sqlite3

class Electrogenos(tk.Tk):
    
    BaseDatos = "TrabajoP.DB" 
    
    def __init__(self):
        super().__init__()

        self.title("Grupos Electrógenos")
        self.geometry("1050x500")
        
        self.notebook = Notebook(self)

        #Creamos la cantidad de ventanas que querramos tener

        cliente = tk.Frame(self.notebook)
        equipo = tk.Frame(self.notebook)
        servicio = tk.Frame(self.notebook)

        #Creando Frame en la ventana de clientes:
        frame = LabelFrame(cliente, text = "-CLIENTE",font=("Courier", 16, "italic"),bg = "#48A" )
        frame.grid(row = 0, column = 0,columnspan = 2 ,pady = 20,padx = 20)

        #-----------------CLIENTES-------------------
        #Ingreso del nombre
        Label(frame,text = "Nombre y apellido: ", font = ("Courier", 14), bg = "#48A" ).grid(row = 1, column = 0)
        self.nombre = Entry(frame)
        self.nombre.focus()
        self.nombre.grid(row = 1, column = 1,ipadx = 150)

        #Ingreso de la dirección 
        Label(frame,text = "Dirección: ",font = ("Courier", 14),bg = "#48A" ).grid(row = 2, column = 0)
        self.direccion = Entry(frame)
        self.direccion.grid(row = 2, column = 1,pady = 5,ipadx = 150)

        #Ingreso del celular 
        Label(frame, text = "Número de contacto: ",font = ("Courier", 14),bg = "#48A" ).grid(row = 3, column = 0)
        self.celular = Entry(frame)
        self.celular.grid(row = 3, column = 1, pady = 5,ipadx = 150)

        #Ingreso del email 
        Label(frame, text = "Email: ",font = ("Courier", 14),bg = "#48A" ).grid(row = 4, column = 0)
        self.email = Entry(frame)
        self.email.grid(row = 4, column = 1, pady = 5,ipadx = 150) 
        
        #Creando Boton
        boton = tk.Button(frame, text = "guardar", font =("Courier",10),bg = "#48A",fg = "#40A",command = self.Agregar_Cliente).grid(row = 5,column = 1, ipadx = 100)
        
        #Creando el mesanje
        self.mensaje = Label(frame,text = "",bg ='#48A',font = ("Courier", 10), fg = "red")
        self.mensaje.grid(row = 6, column = 0,columnspan = 2, sticky = W + E )
        
        #Creando Tabla 
        self.tabla = ttk.Treeview(frame,height=10, columns=[f"#{n}" for n in range(1, 6)],show='headings')
        self.tabla.grid(row = 7, column = 0, columnspan = 2)
        self.tabla.heading("#0",text = "")
        self.tabla.heading("#1", text = "ID Cliente", anchor = CENTER)
        self.tabla.heading("#2", text = "NombreApellido", anchor = CENTER)
        self.tabla.heading("#3", text = "Dirección", anchor = CENTER)
        self.tabla.heading("#4", text = "Celular", anchor = CENTER)
        self.tabla.heading("#5", text = "Email", anchor = CENTER)
       
        tk.Button(frame, text = "Eliminar", font =("Courier",10),bg = "#48A",fg = "red",command = lambda:self.Eliminar_Cliente()).grid(row = 8, column= 0, ipadx=100)
        tk.Button(frame,text = "Editar", font =("Courier",10),bg = "#48A",fg = "#40A",command = lambda:self.Editar_Cliente()).grid(row = 8, column=1, ipadx=100)
       
        #----------------Frame de Equipo----------------#

        frame1 = LabelFrame(equipo,text = "-GRUPO ELECTRÓGENO",font = ("Courier",16,"italic"),bg ='#48A')
        frame1.grid(row = 0, column = 0,pady = 20,padx = 20)
        
        #Ingreso del ID del cliente
        Label(frame1, text = "ID Cliente: ", font = ("Courier",14),bg = "#48A").grid(row = 0, column = 0)
        self.ID_Cliente = Entry(frame1)
        self.ID_Cliente.grid(row = 0 , column = 1, pady = 5,ipadx = 150)

        #Ingreso Marca
        Label(frame1, text = "Marca: ", font = ("Courier",14),bg = "#48A").grid(row = 1, column = 0)
        self.marca = Entry(frame1)
        self.marca.grid(row = 1 , column = 1, pady = 5,ipadx = 150)

        #Ingreso Modelo
        Label(frame1, text = "Modelo: ", font = ("Courier",14),bg = "#48A").grid(row = 2, column = 0)
        self.modelo = Entry(frame1)
        self.modelo.grid(row = 2 , column = 1, pady = 5,ipadx = 150)
        
        #Ingreso Potencia 
        Label(frame1, text = "Potencia: ", font = ("Courier",14),bg = "#48A").grid(row = 3, column = 0)
        self.potencia = Entry(frame1)
        self.potencia.grid(row = 3 , column = 1, pady = 5,ipadx = 150)
        
        boton1 = tk.Button(frame1, text = "guardar", font =("Courier",10),bg = "#48A",fg = "#40A",command = self.Agregar_Equipo).grid(row = 4,column = 1, ipadx = 100)
        
        self.mensaje1 = Label(frame1,text = "",bg ='#48A',font = ("Courier", 10), fg = "red")
        self.mensaje1.grid(row = 5, column = 0, columnspan = 2, sticky = W + E)
        
        self.tabla1 = ttk.Treeview(frame1,height=10, columns=[f"#{n}" for n in range(1, 6)],show='headings')
        self.tabla1.grid(row = 6, column = 0, columnspan =2)
        self.tabla1.heading("#0",text = "")
        self.tabla1.heading("#1", text = "ID Cliente", anchor = CENTER)
        self.tabla1.heading("#2", text = "ID Equipo", anchor = CENTER)
        self.tabla1.heading("#3", text = "Marca", anchor = CENTER)
        self.tabla1.heading("#4", text = "Modelo", anchor = CENTER)
        self.tabla1.heading("#5", text = "Potencia", anchor = CENTER)
        
        tk.Button(frame1,text = "Eliminar", font =("Courier",10),bg = "#48A",fg = "red",command=lambda:self.Eliminar_Equipo()).grid(row = 7, column= 0, ipadx=100)
        tk.Button(frame1,text = "Editar", font =("Courier",10),bg = "#48A",fg = "#40A",command=lambda:self.Editar_Equipo()).grid(row = 7, column=1, ipadx=100)

        #----------------Frame de Servicios----------------#
        frame2 = LabelFrame(servicio,text = "-SERVICIOS",font = ("Courier",16,"italic"),bg ='#48A')
        frame2.grid(row = 0, column = 0,pady = 20,padx = 20)
        
        #Ingreso Equipo ID
        Label(frame2, text = "ID Equipo: ", font = ("Courier",14),bg = "#48A").grid(row = 0, column = 0)
        self.ID_Equipo= Entry(frame2)
        self.ID_Equipo.grid(row = 0 , column = 1, pady = 5)

        #Ingreso Servicio
        Label(frame2, text = "Servicio: ", font = ("Courier",14),bg = "#48A").grid(row = 1, column = 0)
        self.servicio = Entry(frame2)
        self.servicio.grid(row = 1 , column = 1, pady = 5)

        #Ingreso Fecha
        Label(frame2, text = "Fecha: ", font = ("Courier",14),bg = "#48A").grid(row = 2, column = 0)
        self.fecha = Entry(frame2)
        self.fecha.grid(row = 2 , column = 1, pady = 5)
        
        boton2 = tk.Button(frame2, text = "guardar", font =("Courier",10), bg = "#48A", fg = "#40A", command = self.Agregar_Servicios).grid(row = 3,column = 1, ipadx = 50)
        
        self.mensaje2 = Label(frame2, text = "",bg ='#48A',font = ("Courier", 10), fg = "red")
        self.mensaje2.grid(row = 4, column = 0, columnspan = 2, sticky = W + E)

        self.tabla2 = ttk.Treeview(frame2,height=5, columns=[f"#{n}" for n in range(1, 4)],show='headings')
        self.tabla2.grid(row = 5, column = 0, columnspan =2)
        self.tabla2.heading("#0",text = "")
        self.tabla2.heading("#1", text = "ID Equipo", anchor = CENTER)
        self.tabla2.heading("#2", text = "Servicio", anchor = CENTER)
        self.tabla2.heading("#3", text = "Fecha", anchor = CENTER)

        tk.Button(frame2,text = "Eliminar", font =("Courier",10),bg = "#48A",fg = "red", command=lambda:self.Eliminar_Servicio()).grid(row = 6, column= 0, ipadx=100)
        tk.Button(frame2,text = "Editar", font =("Courier",10),bg = "#48A",fg = "#40A", command=lambda:self.Editar_Servicio()).grid(row = 6, column=1, ipadx=100)

        #---------------------------.-----------------------------#
        self.notebook.add(cliente, text="Clientes")
        self.notebook.add(equipo, text="Equipos")
        self.notebook.add(servicio, text="Servicios")

        self.notebook.pack(fill=tk.BOTH, expand=1)

    
    def ejecuta_consulta(self,consulta, parametros = ()):
        with sqlite3.connect(self.BaseDatos) as conn: #El width vendria a ser como el contexto
            cursor = conn.cursor() 
            resultado = cursor.execute(consulta, parametros) #se define la consulta y se guarda en la variante resultado
            conn.commit() #Y esto ejecuta lo guardado en la variante "resultado"
                        #Como inicializamos el sqlite con la función "width" no hace falta cerrar la conexión. 
        return resultado  

    def devuelve_consulta(self):
        #Limpiando la tabla
        registros = self.tabla.get_children() #la func "get_children" devuleve todo los elmentos que tenemos en la tabla, por si queres limpiar o agregar
        for registro in registros: #Recorro los elementos para eliminarlos
            self.tabla.delete(registro)
        
        registros1 = self.tabla1.get_children()
        for registro1 in registros1:
            self.tabla1.delete(registro1)
        
        registros2 = self.tabla2.get_children()
        for registro2 in registros2:
            self.tabla2.delete(registro2)
        
        #Consultando datos
        consulta = "SELECT * FROM Clientes"
        db_filas = self.ejecuta_consulta(consulta)  

        consulta1 = "SELECT * FROM Equipos"
        db_filas1 = self.ejecuta_consulta(consulta1)

        consulta2 = "SELECT * FROM Servicios"
        db_filas2 = self.ejecuta_consulta(consulta2)
        
        #Rellenando los datos
        for fila in db_filas:
            self.tabla.insert("",0, text='', values=(fila))
        
        for fila1 in db_filas1:
            self.tabla1.insert('', 0, text='', values=(fila1))

        for fila2 in db_filas2:
            self.tabla2.insert('', 0, text='', values=(fila2))

    def validacionCliente(self):
        return len(self.nombre.get()) != 0 and len(self.celular.get()) !=0 #Pido validar los datos de las variantes que no van a ser nulas

    def validacionEquipo(self):
        return len(self.ID_Cliente.get()) != 0 and len(self.marca.get()) != 0 and len(self.modelo.get()) != 0 

    def validacionServicio(self):
        return len(self.ID_Equipo.get()) != 0 and len(self.servicio.get()) != 0 and len(self.fecha.get()) != 0 

    def Agregar_Cliente(self):
        if self.validacionCliente():
            consulta = "INSERT INTO Clientes VALUES (NULL, ?, ?,?,?)"
            parametros = (self.nombre.get(), self.direccion.get(),self.celular.get(),self.email.get()) #get() es lo que el usuario esta tipiando
            self.ejecuta_consulta(consulta, parametros)
            self.mensaje["text"] = f"- El Cliente {self.nombre.get()} ha sido agregado -"
            self.nombre.delete(0, END) #Esto es para que se limpien las casillas una vez apretado el boton
            self.direccion.delete(0, END) #que vuelvan a su estado inicial
            self.celular.delete(0,END)
            self.email.delete(0,END)
        else: 
            self.mensaje["text"] = "- Los datos son requeridos -"
        self.devuelve_consulta() #Independientemente de si se ejecuta o no devuelve los cambios

    def Agregar_Equipo(self):
        if self.validacionEquipo():
            consulta = "INSERT INTO Equipos VALUES (?,NULL, ?, ?, ?)"
            if len(self.potencia.get()) !=0:
                parametros = (self.ID_Cliente.get(),self.marca.get(), self.modelo.get(),self.potencia.get()) 
            else:
                parametros = (self.ID_Cliente.get(), self.marca.get(), self.modelo.get())
            self.ejecuta_consulta(consulta, parametros)
            self.mensaje1["text"] = f"- El Equipo {self.marca.get()} ha sido agregado -"
            self.ID_Cliente.delete(0, END) 
            self.marca.delete(0, END)
            self.modelo.delete(0,END)
            self.potencia.delete(0,END)
        else: 
            self.mensaje1["text"] = "- Los datos son requeridos -"
        self.devuelve_consulta()

    def Agregar_Servicios(self):
        if self.validacionServicio():
            consulta = "INSERT INTO Servicios VALUES (?, ?, ?)"
            parametros = (self.ID_Equipo.get(),self.servicio.get(),self.fecha.get())
            self.ejecuta_consulta(consulta, parametros)
            self.mensaje2["text"] = f"- El Equipo {self.marca.get()} ha sido agregado -"
            self.ID_Equipo.delete(0,END)
            self.servicio.delete(0, END)
            self.fecha.delete(0, END)
        else:
            self.mensaje2["text"] = "- Los datos son requeridos -"
        self.devuelve_consulta()

    def Eliminar_Cliente(self):
        self.mensaje["text"] = "" #Hacemos esto para que no muestre mensaje cuando ejecutemos
        try:
            self.tabla.item(self.tabla.selection())["values"][0]
        except IndexError as e:
            self.mensaje["text"] = "- Porfavor seleccione un registro -"
            return #Retornamos para que no continue
        dato = self.tabla.item(self.tabla.selection())["values"][0] #Selecciona el item en el que presionamos y lo guarda
        consulta = "DELETE FROM Clientes WHERE ID_Clientes = ?"
        self.ejecuta_consulta(consulta, (dato,)) #Dejamos una "," después del name para que sepa que es una tupla
        self.mensaje["text"] = f"- El dato {dato} se ha eliminado -"
        self.devuelve_consulta()    


    def Eliminar_Equipo(self):
        self.mensaje1["text"] = "" 
        try:
            self.tabla1.item(self.tabla1.selection())["values"][0]
        except IndexError as e:
            self.mensaje1["text"] = "- Porfavor seleccione un registro -"
            return #Retornamos para que no continue
        dato = self.tabla1.item(self.tabla1.selection())["values"][0] 
        consulta = "DELETE FROM Equipos WHERE ID_Clientes = ?"
        self.ejecuta_consulta(consulta, (dato,)) 
        self.mensaje1["text"] = f"- El dato {dato} se ha eliminado -"
        self.devuelve_consulta()

    def Eliminar_Servicio(self):
        self.mensaje2["text"] = "" 
        try:
            self.tabla2.item(self.tabla2.selection())["values"][0]
        except IndexError as e:
            self.mensaje2["text"] = "- Porfavor seleccione un registro -"
            return #Retornamos para que no continue
        dato = self.tabla2.item(self.tabla2.selection())["values"][0] 
        consulta = "DELETE FROM Servicios WHERE ID_Equipos = ?"
        self.ejecuta_consulta(consulta, (dato,)) 
        self.mensaje2["text"] = f"- El dato {dato} se ha eliminado -"
        self.devuelve_consulta()   

    def Editar_Cliente(self):
        self.mensaje["text"] = "" 
        try:
            self.tabla.item(self.tabla.selection())["values"][0]
        except IndexError as e:
            self.mensaje["text"] = "- Porfavor seleccione un registro -"
            return
        OLDNombre = self.tabla.item(self.tabla.selection())["values"][1]
        OLDDireccion = self.tabla.item(self.tabla.selection())["values"][2]
        OLDCelular = self.tabla.item(self.tabla.selection())["values"][3]
        OLDEmail = self.tabla.item(self.tabla.selection())["values"][4]
        self.EditarVentana = Toplevel () # Esto me crea una ventana apartir de presionar el Editar
        self.EditarVentana.title = "Editar producto"

        #Old name
        Label(self.EditarVentana, text = "Nombre anterior: ").grid(row = 0, column = 1)
        Entry(self.EditarVentana, textvariable = StringVar(self.EditarVentana, value = OLDNombre), state = "readonly").grid(
            row = 0, column = 2
        )
        
        #New name
        Label(self.EditarVentana, text = "Nombre actual: ").grid(row = 1, column = 1)
        NuevoNombre= Entry(self.EditarVentana)
        NuevoNombre.grid(row = 1, column = 2)

        #Old Direccion
        Label(self.EditarVentana, text = "Dirección anterior: ").grid(row = 2, column = 1)
        Entry(self.EditarVentana, textvariable = StringVar(self.EditarVentana, value = OLDDireccion), state = "readonly").grid(
            row = 2, column = 2
        )

        #New Direccion
        Label(self.EditarVentana, text = "Dirección actual: ").grid(row = 3, column = 1)
        NuevaDireccion= Entry(self.EditarVentana)
        NuevaDireccion.grid(row = 3, column = 2)

        #Old Celular
        Label(self.EditarVentana, text = "Número anterior: ").grid(row = 4, column = 1)
        Entry(self.EditarVentana, textvariable = StringVar(self.EditarVentana, value = OLDCelular), state = "readonly").grid(
            row = 4, column = 2
        )

        #New Celular
        Label(self.EditarVentana, text = "Número actual: ").grid(row = 5, column = 1)
        NuevoCelular= Entry(self.EditarVentana)
        NuevoCelular.grid(row = 5, column = 2)

        #Old Email
        Label(self.EditarVentana, text = "Email anterior: ").grid(row = 6, column = 1)
        Entry(self.EditarVentana, textvariable = StringVar(self.EditarVentana, value = OLDEmail), state = "readonly").grid(
            row = 6, column = 2
        )

        #New Email
        Label(self.EditarVentana, text = "Email actual: ").grid(row = 7, column = 1)
        NuevoEmail= Entry(self.EditarVentana)
        NuevoEmail.grid(row = 7, column = 2)

        #BOTON UPDATE
        Button (self.EditarVentana, text = "Actualizar",command = lambda: self.EditarRegistrosClientes(NuevoNombre.get(),NuevaDireccion.get(),NuevoCelular.get(),NuevoEmail.get(),OLDNombre,OLDDireccion,OLDCelular,OLDEmail)).grid(row = 8, column = 2, sticky = W)

    def EditarRegistrosClientes(self,NuevoNombre, NuevaDireccion,NuevoCelular,NuevoEmail,OLDNombre,OLDDireccion,OLDCelular,OLDEmail):
        consulta = """UPDATE Clientes SET NombreApellido = ?, Direccion = ?,Celular = ?,
         Email = ? WHERE NombreApellido = ? AND Direccion = ? AND Celular = ? AND Email = ?"""
        parametros = (NuevoNombre, NuevaDireccion,NuevoCelular,NuevoEmail,OLDNombre,OLDDireccion,OLDCelular,OLDEmail)
        self.ejecuta_consulta(consulta, parametros)
        self.EditarVentana.destroy()
        self.mensaje["text"] = f"Registro {NuevoNombre} ha sido actualizado"
        self.devuelve_consulta()

    def Editar_Equipo(self):
        self.mensaje1["text"] = "" 
        try:
            self.tabla1.item(self.tabla1.selection())["values"][0]
        except IndexError as e:
            self.mensaje1["text"] = "- Porfavor seleccione un registro -"
            return
        OLDIDCliente = self.tabla1.item(self.tabla1.selection())["values"][0]
        OLDMarca = self.tabla1.item(self.tabla1.selection())["values"][2]
        OLDModelo = self.tabla1.item(self.tabla1.selection())["values"][3]
        OLDPotencia = self.tabla1.item(self.tabla1.selection())["values"][4]
        self.EditarVentana = Toplevel () # Esto me crea una ventana apartir de presionar el Editar
        self.EditarVentana.title = "Editar Equipo"
        
         #Old id
        Label(self.EditarVentana, text = "ID Cliente anterior: ").grid(row = 0, column = 1)
        Entry(self.EditarVentana, textvariable = StringVar(self.EditarVentana, value = OLDIDCliente), state = "readonly").grid(
            row = 0, column = 2
        )
        
        #New id
        Label(self.EditarVentana, text = "ID Cliente Acutal: ").grid(row = 1, column = 1)
        NuevoID= Entry(self.EditarVentana)
        NuevoID.grid(row = 1, column = 2)

        #Old Marca
        Label(self.EditarVentana, text = "Marca anterior: ").grid(row = 2, column = 1)
        Entry(self.EditarVentana, textvariable = StringVar(self.EditarVentana, value = OLDMarca ), state = "readonly").grid(
            row = 2, column = 2
        )

        #New Marca
        Label(self.EditarVentana, text = "Marca  actual: ").grid(row = 3, column = 1)
        NuevaMarca = Entry(self.EditarVentana)
        NuevaMarca .grid(row = 3, column = 2)

        #Old Modelo
        Label(self.EditarVentana, text = "Modelo anterior: ").grid(row = 4, column = 1)
        Entry(self.EditarVentana, textvariable = StringVar(self.EditarVentana, value = OLDModelo), state = "readonly").grid(
            row = 4, column = 2
        )

        #New Modelo
        Label(self.EditarVentana, text = "Modelo actual: ").grid(row = 5, column = 1)
        NuevoModelo= Entry(self.EditarVentana)
        NuevoModelo.grid(row = 5, column = 2)

        #Old Potencia
        Label(self.EditarVentana, text = "Potencia anterior: ").grid(row = 6, column = 1)
        Entry(self.EditarVentana, textvariable = StringVar(self.EditarVentana, value = OLDPotencia), state = "readonly").grid(
            row = 6, column = 2
        )

        #New Potencia
        Label(self.EditarVentana, text = "Potencia actual: ").grid(row = 7, column = 1)
        NuevaPotencia= Entry(self.EditarVentana)
        NuevaPotencia.grid(row = 7, column = 2)

        #BOTON UPDATE
        Button (self.EditarVentana, text = "Actualizar",command = lambda: self.EditarRegistrosEquipos(NuevoID.get(),NuevaMarca.get(),NuevoModelo.get(),NuevaPotencia.get(),OLDIDCliente,OLDMarca,OLDModelo,OLDPotencia)).grid(row = 8, column = 2, sticky = W)

    def EditarRegistrosEquipos(self,NuevoID, NuevaMarca,NuevoModelo,NuevaPotencia,OLDIDCliente,OLDMarca,OLDModelo,OLDPotencia):
        consulta = """UPDATE Equipos SET ID_Clientes = ?, Marca = ?,Modelo = ?,
         Potencia = ? WHERE ID_Clientes = ? AND Marca = ? AND Modelo = ? AND Potencia = ?"""
        parametros = (NuevoID, NuevaMarca,NuevoModelo,NuevaPotencia,OLDIDCliente,OLDMarca,OLDModelo,OLDPotencia)
        self.ejecuta_consulta(consulta, parametros)
        self.EditarVentana.destroy()
        self.mensaje["text"] = f"Registro {NuevaMarca} ha sido actualizado"
        self.devuelve_consulta()


    def Editar_Servicio(self):
        self.mensaje2["text"] = "" 
        try:
            self.tabla2.item(self.tabla2.selection())["values"][0]
        except IndexError as e:
            self.mensaje2["text"] = "- Porfavor seleccione un registro -"
            return
        OLDIDEquipo = self.tabla2.item(self.tabla2.selection())["values"][0]
        OLDServicio = self.tabla2.item(self.tabla2.selection())["values"][1]
        OLDFecha = self.tabla2.item(self.tabla2.selection())["values"][2]
        
        self.EditarVentana = Toplevel () # Esto me crea una ventana apartir de presionar el Editar
        self.EditarVentana.title = "Editar Registros de Servicios"

         #Old id
        Label(self.EditarVentana, text = "ID Equipo anterior: ").grid(row = 0, column = 1)
        Entry(self.EditarVentana, textvariable = StringVar(self.EditarVentana, value = OLDIDEquipo), state = "readonly").grid(
            row = 0, column = 2
        )
        
        #New id
        Label(self.EditarVentana, text = "ID equipo Acutal: ").grid(row = 1, column = 1)
        NuevoIDEquipo= Entry(self.EditarVentana)
        NuevoIDEquipo.grid(row = 1, column = 2)

        #Old Servicio
        Label(self.EditarVentana, text = "Servicio anterior: ").grid(row = 2, column = 1)
        Entry(self.EditarVentana, textvariable = StringVar(self.EditarVentana, value = OLDServicio ), state = "readonly").grid(
            row = 2, column = 2
        )

        #New Servicio
        Label(self.EditarVentana, text = "Servicio actual: ").grid(row = 3, column = 1)
        NuevoServicio = Entry(self.EditarVentana)
        NuevoServicio .grid(row = 3, column = 2)

        #Old Fecha
        Label(self.EditarVentana, text = "Fecha anterior: ").grid(row = 4, column = 1)
        Entry(self.EditarVentana, textvariable = StringVar(self.EditarVentana, value = OLDFecha), state = "readonly").grid(
            row = 4, column = 2
        )

        #New Fecha
        Label(self.EditarVentana, text = "Modelo actual: ").grid(row = 5, column = 1)
        NuevaFecha= Entry(self.EditarVentana)
        NuevaFecha.grid(row = 5, column = 2)


        #BOTON UPDATE
        Button (self.EditarVentana, text = "Actualizar",command = lambda: self.EditarRegistrosServicios(NuevoIDEquipo.get(),NuevoServicio.get(),NuevaFecha.get(),OLDIDEquipo,OLDServicio,OLDFecha)).grid(row = 6, column = 2, sticky = W)

    def EditarRegistrosServicios(self,NuevoIDEquipo, NuevoServicio,NuevaFecha,OLDIDEquipo,OLDServicio,OLDFecha):
        consulta = """UPDATE Servicios SET ID_Equipos = ?, Servicio = ?,Fecha = ?
         WHERE ID_Equipos = ? AND Servicio = ? AND Fecha = ?"""
        parametros = (NuevoIDEquipo, NuevoServicio,NuevaFecha,OLDIDEquipo,OLDServicio,OLDFecha)
        self.ejecuta_consulta(consulta, parametros)
        self.EditarVentana.destroy()
        self.mensaje["text"] = f"Registro {NuevoIDEquipo} ha sido actualizado"
        self.devuelve_consulta()























if __name__ == '__main__':
    grupo = Electrogenos()
    grupo.devuelve_consulta()
    grupo.mainloop()


   