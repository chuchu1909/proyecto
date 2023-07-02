import ayudame_diosito as f
from ayudame_diosito import *
import Gestion_de_ventas as f
from Gestion_de_ventas import*
import Gestion_de_clientes as f
from Gestion_de_clientes import*
import Gestion_de_pagos as f
from Gestion_de_pagos import*
import Gestion_de_envios as f
from Gestion_de_envios import*      


while True:
    print("Bienvenido a la tienda en línea de productos naturales")
    print("1. Gestión de productos")
    print("2. Gestión de ventas")
    print("3. Gestión de clientes")
    print("4. Gestión de pagos")
    print("5. Gestión de envíos")
    print("6. Indicadores de gestión (estadísticas)")

    seleccion = input(">> ")

    while seleccion != "1" and seleccion != "2" and seleccion != "3" and seleccion != "4" and seleccion  != "5" and seleccion != "6":
        seleccion = input("Valor incorrecto, Por favor eliga una opcion mostrada en pantalla \n >>")

    if seleccion == "1":

        print("Módulo de gestión de productos")
        print("1. agregar_producto")
        print("2. Buscar producto")
        print("3. Modificar producto")
        print("4. Eliminar producto")


        seleccion1 = input(">> ")


        while seleccion1 != "1" and seleccion1 != "2" and seleccion1 != "3" and seleccion1 != "4":
           seleccion1 = input("Valor incorrecto, Por favor eliga una opcion mostrada en pantalla \n >>")

        if seleccion1 == "1":
            f.agregar_producto()
        if seleccion1 == "2":
            f.buscar_productos()
        if seleccion1 == "3":
            f.modificar_producto()
        if seleccion1 == "4":
            f.eliminar_producto()
        
    if seleccion == "2":

        print("Módulo de gestión de ventas")
        print("ventas seleccion")


        ventas1 = input(">> ")


        while ventas1 != "1" :
           ventas1 = input("Valor incorrecto, Por favor eliga una opcion mostrada en pantalla \n >>")

        if ventas1 == 1:
            f.ventas_seleccion()

    if seleccion == "3":

        print("Módulo de gestión de clientes")
        print("1. Registrar cliente")
        print("2. Modificar cliente")
        print("3. eliminar cliente")
        print("4. buscar cliente")

        clientes1 = input(">> ")


        while clientes1 != "1" and clientes1 != "2" and clientes1 != "3" and clientes1 != "4":

           seleccion1 = input("Valor incorrecto, Por favor eliga una opcion mostrada en pantalla \n >>")        
        if clientes1 == "1":
            f.registrar_cliente()
        if clientes1 == "2":
            f.modificar_cliente()
        if clientes1 == "3":
            f.eliminar_cliente()
        if clientes1 == "4":
            f.buscar_cliente()




    if seleccion == "4":

        print("Módulo de gestión de pagos")
        print("1. crear producto")
        print("2. buscar pagos")

        pagos1 = input(">> ")


        while pagos1 != "1" and pagos1 != "2" :

           pagos1 = input("Valor incorrecto, Por favor eliga una opcion mostrada en pantalla \n >>")       

        if pagos1 == "1":
            f.registrar_pago()
        if pagos == "2":
            f.buscar_producto()


    if seleccion == "5":

        print("Módulo de gestión de envíos")
        print("1. registrar envio")
        print("2. Buscar envios")


        envios1 = input(">> ")


        while envios1 != "1" and envios1 != "2":
           envios1 = input("Valor incorrecto, Por favor eliga una opcion mostrada en pantalla \n >>")

        if envios1 == "1":
            f.registrar_envio()
        if envios1 == "2":
            f.buscar_envios

    if seleccion == "6":

        print("Módulo de indicadores de gestión (estadísticas)")
        print("1. Graficos") 
