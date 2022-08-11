import random

def main():
    global matriz
    matriz =[]
    global jogar
    ConstroiMatriz()
    ImprimeMatriz(matriz)
    jogar = (int(input("Deseja jogar (1) ou desistir (0)? \n")))
    while jogar == 1:
        pos_1 = input("poisção 1 \n")
        pos_2 = input("posição 2 \n")
        pos1 = []
        pos1.append(int(pos_1[0]))
        pos1.append(int(pos_1[1]))
        pos2 = []
        pos2.append(int(pos_2[0]))
        pos2.append(int(pos_2[1]))
        if VerificaJogada(pos1, pos2, matriz) is True:
            Troca(pos1, pos2, matriz)
            ImprimeMatriz (matriz)
        else:
            print("jogada inválida")
        if VerificaseGanhou(matriz) is True:
            print("Você Ganhou")
            return
        jogar = (int(input("Deseja jogar (1) ou desistir (0)?")))
    print ("Você Destiu")

def ConstroiMatriz():
    lista = list(range(16))
    for i in range(4):
        linha =[]
        for j in range(4):
            elem = random.choice(lista)
            linha.append(elem)
            lista.remove(elem)
        matriz.append(linha)

def ImprimeMatriz (matriz):
    for i in range(len(matriz)):
        linha = ""
        for j in range (len(matriz[i])):
            linha += " " + ("%3.2s"%(str(matriz[i][j])))
        print("%s" %(linha))


def VerificaJogada (pos1, pos2, matriz):
    if matriz[(pos1[0])-1][(pos1[1])-1] == 0 or matriz[(pos2[0])-1][(pos2[1])-1] == 0:
        if (pos1[0] == pos2[0] and ((pos1[1]== pos2[1]+1) or pos1[1]==pos2[1]-1)) or (pos1[1] == pos2[1] and ((pos1[0]== pos2[0]+1) or pos1[0]==pos2[0]-1)):
            return True
        else:
            return
    else:
        return

def Troca (pos1, pos2, matriz):
    temp = matriz [(pos1[0])-1][(pos1[1])-1]
    matriz[(pos1[0]) - 1][(pos1[1]) - 1] = matriz[(pos2[0])-1][(pos2[1])-1]
    matriz[(pos2[0]) - 1][(pos2[1]) - 1] = temp

def VerificaseGanhou(matriz):
    matriz_c = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0 ]]
    i =0
    while i < 4:
        j = 0
        while j <4:
            if matriz_c[i][j]== matriz[i][j]:
                j = j + 1
            else:
                return
        i = i + 1
    return True

main()