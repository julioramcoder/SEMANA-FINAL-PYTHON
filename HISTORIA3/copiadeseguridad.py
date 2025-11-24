# ==================================== LISTA DE INVENTARIO ============================================== #
Inventario = [
    {"nombre":"coco","precio":1500,"cantidad":345},
    {"nombre":"mango","precio":1200,"cantidad":24},
    {"nombre":"piña","precio":13450,"cantidad":145}
]
# ==================================== AGREGAR PRODUCTOS ============================================== #
def Agregar_productos ():
    salir = ""
    while True: 
        nombre = input("Por favor ingrese el nombre el prodcuto: ")
        precio = float(input("Por favor ingrese el precio del prodcuto: "))
        cantidad = int(input("Por favor ingrese la cantidad de producto: "))

        inventario = {
            "nombre" : nombre,
            "precio" : precio,
            "cantidad" :cantidad
        }
        Inventario.append(inventario)
        print(Inventario)
        
        salir = input("¿Deseas continuar dentro de esta opcion? si/no: ").lower()
        
        if salir == "si":
            continue
        elif salir == "no":
            break
        else:
            print("opcion invalida, vuleva a ingresar")

# ==================================== BUSCAR PRODUCTOS ============================================== #
def Buscar_producto ():
    found = False
    while True:
            nombre= input("por favor ingrese el nombre del producto que quiere validar stock: ")
            for p in Inventario:
                if p["nombre"] == nombre:
                    found=True
                    print(f"segun el stock si contamos con",nombre)
                else:
                    print("Actualmente no cuentas con disponibilida en stock")
                break
            
            salir = input("¿Deseas continuar en esta opcion? si/no: ").lower()
            if salir == "si":
                continue
            elif salir == "no":
                break
            else:
                print("opcion invalida, vuleva a ingresar")
            
# ==================================== MENU DE ACTUALIZAR PRODUCTOS ============================================== #
            
def miniMenuActualizar(p):
    while True:
        print("que informacion deseas actualizar el dia de hoy")
        print("1. actualizar precio")
        print("2. actualizar cantidad" )
        print("3. actualizar ambos valores")
        #salir=(input("para salir al menu principal ingrese out: ")).lower()
        opciones = input(" ingrese una opcion: ")
        if opciones == "1":
            nuevoValor = float(input("Por favor ingrese el nuevo precio: "))
            p["precio"] = nuevoValor
        elif opciones == "2":
            nuevaCantidad = int(input("Por favor ingrese la cantidad: "))
            p["cantidad"] = nuevaCantidad
        elif opciones == "3":
            valornuevo = float(input("Por favor ingrese el nuevo precio: "))
            p["precio"] = valornuevo
            cantidadnuevo= int(input("Por favor ingrese la cantidad: "))
            p["cantidad"] = cantidadnuevo
        print(f"nombre: {p['nombre']}")
        print(f"precio: {p['precio']}")
        print(f"cantidad : {p['cantidad']}")
        mostrar_listaActualizada()
        return 
    
# ==================================== ACTUALIZAR PRODUCTOS ============================================== #
def actualizar():
    while True: 
        nombre = input("Por favor ingresa el nombre del producto que deseas actualizar: ").lower()
        for p in Inventario:
            if p["nombre"] == nombre:
                print(f"nombre: {p['nombre']}")
                print(f"precio: {p['precio']}")
                print(f"cantidad : {p['cantidad']}")
                miniMenuActualizar(p)
                
        salir = input("¿Deseas continuar si/no: ").lower()
        if salir == "si":
            continue
        elif salir == "no":
            break
        else:
            print("opcion invalida, vuleva a ingresar")
            
# ==================================== ELIMINAR PRODUCTOS ============================================== #  
                
def eliminar_producto ():
    
    while True:
        nombre = input('escribe el nombre del producto que desea eliminar: ').lower()
        found = False
        producto = ""
        for p in Inventario:
            if p["nombre"] == nombre: 
                producto = p
                found = True
                break
            else:
                found = False

        if (found == True):
            print(f"El producto encontrado es : {nombre}\n")
            delete = input(f"\n Deseas eliminar este prodcuto llamado {nombre}? si/no: ").lower()
            if delete == "si":
                Inventario.remove(p) 
                print(f"El producto llamado {producto} ha sido eliminado")
            elif delete == "no":
                print("===El proceso de eliminacion fue cancelado===")
            else:
                print("ingresa un valor valido")
                
                
            salir = input("¿Deseas salir y regresar al menu principal? si/no: ").lower()
            if salir == "si":
                break
            elif salir == "no":
                    continue
            else:
                print("opcion invalida, vuleva a ingresar")
        else:
            
            print("Lo siento, el producto no se encontro")  
                    
# ==================================== UNIDADES TOTALES ============================== #

def unidades_totales ():
   
        cantidadTotal = 0
        for p in Inventario:
            print(f"\n{p["nombre"]} {p["cantidad"]}\n")
            cantidadTotal += p["cantidad"]
        print(f"\n La cantidad total de productos en su stock es: {cantidadTotal} productos")

# ==================================== CALCULO TOTAL POR PRODUCTOS ==================================== #
        
def calculo_totalPorProducto ():
    while True:
            nombre = input("Por favor ingresar el nombre del producto que quiere calcular cantidad total o out para salir:").lower()
            if nombre == "out":
                break
            found = False # lo que sea que vayamos a buscar no existe comenzamos negando su existencia 
            product = "" #aca estamos declarando una variable llamada product, vacia porque sera usada.
        
            # lo mas importante, validar la existencia de x cosa dentro de una lista, la cual sera iterada 
            for p in Inventario:
                if p["nombre"] == nombre: #en este caso con p como iterador
                    product = p #que nos traera p un valor, un valor GUARDADO en  en la varibale producto
                    found = True #como al comienzo negamos la exitencia ahora la confirmamos siempre y cuando se encuentre 
                else:
                    found = False
                
            if(found == True): # si en efecto se encuentra ya sera entonces nuestra primera supocicion deja de existir
                print(f"nombre: {product['nombre']}") #procedemos a imprimir cada uno de los valores deseados 
                print(f"precio: {product['precio']}")
                print(f"cantidad : {product['cantidad']}")
        
                total = product['precio'] * product['cantidad'] #se procede con el calculo
                print(f'Total: {total}')
                print(f'\n{product}\n')
                
            else: # ahora que pasa si en efecto no existe, pues se imprime que no existe
                print("Lo sentimos pero no encontramos dicho producto en stok")

# ==================================== CALCULO TOTAL DEL INVENTARIO ============================================== #
     
def calculo_Total():
    cantidadTotal = 0
    for p in Inventario:
        print(f" nombre:{p["nombre "]} cantidad: {p["cantidad"]} {p["precio"]}\n")
        cantidadTotal += p["precio"] * p["cantidad"]
    print(f"\n El precio total de todos los productos en su stock es: {cantidadTotal} de pesos colombianos")
    
# ==================================== PRODUCTO MAS CARO ============================================== #
def producto_MasCaro():
    producto_MasCaro = Inventario[0]
    for p in Inventario:
      if p["precio"] > producto_MasCaro["precio"]:
          producto_MasCaro = p
    print(f"El precio mas alto que tenemo en inventario es {p['precio']} pesos colombianosy es del producto {p["nombre"]}")
        
# ==================================== PRODUCTO DE MAYOR STOCK ============================================== #
def productoMayorStock ():
    productoDeMayorStock = 0
for p in Inventario:
    productoDeMayorStock = p
    if p["cantidad"] > productoDeMayorStock["cantidad"]:
        print(f"El producto con mayor stock es: {p['nombre']} y el numero de unidades disponibles e:  {p["cantidad"]}")
    
# ==================================== CALCULOS ESTADISTICOS ============================================== #
        
def calcular_Estadistica ():
    
     print ("======OPCIONES DE ESTADISTICAS======")
     print("1 Calcular Unidades Totales")
     print("2 Calcular Valor Total Por Producto")
     print("3 Calcular Valor Total Del Inventario")
     print("4 Producto Mas Caro")
     print("5 Producto Con Mayor Stock")
     
     while True: 
        opciones = input("\nPor favor selecciona que operacion requieres de la calculadora: ")
        if opciones == "1":
            unidades_totales()
        elif opciones == "2":
            calculo_totalPorProducto ()
        elif opciones == "3":  
            calculo_Total ()
        elif opciones == "4":
            producto_MasCaro()
        elif opciones == "5":
            productoMayorStock()
        else:
            print( "ERROR VALOR!!!, por favor vuelva a leer las opciones y dijite el numero correspondiente")
            
            
            
# ==================================== MOSTRAR LISTA ACTUALIZADA  ============================================== #
        
def mostrar_listaActualizada (Inventario):
    print("Nombre | Precio | Cantidad")
    for p in Inventario:
        print(f"{p["nombre"]} {p["precio"]} {p["cantidad"]}")
        
# ==================================== MENU PRINCIPAL ============================================== #
     
while True:
    print("\n que quieres hacer hoy?, selecciona las siguientes opciones\n")

    print("1. agregar productos")
    print("2. buscar  productos")
    print("3. actualizar producto")
    print("4. eliminar productos")
    print("5. calculo estadistico")
    print("6. mostrar inventario actual\n")

    procesos = input ("por favor ingresa el numero de la actividad que quieres hacer hoy: ")

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
    else:
            print("\nERROR VALOR!!!, por favor vuelva a leer las opciones y dijite el numero correspondiente")