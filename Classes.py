class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def imprime (self, x, y):
        print ("(%1.1f,%1.1f)"%(x,y))
    def imprimeCentro (self, x, y):
        print ("Centro = (%1.1f,%1.1f)"%(x,y))

class Retangulo:
    def __init__(self, comprimento, largura, ponto):
        self.l = largura
        self.c = comprimento
        self.v = ponto.x
        self.v2= ponto.y
    def calculaCentro (self):
        centro = Ponto(((self.c+self.v)/2),(self.l+self.v2)/2)
        centro.imprimeCentro(centro.x, centro.y)

def Main ():
    ponto = Ponto (int(input("Digite ponto no eixo X:")), int(input("Digite ponto no eixo Y:")))
    global ret
    j = input ("Deseja criar retângulo?")

    if j == "s" or j =="sim" or j== "S" or j== "SIM":
        ret = Retangulo(int(input("Digite a comprimento:")), (int(input("Digite a largura:"))), ponto)
    else:
        return
    i = input("Deseja atualizar retângulo ou Calcular centro?")

    if i == "A" or "a":
        ret = Retangulo(int(input("Digite a comprimento:")), (int(input("Digite a largura:"))), ponto)
    ret.calculaCentro()
Main()