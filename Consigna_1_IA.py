def ordenar_numeros(numeros: list[int]) -> list[int]:
    return sorted(numeros)
"""
Recibe una lista de números y devuelve la lista ordenada en orden ascendente.
:param numeros: Lista de números a ordenar.
:return: Lista de números ordenada.
"""

def obtener_lista_numeros() -> list[int]:
    """
    Solicita al usuario una lista de números separados por comas y la convierte en una lista de enteros.
    Maneja posibles errores en la entrada del usuario.
    :return: Lista de números ingresados por el usuario.
    """
    while True:
        entrada = input("Ingrese una lista de números separados por comas: ")
        try:
            # Eliminamos espacios y convertimos los valores en enteros
            numeros = [int(num.strip()) for num in entrada.split(',')]
            return numeros
        except ValueError:
            print("Error: Ingrese solo números separados por comas.")

# Obtener la lista de números del usuario
numeros = obtener_lista_numeros()

# Mostrar la lista ordenada
print("Lista ordenada:", ordenar_numeros(numeros))
