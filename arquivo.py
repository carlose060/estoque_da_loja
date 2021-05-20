from produto import Produto
import os


class Arquivo:
    """Classe para instanciar objetos que permitem manipular os arquivos que guardam informacoes sobre produtos da loja."""

    def carrega_produtos(self):
        """Esse metodo carrega os produtos toda vez que o programa eh iniciado."""
        produtos_armazenados = os.listdir('prod/')
        itens = list()

        for nome_produto in produtos_armazenados:
            caminho_arquivo = f'prod/{nome_produto}'
            with open(caminho_arquivo, 'r') as file:
                produto = file.read()
            produto = produto.split(';')
            item = Produto(produto[0],produto[1],produto[2],produto[3])
            itens.append(item)
        return itens

    def cria_produto(self,produto,itens):
        """"Cria novos produto."""
        texto = (str(produto.get_nome())+';'+str(produto.get_qt())+
                 ';'+str(produto.get_preco())+';'
                 + str(produto.get_preco_custo())+';')
        caminho_arquivo = f'prod/{produto.get_nome()}.txt'
        with open(caminho_arquivo, 'w') as file:
            file.write(texto)
        itens.append(produto)

    def remove_produto(self,produto,itens):
        '''Exclui o arquivo e o produto na lista.'''
        caminho_arquivo = 'prod/'+produto.get_nome()+'.txt'
        os.remove(caminho_arquivo)
        itens.remove(produto)
        return True

    def remove_quantidade(self,nome,qt,itens):
        '''Remove do estoque uma quantidade x do produto.'''
        for elemento in itens:
            if elemento.get_nome() == nome:
                nova_quantidade = int(elemento.get_qt()) - int(qt)
                if nova_quantidade > 0:
                    elemento.set_qt(nova_quantidade)
                    texto = (str(elemento.get_nome())+';'+str(elemento.get_qt())+
                             ';'+str(elemento.get_preco())+';'
                             + str(elemento.get_preco_custo())+';')
                    caminho_arquivo = f'prod/{elemento.get_nome()}.txt'
                    with open(caminho_arquivo, 'w') as file:
                        file.write(texto)
                    return True
                else:
                    self.remove_produto(elemento,itens)
                    return True
        return False      ##Não removeu, pois nao achou o elemento ou erro durante o codigo



    def aumenta_quantidade(self,nome,qt,itens):
        '''Aumenta do estoque uma quantidade x do produto.'''
        for item in itens:
            if item.get_nome() == nome:
                nova_quantidade = int(item.get_qt()) + int(qt)
                item.set_qt(nova_quantidade)
                texto = str(item.get_nome())+';'+str(item.get_qt())+';'+str(item.get_preco())+';'+str(item.get_preco_custo())+';'
                caminho_arquivo = f'prod/{nome}.txt'
                with open(caminho_arquivo, 'w') as file:
                    file.write(texto)
                return True
        return False

    def altera_preco(self,nome,preco,op,itens):
        '''Altera no arquivo e na lista o preco do produto.'''
        for item in itens:
            if item.get_nome() == nome:
                if int(op) == 1: #Preço de venda
                    item.set_preco(preco)
                else:  ## op = 0 preço de custo
                    item.set_preco_custo(preco)
                texto = str(item.get_nome())+';'+str(item.get_qt())+';'+str(item.get_preco())+';'+str(item.get_preco_custo())+';'
                caminho_arquivo = f'prod/{nome}.txt'
                with open(caminho_arquivo, 'w') as file:
                    file.write(texto)
                return True
        return False
