def obtener_conjunto(mensaje):
    """
    Solicita al usuario una lista de números separados por comas y devuelve un conjunto de enteros.
    Maneja errores de entrada y elimina espacios en blanco.
    """
    while True:
        try:
            return {int(num.strip()) for num in input(mensaje).split(',')}
        except ValueError:
            print("Error: Ingrese solo números separados por comas.")

def encontrar_diferencias(conjunto1, conjunto2):
    """
    Encuentra los números que están en un conjunto pero no en el otro.
    Devuelve dos conjuntos con las diferencias.
    """
    faltan_en_segundo = conjunto1 - conjunto2
    faltan_en_primero = conjunto2 - conjunto1
    return faltan_en_segundo, faltan_en_primero

# Ingresar los conjuntos con validación de entrada
conjunto1 = obtener_conjunto("Ingrese los números del primer conjunto separados por comas: ")
conjunto2 = obtener_conjunto("Ingrese los números del segundo conjunto separados por comas: ")

# Encontrar diferencias
faltan_en_segundo, faltan_en_primero = encontrar_diferencias(conjunto1, conjunto2)

# Mostrar resultados
print("Números que están en el primer conjunto pero no en el segundo:", faltan_en_segundo)
print("Números que están en el segundo conjunto pero no en el primero:", faltan_en_primero)
