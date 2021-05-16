from tkinter import *
from produto import Produto
from arquivo import Arquivo
class Programa:

    def limpaTela(self):
        list = self.fr.grid_slaves()
        for l in list:
            l.destroy()

    def printp(self):
        Label(self.fr,fg="blue",text='Produtos em estoque').grid(row=0)
        for i in range(len(self.list_itens)):
            Label(self.fr,fg="black",text=self.list_itens[i]).grid(row=1+i)


    def pInserir(self):
        para_inserir = Produto(self.t1.get(),self.t2.get(),self.t3.get(),self.t4.get())
        self.arq.NovoProd(para_inserir,self.list_itens)
        self.widgetsMenuMain()
        Label(self.fr,text="Produto inserido com sucesso", fg="blue").grid(column=1,row=5)

    def pAumentar(self):
        if self.arq.AumentarQt(self.t1.get(),self.t2.get(),self.list_itens):
            self.widgetsMenuMain()
            Label(self.fr,text="Adicionado ao estoque", fg="blue").grid(column=1,row=5)
        else:
            self.widgetsMenuMain()
            Label(self.fr,text="O Produto nao foi Aumentado :(", fg="blue").grid(column=1,row=5)


    def pRemover(self):
        if self.arq.RemoverQt(self.t1.get(),self.t2.get(),self.list_itens):
            self.widgetsMenuMain()
            Label(self.fr,text="Produto removido com sucesso", fg="blue").grid(column=1,row=5)
        else:
            self.widgetsMenuMain()
            Label(self.fr,text="O Produto nao foi Removido :(", fg="blue").grid(column=1,row=5)

    def pAlterar(self):
        if self.arq.AlteraPreco(self.t1.get(),self.t2.get(),self.t3.get(),self.list_itens):
            self.widgetsMenuMain()
            Label(self.fr,text="Preço alterado", fg="blue").grid(column=1,row=5)
        else:
            self.widgetsMenuMain()
            Label(self.fr,text="Não foi possivel alterar", fg="blue").grid(column=1, row=5)

    def widgetAlterar(self):
        self.limpaTela()
        self.printp()
        self.t1 = StringVar()
        self.t2 = StringVar()
        self.t3 = StringVar()
        Label(self.fr,text="Nome do produto").grid(column=1,row=0)
        Entry(self.fr, textvariable= self.t1).grid(column=1, row=1)
        Label(self.fr,text="Novo valor").grid(column=1,row=2)
        Entry(self.fr,textvariable=self.t2).grid(column=1,row=3)
        Radiobutton(self.fr, text="Preço de venda",value=1,variable=self.t3).grid(column=1,row=4)
        Radiobutton(self.fr, text="Preço de Custo",value=0,variable=self.t3).grid(column=1,row=5)
        Button(self.fr,text="Alterar",command=self.pAlterar).grid(column=1,row=6)
        Button(self.fr,text="Voltar",command=self.widgetsMenuMain).grid(column=1,row=7)

    def widgetRecolherDados(self):
        self.limpaTela()
        self.printp()
        self.t1 = StringVar()
        self.t2 = StringVar()
        Label(self.fr,text="Nome do produto").grid(column=1,row=0)
        Entry(self.fr,textvariable=self.t1).grid(column=1,row=1)
        Label(self.fr, text="Quantidade").grid(column=1,row=2)
        Entry(self.fr,textvariable=self.t2).grid(column=1,row=3)


    def widgetRemover(self):
        self.widgetRecolherDados()
        Button(self.fr,text="Remover", fg="red",command=self.pRemover).grid(column=1,row=4)
        Button(self.fr,text="Voltar", command=self.widgetsMenuMain).grid(column=1,row=5)



    def widgetAumentar(self):
        self.widgetRecolherDados()
        Button(self.fr,text="Inserir",command=self.pAumentar).grid(column=1,row=4)
        Button(self.fr,text="Voltar",command=self.widgetsMenuMain).grid(column=1,row=5)


    def widgetInserir(self):
        self.limpaTela()
        self.printp()
        self.t1 = StringVar()
        self.t2 = StringVar()
        self.t3 = StringVar()
        self.t4 = StringVar()
        Label(self.fr,text="Nome do produto").grid(column=1,row=0)
        Entry(self.fr,textvariable=self.t1).grid(column=1,row=1)
        Label(self.fr, text="Quantidade no estoque").grid(column=1,row=2)
        Entry(self.fr,textvariable=self.t2).grid(column=1,row=3)
        Label(self.fr,text="Valor de venda").grid(column=1,row=4)
        Entry(self.fr,textvariable=self.t3).grid(column=1,row=5)
        Label(self.fr,text="Valor de custo").grid(column=1,row=6)
        Entry(self.fr,textvariable=self.t4).grid(column=1,row=7)
        Button(self.fr,text="Inserir", command= self.pInserir).grid(column=1,row=8)
        Button(self.fr,text="Voltar", command = self.widgetsMenuMain).grid(column=1,row=9)


    def widgetMenuIns(self):
        self.limpaTela()
        self.printp()
        Button(self.fr,text="Novo produto",command=self.widgetInserir).grid(column=1, row=0)
        Button(self.fr,text="Aumentar estoque",command=self.widgetAumentar).grid(column=1, row=1)
        Button(self.fr,text="Voltar", command= self.widgetsMenuMain).grid(column=1, row=2)

    def widgetsMenuMain(self):
        self.arq = Arquivo()
        self.list_itens = self.arq.CarregaProd()
        self.limpaTela()
        self.printp()
        Button(self.fr, text="Inserir em estoque",command = self.widgetMenuIns).grid(column=1,row=0)
        Button(self.fr, text="Remover em estoque",command= self.widgetRemover).grid(column=1,row=1)
        Button(self.fr, text="Alterar preço",command=self.widgetAlterar).grid(column=1,row=2)
        Button(self.fr, text="SAIR", fg="red", command = root.destroy).grid(column=1,row=3)


    def __init__(self,root):
        self.fr = Frame(root)
        self.fr.pack()

        self.widgetsMenuMain()


root = Tk()
Programa(root)
root.mainloop()
