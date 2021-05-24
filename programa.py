from tkinter import *
from produto import Produto
from arquivo import Arquivo


class Programa:
    '''Classe responsavel pela interface grafica'''

    def limpa_tela(self):
        list = self.fr.grid_slaves()
        for l in list:
            l.destroy()

    def printar_produtos(self):
        '''Mostra todos os produtos na coluna 0.'''
        Label(self.frame1,fg="blue",text='Produtos em estoque').grid(row=0)
        for i in range(len(self.list_itens)):
            Label(self.frame1,fg="black",text=repr(self.list_itens[i])).grid(row=1+i)


    def inserir(self):
        '''Cria um objeto e chama o metodo responsavel por salver o produto.'''
        para_inserir = Produto(self.t1.get(),self.t2.get(),self.t3.get(),self.t4.get())
        self.arquivo.cria_produto(para_inserir,self.list_itens)
        self.widget_menu_principal()
        Label(self.fr,text="Produto inserido com sucesso", fg="blue").grid(column=1,row=5)

    def aumentar(self):
        if self.arquivo.aumenta_quantidade(self.t1.get(),self.t2.get(),self.list_itens):
            self.widget_menu_principal()
            Label(self.fr,text="Adicionado ao estoque", fg="blue").grid(column=1,row=5)
        else:
            self.widget_menu_principal()
            Label(self.fr,text="O Produto nao foi Aumentado :(", fg="blue").grid(column=1,row=5)

    def remover(self):
        if self.arquivo.remove_quantidade(self.t1.get(),self.t2.get(),self.list_itens):
            self.widget_menu_principal()
            Label(self.fr,text="Produto removido com sucesso", fg="blue").grid(column=1,row=5)
        else:
            self.widget_menu_principal()
            Label(self.fr,text="O Produto nao foi Removido :(", fg="blue").grid(column=1,row=5)

    def alterar(self):
        if self.arquivo.altera_preco(self.t1.get(),self.t2.get(),self.t3.get(),self.list_itens):
            self.widget_menu_principal()
            Label(self.fr,text="Preço alterado", fg="blue").grid(column=1,row=5)
        else:
            self.widget_menu_principal()
            Label(self.fr,text="Não foi possivel alterar", fg="blue").grid(column=1, row=5)

    def widget_alterar(self):
        '''Metodo para recolher informacoes para alterar o preco.'''
        self.limpa_tela()
        self.printar_produtos()
        self.t1 = StringVar()
        self.t2 = StringVar()
        self.t3 = StringVar()
        Label(self.fr,text="Nome do produto").grid(column=1,row=0)
        Entry(self.fr, textvariable= self.t1).grid(column=1, row=1)
        Label(self.fr,text="Novo valor").grid(column=1,row=2)
        Entry(self.fr,textvariable=self.t2).grid(column=1,row=3)
        Radiobutton(self.fr, text="Preço de venda",value=1,variable=self.t3).grid(column=1,row=4)
        Radiobutton(self.fr, text="Preço de Custo",value=0,variable=self.t3).grid(column=1,row=5)
        Button(self.fr,text="Alterar",command=self.alterar).grid(column=1,row=6)
        Button(self.fr,text="Voltar",command=self.widget_menu_principal).grid(column=1,row=7)

    def widget_recolhe_dados(self):
        '''Metodo auxiliar para re-utilizacao de codigo.'''
        self.limpa_tela()
        self.printar_produtos()
        self.t1 = StringVar()
        self.t2 = StringVar()
        Label(self.fr,text="Nome do produto").grid(column=1,row=0)
        Entry(self.fr,textvariable=self.t1).grid(column=1,row=1)
        Label(self.fr, text="Quantidade").grid(column=1,row=2)
        Entry(self.fr,textvariable=self.t2).grid(column=1,row=3)


    def widget_remover(self):
        '''Metodo para recolher informacoes para remover o produto.'''
        self.widget_recolhe_dados()
        Button(self.fr,text="Remover", fg="red",command=self.remover).grid(column=1,row=4)
        Button(self.fr,text="Voltar", command=self.widget_menu_principal).grid(column=1,row=5)



    def widget_aumentar(self):
        '''Metodo para recolher informacoes para aumentar o preco.'''
        self.widget_recolhe_dados()
        Button(self.fr,text="Inserir",command=self.aumentar).grid(column=1,row=4)
        Button(self.fr,text="Voltar",command=self.widget_menu_principal).grid(column=1,row=5)


    def widget_inserir(self):
        '''Metodo para recolher informacoes para inserir novo produto.'''
        self.limpa_tela()
        self.printar_produtos()
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
        Button(self.fr,text="Inserir", command= self.inserir).grid(column=1,row=8)
        Button(self.fr,text="Voltar", command = self.widget_menu_principal).grid(column=1,row=9)


    def widget_menu_inserir(self):
        '''Menu de escolha para direcionamento novo produto ou aumentar estoque.'''
        self.limpa_tela()
        self.printar_produtos()
        Button(self.fr,text="Novo produto",command=self.widget_inserir).grid(column=1, row=0)
        Button(self.fr,text="Aumentar estoque",command=self.widget_aumentar).grid(column=1, row=1)
        Button(self.fr,text="Voltar", command= self.widget_menu_principal).grid(column=1, row=2)

    def widget_menu_principal(self):
        '''Meunu principal onde eh iniciado o programa.'''
        self.limpa_tela()
        self.printar_produtos()
        Button(self.fr, text="Adicionar em estoque",command = self.widget_menu_inserir).grid(row=0)
        Button(self.fr, text="Remover em estoque",command= self.widget_remover).grid(row=1)
        Button(self.fr, text="Alterar preço",command=self.widget_alterar).grid(row=2)
        Button(self.fr, text="SAIR", fg="red", command = root.destroy).grid(row=3,padx=65)


    def __init__(self,root):
        self.fr = PanedWindow(root,borderwidth=1,relief='solid')
        self.fr.place(x=5, y=5,width=190,height=590)
        self.frame1 = PanedWindow(root,borderwidth=1,relief='solid')
        self.frame1.place(x=205, y=5,width=190,height=590)
        self.arquivo = Arquivo()
        self.list_itens = self.arquivo.carrega_produtos()
        self.widget_menu_principal()



root = Tk()
root.title('Controle do Estoque')
root.geometry('400x600')
Programa(root)
root.mainloop()
