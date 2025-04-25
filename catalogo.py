# catalogo.py
#Muestra el catalogo de productos disponibles
from utils import limpiar_consola
def obtener_catalogo():
    
    return {
        "A001": {'nombre': 'Pan','precio': 1.5},
        "A002": {'nombre': 'Leche','precio': 2.5},
        "A003": {'nombre': 'Queso','precio': 15},
        "A004": {'nombre': 'Arroz','precio': 5},
        "A005": {'nombre': 'Fideos','precio': 3.2},
        "A006": {'nombre': 'Lentejas','precio': 1.2},
        "A007": {'nombre': 'Atun','precio': 3},
        "A008": {'nombre': 'Avena','precio': 1.5}
    }


#Funcion que imprime el catalogo 
def mostrar_catalogo():
    producto = obtener_catalogo()
    limpiar_consola()
    print("\nCatálogo de productos:\n")
    print(f"{'Código':<10} {'Producto':<15} {'Precio (S/)':>12}")
    print("-" * 40)

    for codigo, datos in producto.items():
        print(f"{codigo:<10} {datos['nombre']:<15} {datos['precio']:>12.2f}")
    
 
