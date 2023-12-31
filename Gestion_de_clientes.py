#Gestion de clientes
lista_clientes = []

class Cliente:
    def __init__(self, nombre, tipo, cedula_rif, correo, direccion, telefono):
        self.nombre = nombre
        self.tipo = tipo
        self.cedula_rif = cedula_rif
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono

def registrar_cliente():
    name = input("Ingrese el nombre y apellido del cliente: ")
    tipe = input("Ingrese el tipo de cliente (Natural o Jurídico): ")
    cedula_rif = input("Ingrese la cédula o RIF del cliente: ")
    correo = input("Ingrese el correo electrónico del cliente: ")
    direccion = input("Ingrese la dirección de envío del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")

    cliente = cliente( name, tipe, cedula_rif, correo, direccion, telefono)
    lista_clientes.append(cliente)

    print("Cliente registrado correctamente.")

def modificar_cliente():
    cedula_rif = input("Ingrese la cédula o RIF del cliente que desea modificar: ")

    for cliente in lista_clientes:
        if cliente["cedula"] == cedula_rif:
            nombre = input("Ingrese el nuevo nombre y apellido del cliente: ")
            cliente["nombre"] = nombre
            tipe = input("ingrese el nuevo tipo de cliente natural o juridico:")
            cliente["tipe"] = tipe
            cedula_rif = input("ingrese la nueva cedula o rif:")
            cliente["cedula_rif"] = cedula_rif
            correo = input("ingrese el nuevo correo")
            cliente["correo"] = correo
            direccion = input("ingrese la nueva direccion:")
            cliente["direccion"] = direccion
            telefono = input("ingrese el nuevo telefono")
            cliente["telefono"] = telefono

def eliminar_cliente():
    cedula_rif = input("Ingrese la cédula o RIF del cliente que desea eliminar: ")

    for cliente in lista_clientes:
        if cliente["cedula"] == cedula_rif:
            lista_clientes.remove(cliente)
            print("Cliente eliminado correctamente.")

def buscar_cliente():
    opcion = input("Seleccione el filtro de búsqueda:\n1. Cédula o RIF\n2. Correo electrónico\n")
    
    if opcion == "1":
        cedula_rif = input("Ingrese la cédula o RIF del cliente que desea buscar: ")
        
        for cliente in lista_clientes:
            if cliente["cedula"] == cedula_rif:
                print("Cliente encontrado:")
                print(cliente)
    elif opcion == "2":
        correo = input("Ingrese el correo electrónico del cliente que desea buscar: ")
        
        for cliente in lista_clientes:
            if cliente["correo"] == correo:
                print("Cliente encontrado:")
                print(cliente)
    else:
        print("Opción inválida")
