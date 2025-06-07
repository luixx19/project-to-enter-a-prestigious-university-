def main():
    print("=adivina el numero=")
    
    import random

    print("Bienvenido al juego de adivinar el número!")
    print("Selecciona la dificultad: ")
    print("1. Fácil (10 intentos)")
    print("2. Medio (5 intentos)")
    print("3. Difícil (3 intentos)")

    # Pedir la dificultad
    dificultad = int(input("Elige una opción (1, 2 o 3): "))
    if dificultad == 1:
        intentos = 10
    elif dificultad == 2:
        intentos = 5
    else:
        intentos = 3

    # Generar un número aleatorio
    numero_secreto = random.randint(1, 100)
    print("elegi un número entre 1 y 100. Adivina cual es... ")

    # Bucle para adivinar
    while intentos > 0:
        print(f"Intentos restantes: {intentos}")
        intento = int(input("Adivina el número: "))

        if intento == numero_secreto:
            print(f"Felicidades! Adivinaste el número. Te sobraron {intentos} intentos.")
            break 
        elif intento < numero_secreto:
            print("El número es mayor")
        else:
            print("El número es menor")

        intentos -= 1

    if intentos == 0:
        print(f"Se acabaron los intentos! El número era {numero_secreto}.")


if __name__ == "__main__":
    main()
    
    #el break se utiliza para salir de un bucle. Ahorita lo utilizamos para detener el 
    #bucle "while" cuando el usuario encuentre el numero (lo investigue porque pedi un poco de ayuda).

    #igual con el "import random"