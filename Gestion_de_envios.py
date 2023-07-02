class Envio:
    def __init__(self, orden_compra, servicio_envio, motorizado=None, costo_servicio=0):
        self.orden_compra = orden_compra
        self.servicio_envio = servicio_envio
        self.motorizado = motorizado
        self.costo_servicio = costo_servicio

# Lista para almacenar los envíos
envios = []

def registrar_envio():
    orden_compra = input("Ingrese la orden de compra: ")
    servicio_envio = input("Ingrese el servicio de envío (MRW, Zoom, Delivery, etc.): ")
    costo_servicio = float(input("Ingrese el costo del servicio: "))

    if servicio_envio.lower() == "delivery":
        nombre_motorizado = input("Ingrese el nombre del motorizado: ")
        telefono_motorizado = input("Ingrese el teléfono del motorizado: ")
        motorizado = {"nombre": nombre_motorizado, "telefono": telefono_motorizado}
        
        envio = Envio(orden_compra, servicio_envio, motorizado, costo_servicio)
    else:
        envio = Envio(orden_compra, servicio_envio, None, costo_servicio)

    envios.append(envio)
    print("Envío registrado exitosamente!")

def buscar_envios():
    filtro_cliente = input("Ingrese el cliente para filtrar los envíos: ")
    filtro_fecha = input("Ingrese la fecha para filtrar los envíos: ")
    
    envios_filtrados = [envio for envio in envios if envio.orden_compra == filtro_cliente or envio.fecha == filtro_fecha]

    if len(envios_filtrados) > 0:
        print("Envíos encontrados:")
        for envio in envios_filtrados:
            print(f"Orden de compra: {envio.orden_compra}")
            print(f"Servicio de envío: {envio.servicio_envio}")
            if envio.motorizado:
                print(f"Motorizado: {envio.motorizado['nombre']} - {envio.motorizado['telefono']}")
            print(f"Costo del servicio: {envio.costo_servicio}")
            print("-------------------------------")
    else:
        print("No se encontraron envíos con los filtros especificados.")

# Menú principal
while True:
    print("===== Gestión de envíos =====")
    print("1. Registrar envío")
    print("2. Buscar envíos")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_envio()
    elif opcion == "2":
        buscar_envios()
    elif opcion == "0":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")