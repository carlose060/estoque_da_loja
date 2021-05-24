from produto import Produto


class Arquivo:
    """Classe para instanciar objetos que permitem manipular os arquivos que guardam informacoes sobre produtos da loja."""

    def carrega_produtos(self):
        """Esse metodo carrega os produtos toda vez que o programa eh iniciado."""
        itens = list()
        caminho_arquivo = 'estoque.csv'
        with open(caminho_arquivo, 'r') as file:
            produtos = file.read()
            #todos elemento em uma string
            produtos = produtos.split('\n')
            #uma lista com os elementos separados
        for indice in range(0,len(produtos)-1):
            produto = produtos[indice].split(';')
            #seperando os atributos para instanciar os objetos
            item = Produto(produto[0],produto[1],produto[2],produto[3])
            itens.append(item)
        return itens

    def cria_produto(self,produto,itens):
        """"Cria novos produto."""
        produto_string = produto.__str__()
        caminho_arquivo = 'estoque.csv'
        itens.append(produto)
        with open(caminho_arquivo, 'a') as file:
            file.write(produto_string)

    def remove_produto(self,produto,itens):
        '''Exclui o arquivo e o produto na lista.'''
        itens.remove(produto)
        todos_produtos = ''
        for item in itens:
            todos_produtos = todos_produtos+item.__str__()
        caminho_arquivo = 'estoque.csv'
        with open(caminho_arquivo, 'w') as file:
            file.write(todos_produtos)
        return True

    def remove_quantidade(self,nome,qt,itens):
        '''Remove do estoque uma quantidade x do produto.'''
        for elemento in itens:
            if elemento.get_nome() == nome:
                #Procurando o elemento na lista
                nova_quantidade = int(elemento.get_qt()) - int(qt)
                if nova_quantidade > 0:
                #Se quantidade for 0 ou menos, posso remover da lista
                    elemento.set_qt(nova_quantidade)
                    todos_produtos = ''
                    for item in itens:
                        todos_produtos = todos_produtos+item.__str__()
                    caminho_arquivo = 'estoque.csv'
                    with open(caminho_arquivo, 'w') as file:
                        file.write(todos_produtos)
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
                todos_produtos = ''
                for elemento in itens:
                    #Concatenação de todos os itens com a nova quantidade
                    todos_produtos = todos_produtos+elemento.__str__()
                caminho_arquivo = 'estoque.csv'
                with open(caminho_arquivo, 'w') as file:
                    file.write(todos_produtos)
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
                todos_produtos = ''
                for elemento in itens:
                    #Concatenação de todos os itens com o novo preço
                    todos_produtos = todos_produtos+elemento.__str__()
                caminho_arquivo = 'estoque.csv'
                with open(caminho_arquivo, 'w') as file:
                    file.write(todos_produtos)
                return True
        return False
