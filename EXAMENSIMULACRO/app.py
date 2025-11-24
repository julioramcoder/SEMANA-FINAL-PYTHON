from GestionInventario import *

def menu_principal():
    while True:
        print("\n========== MENU PRINCIPAL ==========\n")
        print("¿Que quieres hacer hoy?, selecciona una las siguientes opciones:\n")

        print("1. Gestion del inventario")
        print("2. Registro y consulta de ventas")
        print("3. Validar stock disponible")
        print("4. Historial de ventas (solo ver)")
        print("5. Modulo de reportes")
        print("6. Salir")

        procesos = input("Por favor ingresa el numero de la actividad que quieres hacer hoy: ").strip()

        if procesos == "1":
            modulo_inventario()   
        elif procesos == "2":
            modulo_ventas()    
        elif procesos == "3":
            validarStock()
        elif procesos == "4":
            mostrar_historial_ventas()
        elif procesos == "5":
            modulo_reportes()     
        elif procesos == "6":
            print("Saliendo del programa...")
            break
        else:
            print("ERROR: opción invalida. Intenta otra vez.")

# ESTA LÍNEA ES CLAVE:
menu_principal()
