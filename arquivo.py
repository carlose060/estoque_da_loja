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
                if (int(elemento.getQt()) - qt) > 0:
                    with open('prod/'+elemento.getNome()+'.txt', 'r') as file:
                        st = file.read()
                    st = st.split(';')
                    st[1] =  int(st[1]) - qt
                    texto = str(st[0])+';'+str(st[1])+';'+str(st[2])+';'+str(st[3])+';'
                    with open('prod/'+st[0]+'.txt', 'w') as file:
                        file.write(texto)
                    elemento.setQt(int(elemento.getQt()) - qt)
                    break
                else:
                    os.remove('prod/'+elemento.getNome()+'.txt')
                    del(elemento)
                    break

    def AumentarQt(self,nome,qt,itens):
        with open('prod/'+nome+'.txt', 'r') as file:
            st = file.read()
        st = st.split(';')
        st[1] =  int(st[1]) + qt
        texto = str(st[0])+';'+str(st[1])+';'+str(st[2])+';'+str(st[3])+';'
        with open('prod/'+nome+'.txt', 'w') as file:
            file.write(texto)
        for it in itens:
            if it.getNome() == nome:
                it.setQt(int(it.getQt())+ qt)
                break



'''programa = Arquivo().CarregaProd()
for it in programa:
    print(it)
Arquivo().AumentarQt('cha',10,programa)
for it in programa:
    print(it)'''



'''neew = Produto('bola',20,20.5,10.0)
Arquivo().NovoProd(neew)
programa.append(neew)'''
