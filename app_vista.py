from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from tkinter import messagebox
from app_modelo import crud


###########VENTANA###########

class Vista():
    def __init__(self, ventana):
        self.root = ventana
        self.var_producto = StringVar()
        self.var_cantidad = IntVar()
        self.var_precio = IntVar()
        self.stock1 = crud()

###########Titulo###########

        self.root.title("Aplicación de Control de Stock")

###########Labels###########

        self.producto = Label(self.root, text="Producto")
        self.producto.grid(row=1, column=3, sticky=W)

        self.cantidad = Label(self.root, text="Cantidad")
        self.cantidad.grid(row=2, column=3, sticky=W)

        self.precio = Label(self.root, text="Precio")
        self.precio.grid(row=3, column=3, sticky=W)

###########Entradas###########

        self.entry_1 = Entry(self.root, textvariable=self.var_producto)
        self.entry_1.grid(row=1, column=4)

        self.entry_2 = Entry(self.root, textvariable=self.var_cantidad)
        self.entry_2.grid(row=2, column=4)

        self.entry_3 = Entry(self.root, textvariable=self.var_precio)
        self.entry_3.grid(row=3, column=4)

###########Treeview###########

        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("col1", "col2", "col3")
        self.tree.column("#0", width=60, minwidth=60)
        self.tree.column("col1", width=120, minwidth=80)
        self.tree.column("col2", width=60, minwidth=80)
        self.tree.column("col3", width=60, minwidth=80)

        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Producto")
        self.tree.heading("col2", text="Cantidad")
        self.tree.heading("col3", text="Precio")
        self.tree.grid(row=10, column=4, columnspan=3)

###########Botones###########

        self.boton_nuevo = Button(self.root, text="Guardar",command=lambda: self.stock1.alta(self.var_producto, self.var_cantidad, self.var_precio, self.tree))
        self.boton_nuevo.grid(row=1, column=5)

        self.boton_eliminar = Button(self.root, text="Eliminar",command=lambda: self.stock1.borrar(self.tree))
        self.boton_eliminar.grid(row=2, column=5)

        self.boton_editar = Button(self.root, text="Editar",command=lambda: self.stock1.modificar(self.var_producto, self.var_cantidad, self.var_precio, self.tree))
        self.boton_editar.grid(row=3, column=5)

        self.boton_consultar = Button(self.root, text="Refresh",command=lambda: self.stock1.consultar(self.tree))
        self.boton_consultar.grid(row=9, column=3)

