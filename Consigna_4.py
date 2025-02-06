def eliminar_duplicados(lista):
    
    # Recibe una lista de cadenas y devuelve una lista con elementos únicos.
    
    return list(set(lista))

# Ingresar la lista de cadenas
lista_cadenas = input("Ingrese las cadenas separadas por comas: ").split(',')

# Eliminar duplicados
lista_sin_duplicados = eliminar_duplicados(lista_cadenas)

# Mostrar resultado
print("Lista sin duplicados:", lista_sin_duplicados)
