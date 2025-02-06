def ordenar_numeros(numeros):
    # Uso la función incorporada sorted() para ordenar la lista en orden ascendente
    lista_ordenada = sorted(numeros)
    
    return lista_ordenada

"""
Esta función recibe una lista de números y devuelve la lista ordenada en orden ascendente.
:parametro numeros: Lista de números a ordenar.
:return: Lista de números ordenada.
"""

# Solicita al usuario una lista de números
entrada = input("Ingrese una lista de números separados por comas: ")
numeros = list(map(int, entrada.split(','))) # Map = Nos permite aplicar una función sobre los items de un objeto iterable

# Muestra la lista ordenada
print("Lista ordenada:", ordenar_numeros(numeros))
