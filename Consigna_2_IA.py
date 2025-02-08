def crear_conjunto():
    """
    Crea un conjunto a partir de la entrada del usuario.
    Se eliminan espacios en blanco adicionales para mayor precisión.
    """
    elementos = input("Ingrese los elementos del conjunto separados por comas: ")
    return {elemento.strip() for elemento in elementos.split(',')}

def eliminar_elemento(conjunto):
    """
    Elimina un elemento del conjunto si está presente.
    Ahora verifica si el conjunto no está vacío antes de eliminar.
    """
    if not conjunto:
        print("El conjunto está vacío, no hay elementos para eliminar.")
        return
    
    elemento = input("Ingrese el elemento a eliminar: ")
    if elemento in conjunto:
        conjunto.remove(elemento)
        print(f"Elemento '{elemento}' eliminado.")
    else:
        print(f"El elemento '{elemento}' no está en el conjunto.")

# Crear un conjunto
conjunto_usuario = crear_conjunto()
print("Conjunto creado:", conjunto_usuario)

# Eliminar un elemento
eliminar_elemento(conjunto_usuario)
print("Conjunto actualizado:", conjunto_usuario)
