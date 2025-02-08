def factorial(n):
    """
    Recibe un número entero positivo y devuelve su factorial.
    Valida que el número sea mayor o igual a 0 y maneja errores de entrada.
    """
    if n < 0:
        raise ValueError("El número debe ser un entero positivo.")
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

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
numero = obtener_numero()

# Calcular y mostrar el factorial
print(f"El factorial de {numero} es: {factorial(numero)}")
