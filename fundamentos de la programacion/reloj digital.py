
#inicializacion de variables globales para horas y minutos
horas = 0
minutos = 0


def main():
    global horas, minutos 
    print("RELOJ DIGITAL")

    #solicitar la hora y minutos iniciales del usuarip 
    horas = int(input("hora inicial: "))
    minutos = int(input("minutos iniciales: "))

    #ajuste de hora y minutos si estan fuera de los limites permitidos 
    if (horas < 0 or horas > 23):
     horas = 12

    if (minutos < 0 or minutos > 59):
        minutos = 0

    #mostrar la hora inicial en la pantalla
    pantalla(horas, minutos)

    #ejemplos de restar minutos y mostrar el resultado en pantalla
    minutos = restar_minutos(minutos)
    minutos = restar_minutos(minutos)
    pantalla(horas, minutos )


def pantalla(h, m):
    #funcion para mostrar la hora en formato HH:MM
    print("+--+--+--")
    print(f"|{h:02}:{m:02}|")
    print("+--+--+")


def sumar_hora(h):
    #funcion para sumar una hora, con ajuste si se pasa de 23
    h += 1
    if h > 23:
        h = 0
    return h


def restar_hora(h):
    #funcion para restar una hora,con ajuste si es menor de 0
    h-= 1
    if h < 0:
        h = 23 
    return h


def sumar_minutos(m):
#funcion para sumar minutos, con ajuste si pasa de 59
    m += 1
    if m > 59:
        global horas
        horas = sumar_hora(horas)
        m = 0
    return m   
 

def restar_minutos(m):
    #funcion para restar minutos, con ajuste si es menor a 0
    m -= 1
    if m < 0:
        global horas
        horas = restar_hora(horas)
        m = 59
    return m 

if __name__ == "__main__":
    main()

