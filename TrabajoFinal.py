###Gestion de control. Primera version.

def ingreso_producto (lista_stock):
    
        producto=input("Ingrese el nombre del producto: ").lower() ###Ingreso de un nuevo item la idea la key 'producto' esté en minuscula para facilitar la busqueda.
        cantidad=int(input("Ingrese la cantidad a ingresar el producto: "))
        precio=float(input("Ingrese el precio unitario del producto: $"))
        lista_stock[producto]={"cantidad":cantidad,"precio":precio} 

def busqueda_producto(lista_stock):
        producto=input("Ingrese el nombre del producto: ").lower() #seguimos con las minusculas
    
        if producto in lista_stock: 
        ###un condicional para la busqueda, si esta se muestra los datos sino un mjs indicando que no esta.
         
            print(f"""El producto {producto} se encuentra en el inventario.
    Estos son las unidades disponibles: {lista_stock[producto]["cantidad"]}.
    Este es el precio unitario {lista_stock[producto]["precio"]}""")
            
        else:
            print(f"No se ha encontrado una entrada con la descripción {producto}")
        #Me gustaria agreagar un mjs y una funcion en el caso de que si no esta le pregunte al usuario si desea crear una nueva entrada

def modificar_producto(lista_stock):
        producto=input("Ingrese el producto a modificar: ").lower()
        if producto in lista_stock: #me fijo si está el producto y en caso de ser afirmativo procedo a eliminar el par (key-value) y agregar el qu el usuario elija
                lista_stock.pop(producto)
                producto=input("Ingrese el nombre del producto: ").lower()
                cantidad=int(input("Ingrese la cantidad a ingresar el producto: "))
                precio=float(input("Ingrese el precio unitario del producto: "))
                lista_stock[producto]={"cantidad":cantidad,"precio":precio}
        else:
            print(f"No se encuentra en la lista de stock el producto {producto} ")
            
def listado_productos (lista_stock):
    for nombre,producto in lista_stock.items():
        print (f"{nombre} - cantidad: {producto['cantidad']} - precio:{producto['precio']}.")
        
#main
print("""Bienvenido al Sistema de gestión y Control de stock""")

stock={
    "procesador":{"cantidad":12,"precio":50000},
    "motherboard":{"cantidad":10,"precio":11450},
    "mouse":{"cantidad":52,"precio":5000},
    "teclado":{"cantidad":14,"precio":4500},
} 
###Datos para realizar pruebas básicas de funcionamiento, me gustaria cambiar los datos a mostrar quizas agregarle más.
#Que el diccionario queda algo así stock={ 100200 : {'producto':'procesador','cantidad':12,'precio':50000,'importado':False}} ***100200 es una especie de codigo del stock

while True:
    print("""Seleccione su Opción.
          1 - Ingresar producto.
          2 - Buscar producto.
          3 - Modificar datos del producto.
          4 - Ver listado de stock.
          5 - Exportar a un Archivo.
          6 - Importar a un Archivo
          7 - Salir.
           """)
    while True:
        try:
            opcion=int(input("Ingrese su opción: "))
            break
        except:
            print("Tiene que ser un valor númerico: ")
    
    if opcion==1: 
        print("""\nOpcion 1
Ingreso de un nuevo producto dentro del stock""")
        ingreso_producto(stock)
     
    elif opcion==2:   
        print("""\nOpcion 2
Buscaremos un artículo en el stock.""")
        busqueda_producto(stock)
  
    elif opcion==3:
        print("""\nOpcion 3
Modificar producto.""")
        modificar_producto(stock)
               
    elif opcion==4: 
        ###Un simple print del diccionario, falta dejarlo bonito es muy basico y no es una linda salida.
        print("""\nOpcion 4
Listado de los productos en el inventario.""")   
        listado_productos(stock)
            
    elif opcion==5:
        print("""\nOpcion 5.
Exportar a un archivo!!!!!!!!!!!""")
        pass
    
    elif opcion==6:
        print("""\nOpcion 6
Importar desde un Archivo!!!!!!!!!!!""")
        pass
    
    elif opcion==7:
        print("""\nOpcion 7
Saludos.
Adios!!!!!!!!!!!""")
        break
    else:
        print("""Opcion Incorrecta
Vuelta al menú""")
