import shelve
from tkinter import *

class usuario(object):

    def __init__ (self, U):

        self.frame_email = Frame(U)
        self.frame_nome = Frame(U)
        self.frame1 = Frame(U)
        self.frame2 = Frame(U, pady = "10")
        self.framec = Frame(U)
        self.frame3 = Frame(U)

        self.frame_nome.pack()
        self.frame_email.pack()

        self.frame1.pack()
        self.framec.pack()
        self.frame2.pack()
        self.frame3.pack()


        self.nome = Label(self.frame_nome, text="Nome")
        self.nome_ = Entry(self.frame_nome)

        self.email = Label(self.frame_email, text="E-mail")
        self.email_ = Entry(self.frame_email)

        self.usu = Label(self.frame1, text="Usuário")
        self.usuario = Entry(self.frame1)
        self.senha_ = Label(self.frame1, text="Senha")
        self.senha = Entry(self.frame1, show="*")
        self.entra = Button(self.frame2, text="Entrar", bg="yellow", command=self.Verifica)
        self.novo = Button(self.frame2, text= "Novo", bg = "yellow", command = self.Novo_usu)
        self.cria = Button(self.frame2, text= "Criar", fg = "yellow", bg = "black", command = self.Cria)
        self.mens = Label(self.frame3.pack(), text="")

        self.lemb = False
        self.b_lembrar = Checkbutton(self.framec, text = "Lembrar-me", command = self.lembrar)

        self.voltar= Button(self.frame2, text = "Voltar", bg = "yellow", command = self.Inicio)

        self.usu.pack()
        self.usuario.pack()
        self.senha_.pack()
        self.senha.pack()
        self.b_lembrar.pack()
        self.entra.pack(side = LEFT)
        self.novo.pack()
        self.mens.pack()

        self.checa()

    def Destryoer(self):
        self.usu.destroy()
        self.usuario.destroy()
        self.senha_.destroy()
        self.senha.destroy()
        self.b_lembrar.destroy()
        self.entra.destroy()
        self.novo.destroy()
        self.mens.destroy()
        self.email.destroy()
        self.email_.destroy()
        self.nome.destroy()
        self.nome_.destroy()
        self.voltar.destroy()
        self.cria.destroy()


    def Limpatela(self):
        self.entra.pack_forget()
        self.b_lembrar.pack_forget()
        self.novo.pack_forget()

        self.email.pack()
        self.email_.pack()
        self.nome.pack()
        self.nome_.pack()

        self.voltar.pack(side = LEFT)
        self.cria.pack(side = LEFT)

    def Inicio (self):
        self.b_lembrar.pack()
        self.cria.pack_forget()
        self.email.pack_forget()
        self.email_.pack_forget()
        self.nome.pack_forget()
        self.nome_.pack_forget()
        self.voltar.pack_forget()


        self.usu["text"] = "Usuário"
        self.senha_["text"] = "Senha"

        self.cria.pack_forget()
        self.entra.pack(side=LEFT)
        self.novo.pack(side=LEFT)

    def checa (self):
        bd = shelve.open("a.db")

        if "lembrado__" not in bd:
            bd["lembrado__"] = ""


        if bd["lembrado__"] == "":
            pass
        else:
            lemb = bd["lembrado__"]
            u_su = bd[lemb]
            self.b_lembrar.select()
            self.lemb = not self.lemb
            self.usuario.insert(END, u_su[0])
            self.senha.insert(END, u_su[1])
        bd.close()

    def lembrar(self):
        bd = shelve.open("a.db")
        self.lemb = not self.lemb
        if self.lemb:
            lembrado = self.usuario.get().upper()
            bd["lembrado__"] = lembrado
        else:
            bd["lembrado__"] = ""
        bd.close()

    def Cria(self):
        bd = shelve.open("a.db")
        usu__ = self.usuario.get().upper()
        usu__u = self.usuario.get().upper()
        senha = self.senha.get()

        nome = self.nome_.get()
        email=self.email_.get()

        if usu__ == "" or senha =="" or nome =="" or email =="":
            self.mens["text"] = "Nenhum dos campos pode estar vazio!"
            self.mens["fg"] = "red"
        else:
            bd[usu__] = []
            x = bd[usu__]
            x.append(usu__u)
            x.append(senha)
            x.append(nome)
            x.append(email)
            bd[usu__] = x

            self.mens["text"] = "Usuário criado com sucesso!"
            self.usu["text"] = "Usuário"
            self.senha_["text"] = "Senha"

            self.usuario.delete(0, END)
            self.senha.delete(0,END)
            self.nome_.delete(0, END)
            self.email_.delete(0,END)

            self.Inicio()

        bd.close()

    def Novo_usu(self):
        global senha, usuario
        self.usuario.delete(0, END)
        self.senha.delete(0, END)
        self.Limpatela()
        self.usu["text"] = "Novo Usuário"
        self.senha_["text"] = "Nova Senha"

        self.mens["text"] = ""

    def Verifica (self):
        global senha, usuario, mens

        bd = shelve.open("a.db")
        self.senha1 = str(self.senha.get())
        self.usuario_ = self.usuario.get().upper()


        if self.usuario_ not in bd:
            self.mens["text"] = "Usuário Inválido!"
            self.mens["fg"] = "red"
            self.usuario.delete(0, END)
            self.senha.delete(0, END)
            bd.close()
            return
        if self.usuario_ in bd:
            x = bd[self.usuario_]
            senha_correta = x[1]
            if senha_correta == self.senha1 :
                self.mens["text"] = "Bem vindo" + " "+ str(self.usuario_) + "!"
                self.mens["fg"] = "green"
                self.usuario.delete(0, END)
                self.senha.delete(0, END)
                self.Destryoer()

                D = Tk()
                D.geometry("400x400")
                D.title('Login')
                desenho(D)
                D.mainloop()

                bd.close()
                return
            else:
                self.mens["text"] = "Senha inválida!"
                self.mens["fg"] = "red"
                self.usuario.delete(0, END)
                self.senha.delete(0, END)
                bd.close()
                return


class desenho(object):
    def __init__(self,D):


        self.frame1 = Frame()
        self.frame1.pack()

        self.frame2 = Frame()
        self.frame2.pack()

        self.b_esquerda = Button(D, text = "esquerda")
        self.b_cima = Button(D, text="cima")
        self.b_baixo = Button(D, text="baixo")
        self.b_direira = Button(D, text="direita")

        self.b_esquerda.pack(side = "left", anchor="sw")
        self.b_cima.pack(side = "left", anchor="sw")
        self.b_baixo.pack(side = "left", anchor="sw")
        self.b_direira.pack(side = "left", anchor="sw")

U = Tk()
U.geometry("220x260")
U.title('Login')
usuario(U)
U.mainloop()