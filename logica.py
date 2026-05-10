
def iniciar_reto():
    try:
        n1 = float(input("Ingresa el primer número: "))
        n2 = float(input("Ingresa el segundo número: "))
        n3 = float(input("Ingresa el tercer número: "))

        numeros = [n1, n2, n3]
        mayor_a_menor = sorted(numeros, reverse=True)
        menor_a_mayor = sorted(numeros)
        print("\n--- Resultados ---")
        print(f"De mayor a menor: {mayor_a_menor}")
        print(f"De menor a mayor: {menor_a_mayor}")

        if n1 == n2 == n3:
            print("Los tres números son iguales.")
        elif n1 == n2 or n2 == n3 or n1 == n3:
            print("Hay dos números que son iguales.")

    except ValueError:
        print("Error: Por favor, ingresa solo números válidos.")

if __name__ == "__main__":
    iniciar_reto()
    