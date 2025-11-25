
# =================================== IMPORTS ==========================================#

import json #TREAMOS EL MODULO JSON DE PYTHON QUE NOS PERMITE CONVERTIR LOS DATOS DE JSON A ALGO LEGIBLE PARA PYTHON 
from datetime import datetime # ESTE MODULO NOS PERMITE TRABAJAR CON FECHAS Y HORAS NOS DEJA TRABJAR CON ESE FORMATO 


#=============================== DATOS INICALES  =================================#
productos = [
    {"nombreProducto":"Laptop Aspire 5","marca": "Acer","categoria": "Computadores","precioUnitario":649.99,"cantidadStock":18,"garantiaMeses": 12 },
    {"nombreProducto": "Smartphone Galaxy A55","marca": "Samsung","categoria": "Celulares","precioUnitario":399.00,"cantidadStock":24,"garantiaMeses":12  },
    {"nombreProducto": "Audífonos WH-CH720N","marca": "Sony","categoria": "Audio","precioUnitario":129.50,"cantidadStock":45,"garantiaMeses": 23 },
    {"nombreProducto": "Smart TV 55” UHD","marca": "LG","categoria": "Televisores","precioUnitario":579.99,"cantidadStock":12,"garantiaMeses": 6 },
    {"nombreProducto": "Consola Nintendo Switch OLED","marca": "Nintendo","categoria": "Videojuegos","precioUnitario":349.99,"cantidadStock":42,"garantiaMeses": 10 }
    ]
VENTAS_FILE = "ventas.json" #declaramos que toda la informacion del archivo.json va a ventas file 
RegistroVentas = []

#============================== JSON (CARGAR // GUARDAR) ==================================#

#DEBEMOS CREAR UNA FUNCION PARA COMENZAR

VENTAS_FILE = "ventas.json"

def cargar_ventas_json(): 
    
    try: #USAREMOS TRY PARA EVITAR QUE EL CODIGO SE ROMPA SI HAY ARCHIVOS 
        with open (VENTAS_FILE, "r", encoding="utf-8") as f: #AQUI YA LA SABEMOS PEDIMOS ABRIR EL ARCHIVO VENTAS JSON EN MODO LECTURA COMO UN ARCHIVO LEJIBLE PARA PYTHON 
            ventas = json.load(f) #LO QUE HACEMOS ES LEER CON JSONLOAD EL CONTENDIO DEL ARCHVIO F Y GUARDARLOS EN UNA LISTA LLAMADA VENTAS 
            return ventas #Y LO MOSTRAMOS 
    except FileNotFoundError: #DADO EL CASO EL ARCHIVO JSON QUE SE ESTA INTENTANTO ABRIR NO SIRVA ENTONCES SE GENERA ESTA ALARTE 
        return[]   #DEVOLVEMOS UN DICCIONARIO VACIO PARA QUE NO SE ROMPA EL CODIGO 
    
RegistroVentas = cargar_ventas_json() #Aqui decimos los datos que hayas sacado de .json guardalos en mi lista de registro de ventas 
   

#AHORA VAMOS A CREAR UNA FUNCION PARA GUARDAR Y ESCIRBIR EN ARCHIVOS JSON, ASI VAMOS ACTUALIZANDO EL HISTORIAL 
def guardar_en_json(VENTAS_FILE, RegistroVentas):
    try:
        with open (VENTAS_FILE, "w", encoding="utf-8") as f:
            json.dump(RegistroVentas, f, indent = 4, ensure_ascii= False) # JSON.DUMP BASICAMENTE SE USA PARA CONVERTIR INFORMACION TIPO PYTHON A FORMATO LEGFIBLE EN JSON PORQUE YA ESTAMOS GUARDANDO LA INFORMACION DE NUEVO EN JSON 
            #QUE SUCEDE, ENTRE LOS PARENTECIS DEBEMOS PONER EL NOMBRE DE LA LISTA DE DONDE SACAREMOS LA INFORMACION  QUE SE VA A GAURDAR EN (F) QUE SERIA EL ARCHIVO QUE CONVERTIMOS ANTERIORMENTE PARA ESCRIBIR 
            # INDENT=4 ES PARA QUE SE VEA MAS BONITO
            #ENSURE_ASCII ES PARA QUE LOS CARACTERES ESPECIALES SE LEAN TAN CUAL SON.
    except:
        print("Error guardando el archivo json")

#=================================== INVENTARIO =========================================#

def GestionDeInventario():
    while True:
        print ("\n================ GESTION DE INVENTARIO ============\n")
        print("A continuacion podra gestionar el ingreso de los datos requeridos para un buen sistema de inventariado\n")

        nombreProducto = validar_entrada_texto("Porfavor ingrese el nombre del prducto: ")
        marca= validar_entrada_texto("Por favor ingrese la marca del producto:  ")
        categoria = validar_entrada_texto("Por favor ingrese la categoria del producto: ")
        
        
            
            
        while True:
            try:
                precioUnitario = float(input("Por favor ingrese el precio del producto: "))
                if precioUnitario <= 0:
                    print("El precio debe ser mayor que 0")
                    continue
                break
            except:
                print("Eso no es numero valido, intenta otra vez")
                    
        while True:
            try:
                cantidadStock = int(input("Por favor ingrese the quantity on stock: "))
                if cantidadStock <= 0:
                    print("El valor ingresado debe ser mayor a cero")
                    continue
                break
            except:
                print("Eso no es numero valido, intente nuevamente")
                    
        while True: 
            try: 
                garantiaMeses = int(input("Por favor ingrese la garantia del producto: "))
                if garantiaMeses <=0:
                    print("Eso no es numero valido, intente nuevamente")
                    continue
                break
            except:
                print("Eso no es numero valido, intente nuevamente")
                    
        inventario = {

                "nombreProducto" : nombreProducto,
                "marca" : marca,
                "categoria" : categoria,
                "precioUnitario" : precioUnitario,
                "cantidadStock" : cantidadStock,
                "garantiaMeses" : garantiaMeses
            }
            
        productos.append(inventario)
        print(f"producto agregado a:",inventario)
            
        salir = input("Deseas continuaringresando informacion a la lista? (si/no)").lower()
        if salir == "si":
            continue
        else:
            break
#--------------------------------------------------------------------------------------------
def mostrar_inventario():
    print("\n========== INVENTARIO ACTUAL ==========\n")

    if len(productos) == 0:
        print("No hay productos en inventario.")
        return

    for p in productos:
        print("----------------------------")
        print(f"Nombre: {p['nombreProducto']}")
        print(f"Marca: {p['marca']}")
        print(f"Categoria: {p['categoria']}")
        print(f"Precio: {p['precioUnitario']}")
        print(f"Stock: {p['cantidadStock']}")
        print(f"Garantia (meses): {p['garantiaMeses']}")
        print() # ESTO ES PARA DEJAR UN ESPACIO AL FINAL DE ESTA INFORMACION 
#-------------------------------------------------------------------------------------------
def actualizar_producto():
    print("\n========== ACTUALIZAR PRODUCTO ==========\n")
    nombre_buscar = input("Nombre del producto a actualizar: ").lower()

    for p in productos:
        if p["nombreProducto"].lower() == nombre_buscar:

            print("\nProducto encontrado:")
            print(p)

            print("\n¿Que deseas actualizar?")
            print("1. Precio")
            print("2. Stock")
            print("3. Garantia")
            opcion = input("Elige una opcion: ")

            if opcion == "1":
                nuevo_precio = float(input("Nuevo precio: "))
                p["precioUnitario"] = nuevo_precio

            elif opcion == "2":
                nuevo_stock = int(input("Nuevo stock: "))
                p["cantidadStock"] = nuevo_stock

            elif opcion == "3":
                nueva_garantia = int(input("Nueva garantia en meses: "))
                p["garantiaMeses"] = nueva_garantia

            else:
                print("Opcion invalida.")
                return

            print("\nProducto actualizado:")
            print(p)
            return

    print("Producto no encontrado.")
#--------------------------------------------------------------------------------------------
def eliminar_producto():
    print("\n========== ELIMINAR PRODUCTO ==========\n")
    nombre_buscar = input("Nombre del producto a eliminar: ").lower()

    for p in productos:
        if p["nombreProducto"].lower() == nombre_buscar:
            productos.remove(p)
            print("Producto eliminado correctamente.")
            return

    print("Producto no encontrado.")
#--------------------------------------------------------------------------------------------
def modulo_inventario():
    while True:
        print("\n=========== MODULO INVENTARIO ===========")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Volver al menu principal")

        op = input("Elige una opcion: ").strip()

        if op == "1":
            GestionDeInventario()
        elif op == "2":
            mostrar_inventario()
        elif op == "3":
            actualizar_producto()
        elif op == "4":
            eliminar_producto()
        elif op == "5":
            break
        else:
            print("Opcion invalida.")
#--------------------------------------------------------------------------------------------

# Para validar la disponibilidad del stock primero es neesario ver que producto quieres validar por ende 

def validarStock (): 
    while True:
        nombre = input("Por favor ingrese el nombre del producto al cual quiere validarle la disponibilidad: ")
        for p in productos: 
            if p["nombreProducto"] == nombre:
                print(f"la disponibilidad del producto en stock es de: {p['cantidadStock']}")
                break
            else:
                print("Lo sentimos, pero no tenemos disponibilidad de ese elemento en el stock")
        salir = input("¿Deseas continuar en esta opcion? si/no: ").lower()
            
        if salir == "si":
            continue
            
        elif salir == "no":
            break
            
        else:
            print("opcion invalida, vuelva a ingresar")     
                
#============================================ VENTAS ==================================================#
def RegistroAndConsulta ():  
    while True:
        print ("\n================ REGISTRO Y CONSULTA DE VENTAS ============\n")
        print("A continuacion podra gestionar el ingreso de los datos requeridos para un buen registro y consulta de ventas\n")
        cliente = input("Por favor ingrese el nombre del cliente: ")
        tipodecliente= input("Por favor ingrese el tipo de cliente: ")
        productoVendido = input("Por favor ingrese el nombre del producto: ")
        
        producto_encontrado = validar_producto_valido(productoVendido)
        if producto_encontrado is None:
            continue 
        
        while True:
            try:
                cantidadVendida= int(input("Por favor ingrese la cantidad de productos vendidos: "))
                if cantidadVendida <= 0:
                    print("El valor debe ser mayor que 0")
                    continue
                break
            except:
                print("Eso no es numero valido, intenta otra vez")
                    
        while True:
            try:
                fechaDeVenta= input("Por favor ingrese la fecha (dd/mm/yyyy): ")
                fechaDeVenta = datetime.strptime(fechaDeVenta, "%d/%m/%Y")
                fechaDeVenta_str = fechaDeVenta.strftime("%d/%m/%Y") #LO CONVERTIMOS A TEXTO PARA PODER GUARDARLO
                break  # si llego aqui es porque la fecha existe y esta bien escrita
            except:
                print("Eso no es una fecha valida, intente nuevamente")
                
        while True: 
            try: 
                descuentoAplicado= float(input("Por favor ingrese el valor del descuento aplicado: "))
                if descuentoAplicado < 0 or descuentoAplicado > 100:
                    print("descuento invalido, debe estar entre 0 y 100")
                    continue
                break
            except:
                print("eso no es numero valido, intente nuevamente")
                    
#Actualizacion de nuestro registro de ventas y de nuestro inventario para eso debemos validar si existe inventario para esa venta

        for p in productos:
            if p["nombreProducto"] == productoVendido.lower():
                if p["cantidadStock"] >= cantidadVendida:
                    p["cantidadStock"] -= cantidadVendida
                else:
                    print("Lo siento no hay disponibilidad del producto")
                    break
                             
        Registro = {
                
            "cliente": cliente,
            "tipodecliente": tipodecliente,
            "productoVendido": productoVendido,
            "cantidadVendida": cantidadVendida,
            "fechaDeVenta":fechaDeVenta_str,
            "descuentoAplicado":descuentoAplicado
            }
            
        RegistroVentas.append(Registro)
        print(RegistroVentas)
            
        salir = input("Deseas continuaringresando informacion a la lista? (si/no)").lower()
        if salir == "si":
            continue
        else:
            break
#------------------------------------------------------------------------------------------------------------------
       
def mostrar_historial_ventas(): #CREAMOS UNA FUNCION LLAMADA HISTORIAL DE VENTAS
    
    ventas = cargar_ventas_json() # QUE PASA AQUI? COMO YA CON LA FUNCION CARGAR VENTAS JSON HEMOS EXTRAIDO LA INFORMACION QUE TENIA DICHO ARCHIVO LO QUE VAMOS A HACER ES 
    #EXTRAERLA Y LA VAMOS A GUARDAR EN VENTAS PARA QUE ASI SEA MAS COMODO MOVERNOS DENTRO DE LA INFORMACION.
    
    print("\n========================= HISTORIAL DE VENTAS ==========================\n")
    
#LO PRIMERO QUE DEBEMOS HACER ES VALIDAR QUE EL ARCHIVO TENGA INFORMACION, PORQUE SI NO TIENE, PUES NADA SE MOSTRARA, ENTONCES
    if len(ventas)==0:
        print("Aun no tenemos registro de ventas")
        return

    for p in ventas: 
        
        print("---------------------VENTA------------------")
        print(F"Cliente:{p['cliente']}")
        print(F"Tipo de cliente:{p['tipodecliente']}")
        print(F"Producto vendido:{p['productoVendido']}")
        print(F"Cantidad vendida:{p['cantidadVendida']}")
        print(F"Fecha de venta:{p['fechaDeVenta']}")
        print(F"Descuento aplicado:{p['descuentoAplicado']}")
        print()
        
#EN EL CASO QUE SI TENGAMOS INFORMACION DENTRO DEL ARCHIVO ENTONCES COMENZAMOS A ITERAR

#AHORA VAMOS A CREAR UNA FUNCION QUE RECOJA TODAS LAS FUNCIONES QUE NECESITAMOS PARA TRABJAR EN ESTA PARTE 

def modulo_ventas ():
    global RegistroVentas
    RegistroVentas = cargar_ventas_json()  # cargamos historial viejo en la lista real
    while True:
        print("=========== MODULO DE VENTAS ===========")
        print("1. Registrar una venta")
        print("2. Ver historial de ventas")
        print("3. Salir, volver al menu principal")

        opciones = input("Ecoja una de las opciones anteriores ").strip()
        
        if opciones =="1":
            RegistroAndConsulta()
            
            guardar_en_json(VENTAS_FILE,RegistroVentas)
        elif opciones == "2":
            mostrar_historial_ventas()
        elif opciones == "3":
            break
        else:
            print("La opcion dijistada no es valida, vuelve a ingresarla ")
            
#=========================================== REPORTES =============================================#

#VAMOS A CREAR UNA FUNCION PARA VALIDAR LOS 3 PRODUCTOS MAS VENDIDOS 

def top_3_mas_vendidos ():
    #LLAMAMOS A LA FUNCION QUE ES CAPAZ DE SUMINISTRARNOS TODA LA INFORMACION DEL HISTORIAL Y ESA ES CARGAR VENTAS JSON QUIEN ES LA FUNCION QUE TRADUCE LOS ARCHIVOS JSON    
    ventas = cargar_ventas_json()
    
    
    print("\n=========================TOP 3 DE PRODUCTOS MAS VENDIDOS================================\n")
    
    #DEBEMOS VALIDAR QUE SI EXISTAN ARCHIVOS DENTRO DE MI LISTA DE ARCHIVO EXTRAIDO DE JSON
    if len(ventas) == 0:
        print("No existen ventas registradas actualmente, se van a ir a quiebra")
        return
    
    #COMO LAS ESPERANZAS DE QUE SI HAYAN VENTAS NO SE HAN PERDIDO ENTONCES, SOMOS OPTIMISTAS Y CREAMOS UN DICCIONARIO VACIO 
    totales ={}
    
    #VAMOS A COMENZAR A ITERAR TODAS LA VENTAS QUE HEMOS TENIDO, LAS VAMOS A SACAR DE CARGAR VENTAS JSON Y PARA SER MAS ESPECIFICOS SI QUEREMOS SABER CUAL PRODUCTO FUE EL QUE SE VENDIO MAS, CLARAMENTE NECESITAMOS UNICANTE EL NOMBRE DEL PRODUCTO Y LA CANTIDAD 
    for v in ventas:
        producto = v["productoVendido"]
        cantidad = v["cantidadVendida"]
    #CON PYTHON PASA ALGO CURIOSO Y ES QUE UNA VEZ QUE COMIENZA A ITERAR NO SE DETIENE, ME REFIERO A QUE PASARA POR TODOS LOS DICCIONARIOS BUSCANDO UN NOMBRE EN ESPECIFICO, Y SI NO LO ENCUENTRA PUEDE QUE SE VUELVA LOCO POR ENDE VAMOS A ENGAÑARLO 
    # BASICAMENTE CREAMOS UN FALSO PRODUCTO DICIENDO QUE SI 
    
        if producto not in totales:
            totales[producto] = 0 #ASI PYTHON CREERA QUE SIMPLEMNTE NO HAY VENTAS DE UN PRODUCTO Y NO QUE NO EXSISTE EN ESE DICCIONARIO EN ESPECIFICO 
        
        
        totales[producto] += cantidad #AQUI BASICAMENTE DECIMOS, HEY SI TENEMOS UN PRODUCTO X, BUSCALO EN TOTOALES Y SUMALE LA CANTIDAD DE ESA VENTA 
    #CADA VEZ QUE HACES UNA VENTA EL REGISTRO DEL VALOR QUE GAANSTE DE ESA VENTA SOLO IRA AL NOMBRE DEL PRODUCTO VENDIDO
    
    #AHORA DEBEMOS ORGANIZAR LOS VALORES QUE HEMOS FILTRADO SOLAMENTE Y SON PRODUCTO Y CANTIDAD
    ordenados = sorted(totales.items(), key = lambda x: x[1], reverse = True)
    #AQUI, TOTALES ES EL DICCIONARIO QUE YA TENEMOS, CUANDO LE AGG EL .ITEMS ES COMO UNA ORDEN, Y ES CONVIERTE EL DICCIONARIO EN UNA TUPLA ("PRODUCTO",VALOR)
    #SORTED DA LA ORDEN DE ORDENAR UNA LISTA, PERO NECESITA SABER COMO LA VAMOS A ORDENAR Y ES AHI CUANDO ENTRA
    #KEY = LAMBDA X: X[1]
    # AQUI X SERIA LA TUPLA, LA PAREJA DE PRODUCTO Y VALOR 
    # Y SI LO MIRAMOS MAS A FONDO X0 SERIA EL PRODUCTO Y X1 EL VALOR 
    # AHORA TODO JUNTO SIGNIFICA, ORDENA LOS TOTALES USANDO EL VALOR DEL NUMERO COMO REFERENCIA 
    # Y REVERSE = true ES SI VAMOS A ORDENARLOS POR VALORES PERO SOLO DE MAYOR A MENOR 
    
    Top3 = ordenados[:3] #Aqui damos la orden de tomar los 3 primeros valores 
    
    for prod, total in Top3: #AQUI BASICAMENTE DECIMOS SACA LA INFORMACION DEL TOP 3 E IMPRIMEMELO 
        print(prod, "->", total, "unidades vendidas")
        
        
#---------------------------------------------------------------------------------------------------------------------------------  

def ventas_por_marcas(): 
    ventas = cargar_ventas_json()
#VALIDAMOS QUE LAS VENTAS NO EXISTAN 
    if len (ventas) == 0: 
        print("NO HAY VENTAS REGISTRADAS")
        return

    totales_marcas = {}
#EXTRAEMOS CON FOR DATOS RELEVANTES COMO EL NOMBRE DEL PRODUCTO Y LA CANTIDAD VENDIDA 
    for v in ventas: 
        producto = v["productoVendido"]
        cantidad = v["cantidadVendida"]

        marca_encontrada = None
    
        for p in productos: 
            if p["nombreProducto"].lower()== producto.lower():
                marca_encontrada = p["marca"]
                break
            
        if marca_encontrada is None:
            continue
            
        if marca_encontrada not in totales_marcas:
                totales_marcas[marca_encontrada] = 0 
    
        totales_marcas[marca_encontrada] += cantidad
    print("\n============= VENTAS AGRUPADAS POR MARCA ============\n")
    for marca, total in totales_marcas.items():
        print(f"{marca}->{total} unidades vendidas")
#------------------------------------------------------------------------------------------------------------------

def ingresos_bruto_y_neto():
    ventas = cargar_ventas_json()

    if len(ventas) == 0:
        print("No hay ventas registradas.")
        return

    ingreso_bruto = 0
    ingreso_neto = 0

    for v in ventas:
        producto = v["productoVendido"]
        cantidad = v["cantidadVendida"]
        descuento = v["descuentoAplicado"]  # porcentaje

        # buscar precio en inventario
        precio = None
        for p in productos:
            if p["nombreProducto"].lower() == producto.lower():
                precio = p["precioUnitario"]
                break

        if precio is None:
            continue  # si no hay precio, no se puede calcular

        bruto_venta = precio * cantidad
        neto_venta = bruto_venta * (1 - descuento / 100)

        ingreso_bruto += bruto_venta
        ingreso_neto += neto_venta

    print("\n===== INGRESOS =====\n")
    print(f"Ingreso bruto total: {ingreso_bruto}")
    print(f"Ingreso neto total: {ingreso_neto}")  

#-------------------------------------------------------------------------------------------------------------------

def rendimiento_inventario():
    ventas = cargar_ventas_json()

    # 1) sumar vendido total por producto (como en top3)
    vendido_por_producto = {}
    for v in ventas:
        producto = v["productoVendido"]
        cantidad = v["cantidadVendida"]

        if producto not in vendido_por_producto:
            vendido_por_producto[producto] = 0

        vendido_por_producto[producto] += cantidad

    print("\n===== RENDIMIENTO DEL INVENTARIO =====\n")

    # 2) recorrer inventario y mostrar rendimiento
    for p in productos:
        nombre = p["nombreProducto"]
        stock = p["cantidadStock"]

        vendido = vendido_por_producto.get(nombre, 0)

        total_inicial = vendido + stock  # lo que había antes de vender

        if total_inicial == 0:
            porcentaje = 0
        else:
            porcentaje = (vendido / total_inicial) * 100

        print(f"Producto: {nombre}")
        print(f"  Vendido total: {vendido}")
        print(f"  Stock actual: {stock}")
        print(f"  % vendido: {porcentaje:.2f}%")
        print()   
#-------------------------------------------------------------------------------------------------
def modulo_reportes():
    while True:
        print("\n=========== MODULO DE REPORTES ===========")
        print("1. Top 3 productos mas vendidos")
        print("2. Ventas agrupadas por marca")
        print("3. Ingreso bruto y neto")
        print("4. Rendimiento del inventario")
        print("5. Volver al menu principal")

        op = input("Elige una opcion: ").strip()

        if op == "1":
            top_3_mas_vendidos()
        elif op == "2":
            ventas_por_marcas()
        elif op == "3":
            ingresos_bruto_y_neto()
        elif op == "4":
            rendimiento_inventario()
        elif op == "5":
            break
        else:
            print("Opcion invalida.")
#================================= VALIDACION DE ENTRADAS DE USUARIOS =============================

def validar_entrada_texto(mensaje):
    """
    Esta función sirve para pedir un texto al usuario
    y asegurarse de que no esté vacío.

    Si está vacío, no deja avanzar y vuelve a preguntar.
    """
    while True:
        texto = input(mensaje).strip()  # quitamos espacios antes y después

        if texto == "":
            print("No puede estar vacío. Intenta otra vez.")
            # vuelve al inicio del while y pregunta otra vez
        else:
            return texto  # texto correcto, salimos de la función
#------------------------------------------------------------------------------------------------------------
def manejar_error_numero(mensaje, tipo, minimo, maximo=None):
    """
    Esta función pide un número y evita que el programa se rompa.

    - tipo: int o float
    - minimo: valor mínimo permitido
    - maximo: valor máximo permitido (opcional)
    """
    while True:
        try:
            numero = tipo(input(mensaje))

            # Validar mínimo
            if numero < minimo:
                print(f"Debe ser mayor o igual a {minimo}.")
                continue

            # Validar máximo si existe
            if maximo is not None and numero > maximo:
                print(f"Debe ser menor o igual a {maximo}.")
                continue

            return numero  # número válido

        except:
            print("Eso no es un número válido. Intenta otra vez.")
            # vuelve al inicio sin cerrar el programa
            
#-----------------------------------------------------------------------------------------------------------------------
def validar_producto_valido(productoVendido):
    """
    Esta función busca un producto dentro de la lista 'productos'.

    - Si lo encuentra, devuelve el diccionario del producto.
    - Si NO lo encuentra, devuelve None.
    """
    productoVendido = productoVendido.lower()

    for p in productos:
        if p["nombreProducto"].lower() == productoVendido:
            return p  #producto encontrado

    print("Ese producto NO existe en inventario.")
    return None  # producto no encontrado                    

#---------------------------------------------------------------------------------------------------------------------------

def validar_stock_suficiente(producto_encontrado, cantidadVendida):
    """
    Esta función revisa si hay stock suficiente
    antes de hacer una venta.

    Si NO hay stock, devuelve False.
    Si SÍ hay stock, devuelve True.
    """
    stock_actual = producto_encontrado["cantidadStock"]

    if stock_actual < cantidadVendida:
        print("No hay suficiente stock para esa venta.")
        print(f"Stock disponible: {stock_actual}")
        return False  # no se puede vender

    return True  # sí se puede vender


