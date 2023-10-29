def tabla_multiplicar_recursiva(numero, multiplicador, limite):
    if multiplicador > limite:
        return
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")
    tabla_multiplicar_recursiva(numero, multiplicador + 1, limite)

if __name__ == "__main__":
    numero = int(input("Ingrese el número para la tabla de multiplicar: "))
    limite = int(input("Ingrese el límite para la tabla de multiplicar: "))
    tabla_multiplicar_recursiva(numero, 1, limite)
