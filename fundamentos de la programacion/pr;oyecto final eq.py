import random 

FILAS = 6
COLUMNAS = 7
VACIO = " "

def crear_tablero():
    return [[VACIO for _ in range (COLUMNAS)] for _ in range(FILAS)]

def mostrar_tablero():
    for FILA in tablero: 
        print("|"+"|".join(FILA) + "|")
        print(" "+" ".join(str(i) for i in range (1, COLUMNAS + 1)))

def columna_llena(tablero, columna):
    return tablero[0][COLUMNAS] != VACIO 

def insertar_ficha(TABLERO, COLUMNA, FICHA):
    for FILA in reversed (TABLERO)
        if FILA[COLUMNA] == VACIO:
            FILA[COLUMNA] = FICHA 
            return True 
        return False 
    
def verificar_ganador(TABLERO, FICHA):
    #horizontal
    for FILA in range (FILAS):
        for col in range (COLUMNAS - 3):
            if all(TABLERO[FILAS]) 