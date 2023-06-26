
import numpy as np
import random
from random import shuffle
from colorama import init, Fore, Style

class CuboRubik:
    #Constructor
    def __init__(self):
        self.cubo = np.array([
            [[f"{Fore.RED}R{Fore.RESET}"]*3 for _ in range(3)],
            [[f"{Fore.RESET}{Fore.RED}{Style.BRIGHT}N{Fore.YELLOW}{Style.NORMAL}{Fore.RESET}"]*3 for _ in range(3)],
            [['B']*3 for _ in range(3)],
            [[f"{Fore.  YELLOW}A{Fore.RESET}"]*3 for _ in range(3)],
            [[f"{Fore.GREEN}V{Fore.RESET}"]*3 for _ in range(3)],
            [[f"{Fore.BLUE}X{Fore.RESET}"]*3 for _ in range(3)]])

    movimientos = ['B', 'R', 'N', 'A', 'X', 'V']
    direccionMovimineto = ['H','AH']
    combinacionesRealizadas = []
    numCombinacionesRealizadas = 0

    ##FUNCIONES PRINCIPALES
    #ROTAR CARA
    def rotar(self, cara, direccion):
        if cara not in ['R', 'N', 'B', 'A', 'V', 'X']:
            print("Capa inválida")
            return
        if direccion not in ['H', 'AH']:
            print("Dirección inválida")
            return
        # Realizar el movimiento
        if cara == 'B':
            self.moverB(direccion)
            self.numCombinacionesRealizadas += 1
            self.combinacionesRealizadas.append(['B',direccion])
        if cara == 'R':
            self.moverR(direccion)
            self.numCombinacionesRealizadas += 1
            self.combinacionesRealizadas.append(['R', direccion])
        if cara == 'N':
            self.moverN(direccion)
            self.numCombinacionesRealizadas += 1
            self.combinacionesRealizadas.append(['N', direccion])
        if cara == 'A':
            self.moverA(direccion)
            self.numCombinacionesRealizadas += 1
            self.combinacionesRealizadas.append(['A', direccion])
        if cara == 'X':
            self.moverX(direccion)
            self.numCombinacionesRealizadas += 1
            self.combinacionesRealizadas.append(['X', direccion])
        if cara == 'V':
            self.moverV(direccion)
            self.numCombinacionesRealizadas += 1
            self.combinacionesRealizadas.append(['V', direccion])

    #DESORDENAR ALEATORIAMENTE
    '''def desordenar(self):
        shuffle(self.movimientos)
        for key in self.movimientos:
            self.rotar(key, 'H')'''

    #REALIZAR X NUMERO DE MOVIMIENTOS ALEATORIOS
    def movimientosAleatorios(self, numMovimientos):
        for i in range(numMovimientos):
            movAleatorio = random.choice(self.movimientos)
            direccionAleatoria = random.choice(self.direccionMovimineto)
            self.rotar(movAleatorio, direccionAleatoria)

    ##FUNCIONES SECUNDARIAS
    #MOVER CARA BLANCA
    def moverB(self, direccion):
        if direccion.upper() == 'H':
            self.horarioB()
        elif direccion.upper() == 'AH':
            for i in range(3):
                self.horarioB()

    def horarioB(self):
        self.cubo[2] = np.rot90(self.cubo[2], 1)  # gira cara superior (Blanco)
        temp = np.copy(self.cubo[0][0])  # guarda la fila superior de la cara frontal (Rojo)
        self.cubo[0][0] = self.cubo[4][0]  # mueve fila superior de cara izquierda (Verde) a cara frontal
        self.cubo[4][0] = self.cubo[1][0]  # mueve fila superior de cara posterior (Naranja) a cara izquierda
        self.cubo[1][0] = self.cubo[5][0]  # mueve fila superior de cara derecha (Azul) a cara posterior
        self.cubo[5][0] = temp  # mueve fila guardada a cara derecha

    # MOVER CARA AMARILLA
    def moverA(self, direccion):
        if direccion.upper() == 'H':
            self.horarioA()
        elif direccion.upper() == 'AH':
            for i in range(3):
                self.horarioA()

    def horarioA(self):
        self.cubo[3] = np.rot90(self.cubo[3], -1)  # gira cara superior (Blanco)
        temp = np.copy(self.cubo[0][2])  # guarda la fila superior de la cara frontal (Rojo)
        self.cubo[0][2] = self.cubo[4][2]  # mueve fila superior de cara izquierda (Verde) a cara frontal
        self.cubo[4][2] = self.cubo[1][2]  # mueve fila superior de cara posterior (Naranja) a cara izquierda
        self.cubo[1][2] = self.cubo[5][2]  # mueve fila superior de cara derecha (Azul) a cara posterior
        self.cubo[5][2] = temp  # mueve fila guardada a cara derecha

    # MOVER CARA NARANJA
    def moverN(self, direccion):
        if direccion.upper() == 'H':
            self.horarioN()
        elif direccion.upper() == 'AH':
            for i in range(3):
                self.horarioN()

    def horarioN(self):
        self.cubo[1] = np.rot90(self.cubo[1], -1)  # gira cara posterior (Naranja)
        temp = np.copy(self.cubo[2][0])  # guarda la primera fila de la cara superior (Blanco)
        self.cubo[2][0] = self.cubo[5][:,2]  # mueve columna 2 de cara derecha (Azul) a la primera fila de cara superior
        self.cubo[5][:, 2] = self.cubo[3][2]  # mueve tercera fila de cara inferior (Amarillo) a columna 3 de cara derecha
        self.cubo[3][2] = self.cubo[4][:,0]  # mueve la primera columna de cara izquierda (Verde) a la ultima fila de cara inferior
        self.cubo[4][:, 0] = temp  # mueve fila guardada a columna izquierda de cara izquierda

    # MOVER CARA ROJA
    def moverR(self, direccion):
        if direccion.upper() == 'H':
            self.horarioR()
        elif direccion.upper() == 'AH':
            for i in range(3):
                self.horarioR()

    def horarioR(self):
        self.cubo[0] = np.rot90(self.cubo[0], -1)  # gira cara posterior (Naranja)
        temp = np.copy(self.cubo[2][2])  # guarda la tercera fila de la cara superior (Blanco)
        self.cubo[2][2] = self.cubo[4][:, 2][::-1] # mueve columna 3 de cara izquierda a la tercera fila de cara superior
        self.cubo[4][:, 2] = self.cubo[3][0]  # mueve primera fila de cara inferior (Amarillo) a columna 3 de cara izquierda
        self.cubo[3][0] = self.cubo[5][:,0][::-1]  # mueve la primera columna de cara derecha a la primera fila de cara inferior
        self.cubo[5][:, 0] = temp  # mueve fila guardada a columna 1 de cara derecha

    # MOVER CARA AZUL
    def moverX(self, direccion):
        if direccion.upper() == 'H':
            self.horarioX()
        elif direccion.upper() == 'AH':
            for i in range(3):
                self.horarioX()

    def horarioX(self):
            self.cubo[5] = np.rot90(self.cubo[5], -1)  # gira cara X
            temp = np.copy(self.cubo[2][:, 2])  # guarda la ultima columna de la cara B
            self.cubo[2][:, 2] = self.cubo[0][:,2]  # mueve la ultima columna de cara frontal (R) a la ultima columna de cara superior
            self.cubo[0][:, 2] = self.cubo[3][:,2]  # mueve la ultima columna de cara inferior (A) a la ultima columna de cara frontal
            self.cubo[3][:, 2] = self.cubo[1][:, 0][::-1]  # mueve la primera columna de cara posterior (N) a la ultima columna de cara inferior
            self.cubo[1][:, 0] = temp[::-1]  # mueve fila guardada a la primera columna de la cara porterior

    # MOVER CARA VERDE
    def moverV(self, direccion):
        if direccion.upper() == 'H':
            self.horarioV()
        elif direccion.upper() == 'AH':
            for i in range(3):
                self.horarioV()

    def horarioV(self):
        self.cubo[4] = np.rot90(self.cubo[4], -1)  # gira cara posterior (Naranja)
        temp = np.copy(self.cubo[2][:, 0])  # guarda la primera columna de la cara superior (Blanco)
        self.cubo[2][:,0] = self.cubo[1][:,2][::-1]  # mueve columna 3 de cara posterior a la primera columna de cara superior
        self.cubo[1][:, 2] = self.cubo[3][:, 0][::-1]  #mueve la primera columna de cara inferior a la tercera columna de la cara posterior
        self.cubo[3][:, 0] = self.cubo[0][:,0]  # mueve la primera columna de cara frontal a la primera columna de cara inferior
        self.cubo[0][:, 0] = temp  # mueve fila guardada a columna izquierda de cara izquierda


    def imprimirCubo(self):
        self.mostrarMatriz(self.cubo[2])
        self.mostrarMatrizCaras(self.cubo[0], self.cubo[5], self.cubo[1], self.cubo[4])
        self.mostrarMatriz(self.cubo[3])


    def mostrarMatriz(self, matriz):
        fil = len(matriz)  # saber cuantas filas
        col = len(matriz[0])  # saber cuantas columnas
        for i in range(0, fil):
            for j in range(0, col):
                print(matriz[i][j], end="  ")
            print(end="|")
            print()


    def mostrarMatrizCaras(self, matriz1, matriz2, matriz3, matriz4):
        fil = len(matriz1)  # saber cuantas filas
        col = len(matriz1[0])  # saber cuantas columnas
        for i in range(0, fil):
            for j in range(0, col):
                print(matriz1[i][j], end="  ")
            print(end="|  ")
            for j in range(0, col):
                print(matriz2[i][j], end="  ")
            print(end="|  ")
            for j in range(0, col):
                print(matriz3[i][j], end="  ")
            print(end="|  ")
            for j in range(0, col):
                print(matriz4[i][j], end="  ")
            print(end="|  ")
            print()


def main():
    rubik = CuboRubik()
    print("Cubo inicial:")
    rubik.imprimirCubo()


    # Realizar algunas rotaciones

    rubik.rotar('N', 'horario')
    print("Rotacion Superior")
    rubik.imprimirCubo()
    rubik.rotar('N', 'antihorario')
    print()
    print("Rotacion Inferior ")
    rubik.imprimirCubo()
    print()
    print("DESORDENAR CUBO ")
    rubik.desordenar()
    rubik.imprimirCubo()
    print()

    rubik.movimientosAleatorios(5)
    rubik.imprimirCubo()
    print()
    # rubik.rotar('U', 'antihorario')
    #
    # print("Cubo después de las rotaciones:")
    # imprimir_cubo(rubik)



if __name__ == "__main__":
    main()


