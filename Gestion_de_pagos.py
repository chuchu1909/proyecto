#Gestion de pagos
class Pago:
    def __init__(self, cliente, monto, moneda, tipo_pago, fecha):
        self.cliente = cliente
        self.monto = monto
        self.moneda = moneda
        self.tipo_pago = tipo_pago
        self.fecha = fecha

pagos = []

def registrar_pago():
    cliente = input("Cliente que realizó el pago: ")
    monto = float(input("Monto del pago: "))
    moneda = input("Moneda del pago: ")
    tipo_pago = input("Tipo de pago: ")
    fecha = input("Fecha del pago: ")

    pago = Pago(cliente, monto, moneda, tipo_pago, fecha)
    pagos.append(pago)
    print("Pago registrado exitosamente!")

def buscar_pagos():
    filtro_cliente = input("Filtrar por cliente (dejar en blanco para no filtrar): ")
    filtro_fecha = input("Filtrar por fecha (dejar en blanco para no filtrar): ")
    filtro_tipo_pago = input("Filtrar por tipo de pago (dejar en blanco para no filtrar): ")
    filtro_moneda = input("Filtrar por moneda de pago (dejar en blanco para no filtrar): ")

    resultados = []
    for pago in pagos:
        if (not filtro_cliente or pago.cliente == filtro_cliente) and \
                (not filtro_fecha or pago.fecha == filtro_fecha) and \
                (not filtro_tipo_pago or pago.tipo_pago == filtro_tipo_pago) and \
                (not filtro_moneda or pago.moneda == filtro_moneda):
            resultados.append(pago)

    if resultados:
        print("Resultados de búsqueda:")
        for resultado in resultados:
            print(f"Cliente: {resultado.cliente}, Monto: {resultado.monto}, Moneda: {resultado.moneda}, Tipo de pago: {resultado.tipo_pago}, Fecha: {resultado.fecha}")
    else:
        print("No se encontraron resultados para los filtros especificados.")

while True:
    print("== Gestión de Pagos ==")
    print("1. Registrar pago")
    print("2. Buscar pagos")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        registrar_pago()
    elif opcion == "2":
        buscar_pagos()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")