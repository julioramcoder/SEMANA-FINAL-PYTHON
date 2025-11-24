#============ MENU PRINCIPAL ==========#

from moduloDeServicio import*
from archivos import menu_cargar_csv
from archivos import menu_guardar_csv
while True:
    print("\n========== MENU PRINCIPAL ==========\n")
    
    print("¿Que quieres hacer hoy?, selecciona una las siguientes opciones:\n")

    print("1. Agregar Productos")
    print("2. Buscar  Productos")
    print("3. Actualizar Producto")
    print("4. Eliminar Productos")
    print("5. Calculos Estadisticos")
    print("6. Mostrar Inventario Actual")
    print("7. guardar CSV")
    print("8. cargar CSV")
    print("9. salir")

    procesos = input ("Por favor ingresa el numero de la actividad que quieres hacer hoy: ")

    if procesos not in [str(i) for i in range(1,10)]: #aqui estamos validando, si lo que preguntamos con "procesos" esta dentro del rango, el cual esta de 1 al 10 sin incluir a este ultimo numero y diciendo qque lo que traiga el iterador "i" sera un texto 
        print("Opción inválida.") #si no esta pues entonces se imprime este mensaje 
        continue

    if procesos == "1":
        Agregar_productos()
    elif procesos == "2":
        Buscar_producto()
    elif procesos == "3":
        actualizar()
    elif procesos =="4":
        eliminar_producto()
    elif procesos == "5":
        calcular_Estadistica ()
    elif procesos == "6":
        mostrar_listaActualizada(Inventario)
    elif procesos == "7":
        menu_guardar_csv (Inventario)
    elif procesos == "8":
        menu_cargar_csv(Inventario)  
        
    elif procesos == "9":
        print("Saliendo...")
        break
    else:
        print("\nERROR VALOR!!!, por favor vuelva a leer las opciones y dijite el numero correspondiente")
    