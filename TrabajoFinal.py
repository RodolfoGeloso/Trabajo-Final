###Gestion de control. Primera version.

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
          5 - Salir.
           """)
    opcion=int(input("Ingrese su opción: "))
    
    if opcion==1: ###Ingreso de un nuevo item la idea la key 'producto' esté en minuscula para facilitar la busqueda.
        print("""\nOpcion 1
Ingreso de un nuevo producto dentro del stock""")
        producto=input("Ingrese el nombre del producto: ").lower()
        cantidad=int(input("Ingrese la cantidad a ingresar el producto: "))
        precio=float(input("Ingrese el precio unitario del producto: "))
        
        stock[producto]={"cantidad":cantidad,"precio":precio} 
        ### luego del ingreso de los datos se los empaqueta en un diccionario y 
        # pasan a ser el value de otro diccionario en el cual el nombre del produccto es su descripción
        
    elif opcion==2:   
        print("""\nOpcion 2
Buscaremos un artículo en el stock.""")
        producto=input("Ingrese el nombre del producto: ").lower() #seguimos con las minusculas
        
        if producto in stock: 
        ###un condicional para la busqueda, si esta se muestra los datos sino un mjs indicando que no esta.
        
            
            print(f"""El producto {producto} se encuentra en el inventario.
    Estos son las unidades disponibles: {stock[producto]["cantidad"]}.
    Este es el precio unitario {stock[producto]["precio"]}""")
            
        else:
            print(f"No se ha encontrado una entrada con la descripción {producto}")
        #Me gustaria agreagar un mjs y una funcion en el caso de que si no esta le pregunte al usuario si desea crear una nueva entrada
        
    elif opcion==3:
        print("""\nOpcion 3
Modificar producto.""")
        producto=input("Ingrese el producto a modificar: ").lower()
        if producto in stock: #me fijo si está el producto y en caso de ser afirmativo procedo a eliminar el par (key-value) y agregar el qu el usuario elija
                stock.pop(producto)
                producto=input("Ingrese el nombre del producto: ").lower()
                cantidad=int(input("Ingrese la cantidad a ingresar el producto: "))
                precio=float(input("Ingrese el precio unitario del producto: "))
                stock[producto]={"cantidad":cantidad,"precio":precio}
        else:
            print(f"No se encuentra en la lista de stock el producto {producto} ")
            
    elif opcion==4: 
        ###Un simple print del diccionario, falta dejarlo bonito es muy basico y no es una linda salida.
        print("""\nOpcion 4
Listado de los productos en el inventario.""")
        
        for nombre,item in stock.items():
            print(nombre, item)
    elif opcion==5:
        print(""""\nOpcion 5
Saludos.
Adios!!!!!!!!!!!""")
        break
