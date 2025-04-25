#utils.py 
#Funciones auxiliares: validacion de entrada, limpiar pantalla,validacion de opciones,etc.
import os
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')


def limpiar_mensaje_error():
 
    print("\033[A\033[K", end="") 



def pregunta_si_no(mensaje):

    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ['si', 'no']:
            return respuesta
        print('Por favor, ingrese "Si" o "No".')