from produto import Produto
import os
class Arquivo:

    def CarregaProd(self):
        todos = os.listdir('prod/')
        itens = list()
        for um_por_vez in todos:
            with open('prod/'+um_por_vez, 'r') as file:
                st = file.read()
            st = st.split(';')
            item = Produto(st[0],st[1],st[2],st[3])
            itens.append(item)
        return itens

    def NovoProd(self,produto,itens):
        texto = str(produto.getNome())+';'+str(produto.getQt())+';'+str(produto.getPreco())+';'+str(produto.getPreco_custo())+';'
        with open('prod/'+produto.getNome()+'.txt', 'w') as file:
            file.write(texto)
        itens.append(produto)

    def RemoverQt(self,nome,qt,itens):
        for elemento in itens:
            if elemento.getNome() == nome:
                if (int(elemento.getQt()) - int(qt)) > 0:
                    elemento.setQt(int(elemento.getQt()) - int(qt))  #Jeito alternativo e mais pratico para fazer a remoção
                    texto = str(elemento.getNome())+';'+str(elemento.getQt())+';'+str(elemento.getPreco())+';'+str(elemento.getPreco_custo())+';'
                    with open('prod/'+elemento.getNome()+'.txt', 'w') as file:
                        file.write(texto)
                    return True
                else:
                    os.remove('prod/'+elemento.getNome()+'.txt')
                    itens.remove(elemento) #del(elemento) so funcionava como indice, o antigo modo do for
                    return True
        return False      ##Não removeu, pois nao achou o elemento ou erro durante o codigo

    def AumentarQt(self,nome,qt,itens):
        for it in itens:
            if it.getNome() == nome:
                it.setQt(int(it.getQt())+ int(qt))
                texto = str(it.getNome())+';'+str(it.getQt())+';'+str(it.getPreco())+';'+str(it.getPreco_custo())+';'
                with open('prod/'+nome+'.txt', 'w') as file:
                    file.write(texto)
                return True
        return False



    def AlteraPreco(self,nome,preco,op,itens):
        for it in itens:
            if it.getNome() == nome:
                if int(op) == 1: #Preço de venda
                    it.setPreco(preco)
                else:  ## op = 0 preço de custo
                    it.setPreco_custo(preco)
                texto = str(it.getNome())+';'+str(it.getQt())+';'+str(it.getPreco())+';'+str(it.getPreco_custo())+';'
                with open('prod/'+nome+'.txt', 'w') as file:
                    file.write(texto)
                return True
        return False
