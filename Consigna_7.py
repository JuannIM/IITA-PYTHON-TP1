def suma_recursiva(n):
    """
    Recibe un número n y devuelve la suma de los primeros n números naturales de forma recursiva.
    """
    if n == 0:
        return 0
    return n + suma_recursiva(n - 1)

# Solicitar un número al usuario
n = int(input("Ingrese un número entero positivo: "))

# Calcular y mostrar la suma recursiva
print(f"La suma de los primeros {n} números naturales es: {suma_recursiva(n)}")
