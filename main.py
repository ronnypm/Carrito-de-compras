#main.py 
#parte principal del programa 
from catalogo import mostrar_catalogo
from carrito import mostrar_productos_carrito,agregar_producto_carrito
from checkout import mostrar_carrito,eliminar_producto_carrito,vaciar_carrito,finalizar_compra
from utils import limpiar_consola

#Creacion del  menú 

def mostrar_menu():
    opciones = ['Ver catálogo',
                'Agregar productos al carrito',
                'Eliminar productos del carrito',
                'Vaciar carrito',
                'Mostrar carrito',
                'Finalizar compra',
                'Salir'
    ]


    print('=' * 100)
    print(f'Carrito de compras'.center(120))
    print('=' * 100)

    #Recorrido de la lista para mostrar el menu
    for indice, opcion in  enumerate(opciones, start=1):
        print(f'{indice}. {opcion}')

    return opciones



def obtener_opciones(opciones):
    while True:
        try:
        #Se hace mas dinamico el ingreso de opciones con len() en caso se ingrese mas datos en la lista opciones=[].
            elejir_opcion = int(input(f'Elija una opción (1-{len(opciones)}):'))
            if 1 <= elejir_opcion <= len(opciones):
                return elejir_opcion
            else:
                print(f'Por favor, ingrese un número entre 1 y {len(opciones)}.')
        except ValueError:
            print('Error, solo se permiten numeros.')

    

def menu():
    try:
    #Bucle principal
        while True:
            opcion = mostrar_menu() 
            eleccion = obtener_opciones(opcion)

            if eleccion == 1:
                mostrar_catalogo()
            elif eleccion == 2:
                mostrar_productos_carrito()
                agregar_producto_carrito()
            elif eleccion == 3:
                eliminar_producto_carrito()
            elif eleccion == 4:
                vaciar_carrito()
            elif eleccion == 5:
                limpiar_consola()
                mostrar_carrito()
            elif eleccion == 6:
                finalizar_compra()
            elif eleccion == 7:
                print('Saliendo del programa. ¡Gracias por comprar!')
                break

          
            input("\nPresione Enter para volver al menú...\n")
            limpiar_consola()

    except KeyboardInterrupt:
          print ('\nPrograma interrumpido por el usuario')
menu()
