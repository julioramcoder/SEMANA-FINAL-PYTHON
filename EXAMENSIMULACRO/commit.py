# =============================== ARQUITECTURA GENERAL (resumen rápido) =============================== #
# - productos: lista principal del inventario (TODO lo que existe).
# - RegistroVentas: lista en memoria temporal de ventas (mientras la app corre).
# - ventas.json: historial permanente (lo usas para reportes y para no perder ventas).
#
# Flujo al registrar una venta:
# 1) Validar que el producto exista en inventario (validar_producto_valido).
# 2) Validar que haya stock suficiente (validar_stock_suficiente).
# 3) Descontar stock del producto vendido.
# 4) Guardar venta en RegistroVentas.
# 5) Guardar RegistroVentas en ventas.json (guardar_en_json).
#
# Flujo de reportes:
# 1) Leer ventas.json (cargar_ventas_json).
# 2) Armar diccionarios con acumulados (por producto / marca).
# 3) Ordenar si hace falta y mostrar resultados.
# ===================================================================================================== #


# =============================== INVENTARIO ================================= #
productos = [
    {"nombreProducto":"Laptop Aspire 5","marca": "Acer","categoria": "Computadores","precioUnitario":649.99,"cantidadStock":18,"garantiaMeses": 12 },
    {"nombreProducto": "Smartphone Galaxy A55","marca": "Samsung","categoria": "Celulares","precioUnitario":399.00,"cantidadStock":24,"garantiaMeses":12  },
    {"nombreProducto": "Audífonos WH-CH720N","marca": "Sony","categoria": "Audio","precioUnitario":129.50,"cantidadStock":45,"garantiaMeses": 23 },
    {"nombreProducto": "Smart TV 55” UHD","marca": "LG","categoria": "Televisores","precioUnitario":579.99,"cantidadStock":12,"garantiaMeses": 6 },
    {"nombreProducto": "Consola Nintendo Switch OLED","marca": "Nintendo","categoria": "Videojuegos","precioUnitario":349.99,"cantidadStock":42,"garantiaMeses": 10 }
]

# Aquí se guardan ventas en memoria mientras el programa está abierto
RegistroVentas = []

from datetime import datetime
import json

VENTAS_FILE = "ventas.json"


def GestionDeInventario():
    # Agrega productos nuevos a la lista "productos".
    while True:
        print ("\n================ GESTION DE INVENTARIO ============\n")
        print("A continuacion podra gestionar el ingreso de los datos requeridos para un buen sistema de inventariado\n")

        # .lower() se usa para normalizar texto (todo minúscula)
        # y evitar fallos después al comparar nombres.
        nombreProducto = input("Por favor ingrese el nombre del producto: ").lower()
        marca = input("Por favor ingrese la marca del producto: ").lower()
        categoria = input("Por favor ingrese la categoria del producto: ").lower()

        # Validación de precio: debe ser número y > 0
        while True:
            try:
                precioUnitario = float(input("Por favor ingrese el precio del producto: "))
                if precioUnitario <= 0:
                    print("El precio debe ser mayor que 0")
                    continue
                break
            except:
                print("Eso no es numero valido, intenta otra vez")

        # Validación de stock: debe ser entero y > 0
        while True:
            try:
                cantidadStock = int(input("Por favor ingrese the quantity on stock: "))
                if cantidadStock <= 0:
                    print("El valor ingresado debe ser mayor a cero")
                    continue
                break
            except:
                print("Eso no es numero valido, intente nuevamente")

        # Validación de garantía: entero y > 0
        while True:
            try:
                garantiaMeses = int(input("Por favor ingrese la garantia del producto: "))
                if garantiaMeses <=0:
                    print("Eso no es numero valido, intente nuevamente")
                    continue
                break
            except:
                print("Eso no es numero valido, intente nuevamente")

        # Diccionario estándar de producto para guardar en inventario
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
    # Imprime inventario completo.
    print("\n========== INVENTARIO ACTUAL ==========\n")

    if len(productos) == 0:
        print("No hay productos en inventario.")
        return

    # Recorre productos y muestra cada uno
    for p in productos:
        print("----------------------------")
        print(f"Nombre: {p['nombreProducto']}")
        print(f"Marca: {p['marca']}")
        print(f"Categoria: {p['categoria']}")
        print(f"Precio: {p['precioUnitario']}")
        print(f"Stock: {p['cantidadStock']}")
        print(f"Garantia (meses): {p['garantiaMeses']}")
        print()  # espacio visual para separar productos


#-------------------------------------------------------------------------------------------
def actualizar_producto():
    # Permite editar un producto existente.
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
    # Borra un producto del inventario.
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
    # Menú de inventario.
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
def validarStock (): 
    # Consulta stock de un producto específico.
    while True:
        nombre = input("Por favor ingrese el nombre del producto al cual quiere validarle la disponibilidad: ")

        for p in productos: 
            if p["nombreProducto"].lower() == nombre.lower():
                print(f"la disponibilidad del producto en stock es de: {p['cantidadStock']}")
                break
        else:
            # Este "else" pertenece al for:
            # solo corre si NO se encontró producto (o sea, nunca hubo break).
            print("Lo sentimos, pero no tenemos ese producto en el stock")

        salir = input("¿Deseas continuar en esta opcion? si/no: ").lower()

        if salir == "si":
            continue
        elif salir == "no":
            break
        else:
            print("opcion invalida, vuelva a ingresar")   


#============================================ JSON / HISTORIAL ============================================#

def cargar_ventas_json(): 
    # Lee ventas.json y devuelve lista de ventas.
    try:
        with open (VENTAS_FILE, "r", encoding="utf-8") as f:
            ventas = json.load(f)
            # json.load(...) convierte el contenido del archivo JSON
            # en una lista de diccionarios de Python.
            return ventas
    except FileNotFoundError:
        # Si el archivo no existe, devolvemos lista vacía
        # para que la app no se caiga.
        return[]  


def guardar_en_json(VENTAS_FILE, RegistroVentas):
    # Guarda RegistroVentas dentro de ventas.json.
    try:
        with open (VENTAS_FILE, "w", encoding="utf-8") as f:
            json.dump(RegistroVentas, f, indent = 4, ensure_ascii= False)
            # indent=4: deja el JSON bonito, fácil de leer.
            # ensure_ascii=False: permite tildes sin convertirlas a códigos raros.
    except:
        print("Error guardando el archivo json")


#=============================== HISTORIAL DE VENTAS ===================================#

def mostrar_historial_ventas():
    # Muestra todas las ventas ya guardadas en JSON.
    ventas = cargar_ventas_json()

    print("\n========================= HISTORIAL DE VENTAS ==========================\n")

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
        print(F"Descuento aplicado:{p['descuentoAplicado']}%")
        print()


#============================================ VENTAS ==================================================#

def RegistroAndConsulta ():  
    # Registra una venta y actualiza inventario + historial.
    while True:
        print ("\n================ REGISTRO Y CONSULTA DE VENTAS ============\n")
        print("A continuacion podra gestionar el ingreso de los datos requeridos para un buen registro y consulta de ventas\n")

        cliente = validar_entrada_texto("Por favor ingrese el nombre del cliente: ")
        tipodecliente= validar_entrada_texto("Por favor ingrese el tipo de cliente: ")
        productoVendido = validar_entrada_texto("Por favor ingrese el nombre del producto: ")

        # 1) Validar que el producto exista en inventario.
        producto_encontrado = validar_producto_valido(productoVendido)
        if producto_encontrado is None:
            # None aquí significa “no encontrado”.
            # Si no hay producto real, no se registra venta.
            continue 

        # 2) Pedir cantidad vendida con rango válido.
        cantidadVendida = manejar_error_numero(
            "Por favor ingrese la cantidad de productos vendidos: ",
            int, 1
        )

        # 3) Validar stock suficiente.
        if not validar_stock_suficiente(producto_encontrado, cantidadVendida):
            continue

        # 4) Descontar stock real del inventario.
        producto_encontrado["cantidadStock"] -= cantidadVendida

        # 5) Pedir fecha y guardarla como texto (JSON no guarda datetime).
        while True:
            try:
                fechaDeVenta= input("Por favor ingrese la fecha (dd/mm/yyyy): ")
                fechaDeVenta = datetime.strptime(fechaDeVenta, "%d/%m/%Y")
                fechaDeVenta_str = fechaDeVenta.strftime("%d/%m/%Y")
                # strftime(...) convierte la fecha a texto tipo "20/11/2025"
                # para poder guardarla en JSON sin error.
                break
            except:
                print("Eso no es una fecha valida, intente nuevamente")

        # 6) Pedir descuento con rango 0-100.
        descuentoAplicado= manejar_error_numero(
            "Por favor ingrese el valor del descuento aplicado (0-100): ",
            float, 0, 100
        )

        # 7) Construir diccionario de venta con claves fijas.
        Registro = {
            "cliente": cliente,
            "tipodecliente": tipodecliente,
            "productoVendido": productoVendido,
            "cantidadVendida": cantidadVendida,
            "fechaDeVenta":fechaDeVenta_str,
            "descuentoAplicado":descuentoAplicado
        }

        RegistroVentas.append(Registro)
        print("Venta registrada:", Registro)

        salir = input("Deseas continuaringresando informacion a la lista? (si/no)").lower()
        if salir == "si":
            continue
        else:
            break


def modulo_ventas ():
    # Antes de empezar a vender, cargamos el historial viejo a RegistroVentas,
    # así no se pierde lo anterior.
    global RegistroVentas
    RegistroVentas = cargar_ventas_json()

    while True:
        print("=========== MODULO DE VENTAS ===========")
        print("1. Registrar una venta")
        print("2. Ver historial de ventas")
        print("3. Salir, volver al menu principal")

        opciones = input("Ecoja una de las opciones anteriores ").strip()
        
        if opciones =="1":
            RegistroAndConsulta()
            guardar_en_json(VENTAS_FILE,RegistroVentas)
            # guardamos al salir de registrar ventas para dejar histórico actualizado.
        elif opciones == "2":
            mostrar_historial_ventas()
        elif opciones == "3":
            break
        else:
            print("La opcion dijistada no es valida, vuelve a ingresarla ")


#=========================================== REPORTES =============================================#

def top_3_mas_vendidos ():
    # Calcula el top 3 usando el historial real (JSON).
    ventas = cargar_ventas_json()
    
    print("\n=========================TOP 3 DE PRODUCTOS MAS VENDIDOS================================\n")
    
    if len(ventas) == 0:
        print("No existen ventas registradas actualmente")
        return

    totales ={}
    # totales será un diccionario así:
    # {"Laptop Aspire 5": 10, "Smart TV 55” UHD": 2, ...}
    # donde cada valor es la suma de unidades vendidas.

    for v in ventas:
        producto = v["productoVendido"]
        cantidad = v["cantidadVendida"]
    
        if producto not in totales:
            totales[producto] = 0
        
        totales[producto] += cantidad

    ordenados = sorted(
        totales.items(),
        key = lambda x: x[1],
        # totales.items() convierte el diccionario en lista de pares:
        # [("Laptop Aspire 5", 10), ("Smart TV 55” UHD", 2), ...]
        # y el lambda x: x[1] le dice que ordene usando la cantidad vendida.
        reverse = True
        # reverse=True para que quede de mayor a menor (más vendido primero).
    )
    
    Top3 = ordenados[:3]
    # [:3] toma solo los 3 primeros de esa lista ordenada.

    for prod, total in Top3:
        print(prod, "->", total, "unidades vendidas")
        

def ventas_por_marcas(): 
    ventas = cargar_ventas_json()

    if len (ventas) == 0: 
        print("NO HAY VENTAS REGISTRADAS")
        return

    totales_marcas = {}

    for v in ventas: 
        producto = v["productoVendido"]
        cantidad = v["cantidadVendida"]

        marca_encontrada = None
        # marca_encontrada empieza en None = “no he encontrado marca todavía”.
        # Si después de buscar sigue None, significa que no hubo coincidencia.

        for p in productos: 
            if p["nombreProducto"].lower()== producto.lower():
                marca_encontrada = p["marca"]
                break
            
        if marca_encontrada is None:
            # Si no encontramos la marca en inventario, ignoramos esa venta.
            continue
            
        if marca_encontrada not in totales_marcas:
            totales_marcas[marca_encontrada] = 0 
    
        totales_marcas[marca_encontrada] += cantidad

    print("\n============= VENTAS AGRUPADAS POR MARCA ============\n")
    for marca, total in totales_marcas.items():
        print(f"{marca}->{total} unidades vendidas")


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
        descuento = v["descuentoAplicado"]

        precio = None
        # precio=None significa “no he encontrado el precio todavía”.
        # Si al final queda en None, no calculo esa venta.

        for p in productos:
            if p["nombreProducto"].lower() == producto.lower():
                precio = p["precioUnitario"]
                break

        if precio is None:
            continue

        bruto_venta = precio * cantidad
        neto_venta = bruto_venta * (1 - descuento / 100)

        ingreso_bruto += bruto_venta
        ingreso_neto += neto_venta

    print("\n===== INGRESOS =====\n")
    print(f"Ingreso bruto total: {ingreso_bruto}")
    print(f"Ingreso neto total: {ingreso_neto}")  


def rendimiento_inventario():
    ventas = cargar_ventas_json()

    # 1) sumar vendido total por producto (igual que top3).
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
        # .get(nombre, 0) significa:
        # “si el producto está en el diccionario, dame su total vendido;
        #  si no está (nunca se vendió), devuelve 0”.
        # Esto evita errores y además te permite medir productos sin ventas.

        total_inicial = vendido + stock
        # total_inicial es una aproximación del stock que había al inicio:
        # lo que vendiste + lo que todavía te queda.

        if total_inicial == 0:
            porcentaje = 0
        else:
            porcentaje = (vendido / total_inicial) * 100

        print(f"Producto: {nombre}")
        print(f"  Vendido total: {vendido}")
        print(f"  Stock actual: {stock}")
        print(f"  % vendido: {porcentaje:.2f}%")
        # :.2f significa:
        # “mostrar el porcentaje con 2 decimales”
        # Ej: 33.333333 -> 33.33
        # Se usa para que el reporte sea legible y no salga con mil decimales.
        print()   


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


# ================================== VALIDACION DE ENTRADAS DE USUARIOS =============================

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
        else:
            return texto  # texto correcto


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

            if numero < minimo:
                print(f"Debe ser mayor o igual a {minimo}.")
                continue

            if maximo is not None and numero > maximo:
                # maximo=None significa “no hay máximo”.
                # is not None significa “solo valida máximo si sí existe”.
                print(f"Debe ser menor o igual a {maximo}.")
                continue

            return numero  # número válido

        except:
            print("Eso no es un número válido. Intenta otra vez.")
            

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