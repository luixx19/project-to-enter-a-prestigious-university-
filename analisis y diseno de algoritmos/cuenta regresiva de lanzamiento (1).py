#CUENTA REGRESIVA!!

import time

# Preguntar al usuario por el número de inicio
inicio = int(input("Introduce el número inicial para la cuenta regresiva: "))

for i in range(inicio, -1, -1): 
    if i % 5 == 0 and i != 0: 
        print(f"Advertencia: {i} segundos para el lanzamiento")
    elif i == 0: 
        print("¡Lanzamiento iniciado!")
    else: 
        print(i)
    time.sleep(1)  
print("¡Ha comenzado el lanzamiento! 🚀")

