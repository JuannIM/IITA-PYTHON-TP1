def contar_ocurrencias(lista, elemento):
    
    # Recibe una lista y un elemento, y devuelve cuántas veces aparece en la lista.
    
    return lista.count(elemento)

# Solicitar la lista al usuario
lista = input("Ingrese los elementos de la lista separados por comas: ").split(',')

# Solicitar el elemento a contar
elemento = input("Ingrese el elemento a contar: ")

# Contar ocurrencias y mostrar el resultado
print(f"El elemento '{elemento}' aparece {contar_ocurrencias(lista, elemento)} veces en la lista.")
