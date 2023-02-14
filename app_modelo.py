from tkinter.messagebox import *
from tkinter.messagebox import *
import sqlite3
from app_decorador import*
from app_observador import Sujeto
from peewee import *
import re


db = SqliteDatabase("mibase.db")

class BaseModel(Model):
        class Meta:
            database = db

class Stock(BaseModel):
        producto = CharField()
        cantidad = CharField()
        precio = CharField()

db.connect()
db.create_tables([Stock])


class crud(Sujeto):
    def __init__(self,
    ):pass

    def actualizar_treeview(self, mitreeview):
        records = mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)

        for valor_rec in Stock.select():
            mitreeview.insert("", 0, text=valor_rec.id,values=(valor_rec.producto, valor_rec.cantidad, valor_rec.precio),
            )
            
    @decorador_alta
    def alta(self, producto, cantidad, precio, mitreeview):

        stock = Stock()
        stock.producto = producto.get()
        stock.cantidad = cantidad.get()
        stock.precio = precio.get()
        stock.save()
        showinfo(message="Producto dado de alta con éxito", title="Alta")

        self.actualizar_treeview(mitreeview)
        
    @decorador_borrar
    def borrar(self, mitreeview):
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        borrar = Stock.get(Stock.id == valor_id["text"])
        if askyesno("Borrar Producto", f"¿Desea borrar el producto?"):
            try:
                borrar.delete_instance()
                showinfo("Borrar", "Eliminado con éxito")
                self.actualizar_treeview(mitreeview)
            except:
                showerror(message="Error al eliminar el producto", title="Error")

    @decorador_modificar
    def modificar(self, producto, cantidad, precio, mitreeview):
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        actualizar = Stock.update(
            producto=producto.get(), cantidad=cantidad.get(), precio=precio.get()
        ).where(Stock.id == valor_id["text"])
        actualizar.execute()
        showinfo(message="Producto actualizado con éxito", title="Modificación")

        self.actualizar_treeview(mitreeview)

    def consultar(self, mitreeview):
        self.actualizar_treeview(mitreeview)
