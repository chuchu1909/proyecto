#Gestion de productos
import requests


lista_productos = []

class producto:
    def __init__(self, name, description, price, category, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.quantity = quantity


def agregar_producto():
    name = input("Ingrese el nombre del producto: ")
    description = input("Ingrese la descripción del producto: ")
    price = float(input("Ingrese el precio del producto: "))
    category = input("Ingrese la categoría del producto: ")
    quantity = int(input("Ingrese el inventario disponible del producto: "))

    producto = producto(name, description, price, category, quantity)
    lista_productos.append(producto)

    print("El producto ha sido agregado exitosamente.")

    


def buscar_productos():
    filtro = input("Ingrese el filtro de búsqueda: ")
    lista_productos = []
    for producto in lista_productos:
        if filtro.lower() in producto.nombre.lower():

            if len(lista_productos) > 0:
                print("Resultados de la búsqueda:")
                for producto in lista_productos:
                    print(f"Nombre: {producto.name}")
                    print(f"Descripción: {producto.description}")
                print(f"Precio: {producto.price}")
                print(f"Categoría: {producto.category}")
                print(f"Inventario: {producto.qunatity}")
        else:
            print("No se encontraron productos que coincidan con el filtro de búsqueda.")


def modificar_producto():
    name = input("ingresa el nombre del producto que quieras modificar")

    for producto in lista_productos:
        if producto["name"] == name:
            name = input("ingrese el nuevo nombre")
            producto["name"] = name
            description = input("ingrese la nueva descripcion")
            producto["description"] = description
            price = input("ingrese el nuevo precio")
            producto["price"] = price
            category = input("ingrese la nueva categoria")
            producto["category"] = category
            quantity = input("ingrese la nueva cantidad del producto")
            producto["quantity"] = quantity


def eliminar_producto():
    name = input["ingrese el nombre del producto que desea eliminar"]

    for producto in lista_productos:
        if producto["name"] == name:
            lista_productos.remove(producto)
            print("producto eliminado correctamente")






