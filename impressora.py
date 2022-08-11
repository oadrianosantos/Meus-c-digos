import sys
class impressora (object):

    papeltot = 0
    vazio = False
    def __init__(self, papel = 0, INK_CAPACTY =1000, INK_USAGE =1):
        self.papel = papel
        self.INK_CAPACTY = INK_CAPACTY
        self.INK_USAGE = INK_USAGE

    def addpaper(self,x):
        self.papel += x
        return

    def getcourrentpaper (self):
        return print ("Qtd de papel", self.papel)

    def gettotpaperused(self):
        return print(self.papeltot)

    def ISinkout(self):
        if self.INK_CAPACTY == 0:
            print ("Recarregar cartucho")
            self.vazio = True
        return self.vazio

    def replaceINK(self):
        self.INK_CAPACTY = 1000
        return

    def printumlado (self, x):
       # while not self.vazio:
        self.INK_CAPACTY -= x*self.INK_USAGE
        self.papel -= x
        self.ISinkout()
        self.papeltot += x
        return

    def printdoislados (self, x):

        self.INK_CAPACTY -= 2*x*self.INK_USAGE
        self.papel -= x
        self.papeltot += x
        self.ISinkout()

        return



def main ():
    imp = impressora(50, 1000, 1)

    imp.printdoislados(25)
    imp.getcourrentpaper()
    imp.gettotpaperused()




if __name__ == '__main__':
    sys.exit(main())