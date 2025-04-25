#checkout.py
#logica para finalizar la compra y mostrar el resumen 
from carrito import obtener_carrito
from utils import limpiar_consola,pregunta_si_no



#Funcio para eliminar productos del carrito 
def eliminar_producto_carrito():
    while True:
        carrito_actual = obtener_carrito()
        limpiar_consola()
        print('Eliminar producto de carrito.')
        mostrar_carrito()
        producto_eliminar = input('\nIngrese el codigo del producto a eliminar: ').strip().upper()


        if producto_eliminar in carrito_actual:
            producto_eliminado = carrito_actual[producto_eliminar]['nombre']
            del(carrito_actual[producto_eliminar])
            print(f'Producto eliminado {producto_eliminado}')
            
    
        #Si el carrito queda vacio ya no se sigue preguntado si eliminar otro producto
        if not  carrito_actual:
            limpiar_consola()
            mostrar_carrito()
            print('\nCarrito vacio')
            return
            

        #Pregunta si se quiere seguien elimando productos
        eliminar_otro_producto = pregunta_si_no('Desa eliminar otro producto (Si-No): ')
        if eliminar_otro_producto == 'no':
             break
        elif eliminar_otro_producto == 'si':
            continue
      



#Funcion para eliminar todos los productos del carrito
def vaciar_carrito():
        carrito_actual = obtener_carrito()
        limpiar_consola()
        print('Vaciar carrito.')
        mostrar_carrito()
        

        #Si no hay producto no nos pregunta si vaciar el corrito 
        if not  carrito_actual:
            limpiar_consola()
            mostrar_carrito()
            print('\nNo tiene productos en su carrito')
            return



        eleminar_compra_completa =pregunta_si_no('\nDesea eliminar toda su compra?(Si-No): ')


        if eleminar_compra_completa == 'si':
            limpiar_consola()
            carrito_actual.clear()
            print('Vaciar corrito.')
            mostrar_carrito()
            print('\nSe elimino todos los producto.')
            return
        elif eleminar_compra_completa == 'no':
            print('Puede seguir comprando o ir a pagar su compra.')
            return 
     



#Funcion mostrar resumen de compra
def mostrar_carrito():
    carrito_actual = obtener_carrito()
    print('\nResumen de compra.')
    print(f'{"Código":<10} {"Producto":<20} {"Precio Unidad":<15} {"Cantidad":<10} {'Precio total(S/)':<15}')
    print("-" * 74)

    for codigo, datos in carrito_actual.items():
        suma_precios = datos["precio"] * datos["cantidad"]
        print(f'{codigo:<10} {datos["nombre"]:<20} {datos["precio"]:<15.2f} {datos["cantidad"]:<10} {suma_precios:<15.2f}')



def procesar_pago(total):
    print('\nDatos del cliente')
    nombre = input('Ingrese su nombre:')
    
    
    while True:
        try:

            monto_pago  = float(input('Ingrese el monto a pagar: '))


            if monto_pago < total:
                print(f'Saldo insuficiente falta S/.{total - monto_pago}')
            elif monto_pago > total:
                print(f'Monto exedido, usted tiene que pagar S/.{total}')
            else:
                print(f'Pago exitoso. Gracias {nombre} por su compra')
                exit()
        except ValueError:
            print('Ingrese un dato correcto.')
    



#funcion para pagar y finlaizar la compra
def finalizar_compra():
    carrito_actual = obtener_carrito()
    limpiar_consola()
    print('Finalizando compra...')
    mostrar_carrito()


    total = 0
    for datos in carrito_actual.values():
        total += datos["precio"] * datos["cantidad"]

    print("-" * 74)
    print(f'{"Total a pagar:":<55}    {total:.2f}')
    procesar_pago(total)

    


        
    
   






    

