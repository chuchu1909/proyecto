class Venta:
        def __init__(self, cliente, productos, cantidades, metodo_pago, metodo_envio):
                self.cliente = cliente
                self.productos = productos
                self.cantidades = cantidades
                self.metodo_pago = metodo_pago
                self.metodo_envio = metodo_envio

        def calcular_total(self):
                subtotal = sum([producto.precio * cantidad for producto, cantidad in zip(self.productos, self.cantidades)])
                descuento = 0
                if self.cliente.tipo == "juridico" and self.metodo_pago == "contado":
                        descuento = subtotal * 0.05
                iva = subtotal * 0.16
                igtf = 0
                if self.metodo_pago == "divisas":
                        igtf = subtotal * 0.03
                total = subtotal - descuento + iva + igtf
                return total
        
class Cliente:
        def __init__(self, nombre, tipo):
                self.nombre = nombre
                self.tipo = tipo

ventas = []

def ventas_seleccion():

    while True:
        print("Bienvenido a la gestión de ventas")
        print("1. Registrar una venta")
        print("2. Generar facturas")
        print("3. Buscar ventas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
                cliente_nombre = input("Ingrese el nombre del cliente: ")
                cliente_tipo = input("Ingrese el tipo de cliente (juridico o natural): ")
                cliente = Cliente(cliente_nombre, cliente_tipo)

                productos = []
                cantidades = []

                while True:
                        producto_nombre = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
                        if producto_nombre == "fin":
                                break
                        cantidad = int(input("Ingrese la cantidad: "))
                        productos.append(producto_nombre)
                        cantidades.append(cantidad)

                metodo_pago = input("Ingrese el método de pago: ")
                metodo_envio = input("Ingrese el método de envío: ")

                venta = Venta(cliente, productos, cantidades, metodo_pago, metodo_envio)
                ventas.append(venta)

                print("¡Venta registrada con éxito!")
        
        elif opcion == "2":
                for i, venta in enumerate(ventas):
                        print(f"Factura de Venta #{i+1}")
                        print("Cliente:", venta.cliente.nombre)
                        print("Productos comprados:")
                        for producto, cantidad in zip(venta.productos, venta.cantidades):
                                print(producto, "x", cantidad)
                        print("Método de pago:", venta.metodo_pago)
                        print("Método de envío:", venta.metodo_envio)
                        print("Total de compra:", venta.calcular_total())
                        print()

        elif opcion == "3":
                filtro_cliente = input("Ingrese el nombre del cliente para filtrar (o dejar vacío para mostrar todas las ventas): ")
                filtro_fecha = input("Ingrese la fecha de venta para filtrar (o dejar vacío para mostrar todas las ventas): ")
                filtro_monto = input("Ingrese el monto total de venta para filtrar (o dejar vacío para mostrar todas las ventas): ")

                ventas_filtradas = []

                for venta in ventas:
                        if (filtro_cliente == "" or venta.cliente.nombre == filtro_cliente) and (filtro_fecha == "" or venta.fecha == filtro_fecha) and (filtro_monto == "" or venta.calcular_total() == float(filtro_monto)):
                                ventas_filtradas.append(venta)

                for i, venta in enumerate(ventas_filtradas):
                        print(f"Venta #{i+1}")
                        print("Cliente:", venta.cliente.nombre)
                        print("Productos comprados:")
                        for producto, cantidad in zip(venta.productos, venta.cantidades):
                                print(producto, "x", cantidad)
                        print("Método de pago:", venta.metodo_pago)
                        print("Método de envío:", venta.metodo_envio)
                        print("Total de compra:", venta.calcular_total())
                        print()
        
        elif opcion == "4":
                print("¡Hasta luego!")
                break

        else:
                print("Opción inválida. Por favor, seleccione una opción válida.")