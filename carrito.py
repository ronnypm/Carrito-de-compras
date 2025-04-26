#carrito.py
#Funciones para menejar el carrito de compras:mostrar,validar_codigo, agregar.
from catalogo import obtener_catalogo
from utils import limpiar_consola,pregunta_si_no



#Funcion que muestar codigo con su respectivo producto
def mostrar_productos_carrito():
    productos = obtener_catalogo()
    limpiar_consola()
    print("Productos disponibles:")
   

    print(f'{"Código":<10} {'Producto':<10}')
    print("-" * 40)
    for codigo, producto in productos.items():
        print(f'{codigo:<10} {producto['nombre']:<10}')




#Funcion que valida codigo del producto
def validar_codigo_carrito():
    # print("Ejecutando validación de código...")
    productos = obtener_catalogo()
    
    while True:

        codigo_producto = input('\nIngrese el código del producto que desea:  ').strip().upper()
        try:
            cantidad_producto  = int(input('Ingrese la cantidad: '))
        except ValueError:
            print("Por favor ingrese un numero")

        #valida que se ingrese un codigo correcto 
        if codigo_producto in productos:
            return codigo_producto, cantidad_producto
        else:
            #si no se ingresa un codigo correcto imprime error y vuelve a pedir otro codigo
            print('Por favor ingrese un codigo correcto.')




#Fucion par agreagar productos al carrito 
carrito = {}

def agregar_producto_carrito():
    global carrito
    while True:
        codigo_producto, cantidad_producto= validar_codigo_carrito()
        productos = obtener_catalogo()

        producto = productos[codigo_producto]

        if codigo_producto in carrito:
            carrito[codigo_producto]['cantidad'] += cantidad_producto
        else:
            carrito[codigo_producto] = {
                'nombre':producto['nombre'],
                'precio':producto['precio'],
                'cantidad': cantidad_producto

        }
            
        
        print(f'✔ Se agregado {producto["nombre"]} al carrito.')



        #preguntamos al usuario si quiere seguir ingresando productos
        nuevo_producto = pregunta_si_no('Desea agregar otro producto (Si-No)?: ')

        if nuevo_producto == 'no':
            return carrito
        
    

def obtener_carrito():
    return carrito
    


