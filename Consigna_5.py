def factorial(n):
    
    # Recibe un número entero positivo y devuelve su factorial.
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Solicitar un número al usuario
numero = int(input("Ingrese un número entero positivo: "))

# Calcular y mostrar el factorial
print(f"El factorial de {numero} es: {factorial(numero)}")
