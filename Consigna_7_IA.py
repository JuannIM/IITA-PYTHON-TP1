def suma_recursiva(n):
    """
    Recibe un número n y devuelve la suma de los primeros n números naturales de forma recursiva.
    Valida que el número sea positivo y maneja errores.
    """
    if n < 0:
        raise ValueError("El número debe ser un entero positivo.")
    if n == 0:
        return 0
    return n + suma_recursiva(n - 1)

def obtener_numero():
    """
    Solicita un número entero positivo al usuario y maneja errores de entrada.
    """
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo: "))
            if numero >= 0:
                return numero
            else:
                print("Error: Debe ingresar un número positivo.")
        except ValueError:
            print("Error: Ingrese un número válido.")

# Obtener el número validado
n = obtener_numero()

# Calcular y mostrar la suma recursiva
print(f"La suma de los primeros {n} números naturales es: {suma_recursiva(n)}")
