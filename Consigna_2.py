def crear_conjunto():
    
    # Crea un conjunto a partir del input del usuario.
    
    elementos = input("Ingrese los elementos del conjunto separados por comas: ")
    return set(elementos.split(','))

def eliminar_elemento(conjunto):
    
    # Elimina un elemento del conjunto si está presente.
    
    elemento = input("Ingrese el elemento que quiere eliminar: ")
    if elemento in conjunto:
        conjunto.remove(elemento)
        print("Elemento eliminado.")
    else:
        print("El elemento no está en el conjunto.")

# Crear un conjunto
conjunto_usuario = crear_conjunto()
print("Conjunto creado:", conjunto_usuario)

# Eliminar un elemento
eliminar_elemento(conjunto_usuario)
print("Conjunto actualizado:", conjunto_usuario)

# No he realizado este programa para utilizarlo unicamente con INT, se puede utilizar lo que se desee.
