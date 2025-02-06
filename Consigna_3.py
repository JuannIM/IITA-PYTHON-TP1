def encontrar_diferencias(conjunto1, conjunto2):
    
    # Encuentra los números que están en un conjunto pero no en el otro.
    
    faltan_en_segundo = conjunto1 - conjunto2
    faltan_en_primero = conjunto2 - conjunto1
    return faltan_en_segundo, faltan_en_primero

# Ingresar los conjuntos
conjunto1 = set(map(int, input("Ingrese los números del primer conjunto separados por comas: ").split(',')))
conjunto2 = set(map(int, input("Ingrese los números del segundo conjunto separados por comas: ").split(',')))

# Encontrar diferencias
faltan_en_segundo, faltan_en_primero = encontrar_diferencias(conjunto1, conjunto2)

# Mostrar resultados
print("Números que están en el primer conjunto pero no en el segundo:", faltan_en_segundo)
print("Números que están en el segundo conjunto pero no en el primero:", faltan_en_primero)
