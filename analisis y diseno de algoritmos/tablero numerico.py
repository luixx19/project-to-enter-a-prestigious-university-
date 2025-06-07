#valores globales 
global aumentar, igual, disminuir
global continuar, numero

def main():
    print("TABLERO NUMERICO")
    #leer un numero entero inicial
    numero = int(input("ingresa un numero entero: "))
    continuar = True

    while continuar:
        mostrar_menu()
        #elegir una opcion 
        opcion = input("elige una opcion del menu (1, 2, 3): ")
        
        if opcion == "1":
            numero += 1
            print(f"el numero ha sido aumentado. Ahora es: {numero}")

        elif opcion == "2": 
            print(f"el numero se ha mantenido igual: {numero}")
    
        elif opcion == "3":
            numero -= 1
            print(f"el numero ha sido disminuido. Ahora es: {numero}")

        else:
            print(f"opcion no valida, por favor selecciona la opcion que te estan marcando, pofavo🫃")


def mostrar_menu():
    print("menu..:") 
    print("1. aumentar (+)")
    print("2. igual(=)")
    print("3. disminuir(-)")

        

   # match continuar:
   #     case 1:
   #         numero = numero + 1
   #         print(f"el valor final del numero es: {numero}")
   #     case 2:
   #         print(f"el valor final del numero es: {numero}")
   #     case 3:
   #         print(f"el valor final del numero es: {numero}")
   #     case_:
   #         print("pon el valoer bien, pofavo")

if __name__ == "__main__":
    main()