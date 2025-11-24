#==============================================FUNCION DESCARGAR UN ARCHIVO CSV ============================================================#


def cargar_csv (ruta): # con esta funcion vamos a cargar un archivo nuevo un tipo de archivo csv ( de argumento le subimos el lugar donde se guarsda el archivo)
    
    lista_productos = [] # aqui guardaremos lo que se leera del archivo
    filas_invalidas = 0
    with open(ruta, "r") as archivo: #aqui estamos dando la orden de leer el documento, y donde esta la informacion que necesito 
        #y a dicho archivo lo leeremos como "as archivo"
        lineas = archivo.readlines() #readlines es literamelnte leer todos los renglomes que hay un el archivos 
        
        
    encabezado = lineas[0].strip() #linea cero significa literalmente esta es el codigo para ponerle titulos o emcabezados de lo que seran los diccionarios 
        #el encabezado le da sentido al codigo y strip elimina los satos de linea
    encabezado_esperado = "nombre,precio,cantidad" #validamos para que no haya confucion del orden ni de los nombres del titulo 
    if encabezado != encabezado_esperado:
        print("archivo malo")
        return [] #me retorna a la lista vacia 
       
    #como ya le dimos la orden a python de como es qye vamos a leer un archvio csv ahora coemnzamos a sacar la informacion del archivo usando un for  
    for linea in lineas [1:]: # esto significa que vamos a comenzar a leer desde la posicion 1 o sea la segunda linea de informacion
        linea = linea.strip() # como las lineas vienen asi ("coco,1500,345\n") con el strip quitamos ese \n, recuerda que esamos traduciendo a formato leible por python 
        partes = linea.split(",") #aca el split parte el texto que viene como "nombre,precio,cantidad" en "nombre", "precio"...y los guarda en una lista 
        if len (partes) != 3: #basicamente es, si mientras hacias tu traabjo de partir solo partiste 2 entonces eso esta malo
            print("fila invalida, se ignora", linea)
            continue
        nombre,precio_txt,cantidad_txt = partes #esto signica que lo que tenemos en partes, lo guardes en nombre, precio y texto, recuerda que en paython lo que esta del lado drecho se guarda en lo que esta en izquierdo hablando de simbolo iguales 
        
        try: #aca simplemnte vamos a tratar de converir (lo que sacamos de partes) en lo siguiente: 
            precio = float(precio_txt)
            cantidad = int(cantidad_txt)
        except:
            filas_invalidas += 1 # un contador 
            print("Fila invalida, el precio indicado y la cantidad no son numeros, se ignorara esa linea",linea)
            continue # si no se logro convertir, ignoramos y seguimos 
        
        if precio <=0  or cantidad <=0: #aqui vamos a invalidar la informacion que no corresponda a numeros positivos 
            filas_invalidas += 1
            print("Fila invalida, el precio indicado y la cantidad no son validos negativos o cero, se ignorará esa linea",linea)
            print("Los valores ingresados son negagtivos")
            continue
        
        producto = { #aqui, como ya validamos que la informacion que esta pasando es valida, la vamos guardando en un diccionario  

            
            "nombre": nombre, 
            "precio" : float(precio),
            "cantidad" : int(cantidad)
        }
        
        
        lista_productos.append(producto) # la guardamos en una lista 
    print(f"El numero de productos cargados fueron: {len(lista_productos)}  ") #aqui le indicamos al usario cuantos productos de los que trajimos de la tabla de excel csv estaban malos 
    print(f"El numero de filas invalidas fueron: {filas_invalidas}")
    
    return lista_productos # y podemos adquirir la lista que ya tenemos 


#==============================================FUNCION PARA MODIFICAR UN ARCHIVO QUE YA NO ES CSV AHORA ES LIBLE POR PYTHON  ============================================================#


def aplicar_carga_csv(inventario, lista_cargada, decision,):
    if decision == "s":
        inventario.clear() #aqui borramos el invenario viejo porque asi lo decidio el usuario
        inventario.extend(lista_cargada) #Basicamente estamos dando la orden de que lo que trajo el csv se guarde en inventario (lista cargada es lo que trajo el csv)
        return print("Inventario reemplazado con el csv")
    
    elif decision == "n":
        for nuevo in lista_cargada: #aqui estamos recorriendo todo lo que nos trajo el csv para saber que hay 
            existe = False #antes de cualquier cosa asumiremos que lo que trajo el csv no lo tenemos 
            
            for p in inventario: # por ende vamos a confirmar eso 
                if p["nombre"].lower()==nuevo["nombre"].lower(): #basicamente aqui dice que si el iterador encuentra un nombre que es igual al nuevo nombre entonces 
                    p["cantidad"] += nuevo["cantidad"] #solo debemos sumar el viejo con el nuevo 
                    if p["precio"] != nuevo["precio"]:# si el precio es diferente el viejo del nuevo 
                        p["precio"] = nuevo["precio"] # entonces solo debemos igualarlo para que python entienda que debe reemplazarlo 
                    existe = True #como sabemos que si hay productos repetido entonces la codicion anterior cambia y significa que el producto no es nuevo 
                    break #y finalizamos
                
            if not existe:
                inventario.append(nuevo) #si el producto no existe actualmente en el inventario, pues se guarda directamente 
    else:
        return"Opcion invalida.No se hizo nada" # por si dijitan algo que no va
    
  
   
#==============================================MENU PARA LLAMAR LAS FUNCIONES ANTERIORES Y PONERLAS A TRABAJAR  ============================================================#

def menu_cargar_csv(Inventario):
    ruta = input("por favor, escribe la ruta del archivo CSV: ") #aqui entonces vamos a preguntar donde esta el archivo csv que necesitamos parfa coemnzar a trabajar 
    lista_cargada = cargar_csv(ruta)  #dejamos estipulado que todo lo que se haga en la funcion cargar csv va a quedar guardada en lista de carga 
    
    if not lista_cargada: #si no hay nada pues no hay nada 
        print("Lo sentimos, pero no se cargonada, archivo vacio o invalido")
        return

    decision = input("¿ Desea sobre escribir el inventario actual? (si/no): ").lower() # aca por oto lado vamos a preguntar se hara con la informacion 
    mensaje = aplicar_carga_csv (Inventario, lista_cargada, decision ) #ponemos a trabajar a la funcion y sea lo que sea que se haga con la informacion 
    print("Inventario reemplazado con el csv")
    return
    
    
 #==============================================FUNCION PARA CONVERTIR TODO DE NUEVO A FORMATO CSV Y GUARDARLO DONDE TU QUIERAS ============================================================#
 
 
 
def guardar_csv(inventario, ruta, incluir_header=True): #Creamos una funcion para guardar la informacion que ya hemos manipulado, debemos tener en cuenta el inventario claramente 
# la ruta donde vamos a gurdar y pues dejar como claridad con incluir_header=True que necesitamos tener si o si encabezado 
    if len(inventario) == 0: 
        print("Inventario vacío. No hay nada para guardar.") #aqui se hace una confirmacion si la lista de inventarios esta vacia pues no es necesario crear un archivo para guardar algo vacio 
        return # a menos que querramos usar esto despues para guardar x cosas, dependera de lo que queramos

    try: # si tenemos datos en inventario vamos a intentar entonces crear un archivo donde guardaremos la informacion de inventario como un copia y pega 
        with open(ruta, "w", encoding="utf-8") as archivo: # pero con ciertas condiciones, el archvio debera tener una ruta para guardarlo mas tarde, que quede estipulado que vamos a "escribir"
            # y que por si acaso hay caracteres especiales con encoding podamos entenderlos, bueno python pueda entenderlos 
            if incluir_header: 
                archivo.write("nombre,precio,cantidad\n") # aqui estamos escribiendo un encabezado en formato de nuevo csv

            for p in inventario: #abrimos un bucle porque con un iterador vamos a sacar la informacion dentro del inventario y...
                linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n" # y vamos a crear lineas y en las lineas vamos guardando la informacion en cada casilla todo en formato csv
                archivo.write(linea) # y la informacion de la linea vamos a guardarla en el archvo que creamos al comienzo de la funcion.

        print(f"Inventario guardado en: {ruta}") #despues que el for haga todo ese trabajo se guarda en la ruta el archivo sea cual sea la ruta 

    except PermissionError:
        print("No tienes permisos para escribir en esa ruta.") #por si acaso dejamos unos except para que no se rompa el codigo 
    
#==============================================MENU PARA PONER A FUNCIONAR EL GUARDAR CSV ============================================================#

def menu_guardar_csv(inventario): #aqui creamos el menu que va a llamar la funcion gaurdar el cvs 
    ruta = input("Escribe la ruta donde quieres guardar el CSV (ej: inventario.csv): ").strip() # y pedimos donde se guardara todo 
    
    guardar_csv(inventario, ruta, incluir_header=True) # llammos la funcion que hace todo el trabajo pesado, como el que estoy haciendo yo a las 2 am un viernes :(