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
        produto_string = (str(produto.get_nome())+';'+str(produto.get_qt())+
                 ';'+str(produto.get_preco())+';'
                 + str(produto.get_preco_custo())+'\n')
        caminho_arquivo = 'estoque.csv'
        with open(caminho_arquivo, 'r') as file:
            todos_produtos= file.read()
            #Todos os produtos salvos ate o momento
            todos_produtos= todos_produtos+produto_string
            #Concateno com o novo produto
        with open(caminho_arquivo, 'w') as file:
            file.write(todos_produtos)
        itens.append(produto)

    def remove_produto(self,produto,itens):
        '''Exclui o arquivo e o produto na lista.'''
        produto_string = (str(produto.get_nome())+';'+str(produto.get_qt())+
                 ';'+str(produto.get_preco())+';'
                 + str(produto.get_preco_custo())+'\n')
        caminho_arquivo = 'estoque.csv'
        with open(caminho_arquivo, 'r') as file:
            todos_produtos= file.read()
            todos_produtos= todos_produtos.split(produto_string)
            #Removendo o produto do .csv, vira uma lista com dois item
            print(todos_produtos)
            print(len(todos_produtos))
            produto_string= todos_produtos[0]+todos_produtos[1]
            #Junta os dois itens em uma string para inserir no .csv
        with open(caminho_arquivo, 'w') as file:
            file.write(produto_string)
        itens.remove(produto)
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
                    produto_string = ''
                    for item in itens:
                        #Concatenação de todos os itens
                        produto_string = (produto_string+str(item.get_nome())+';'+str(item.get_qt())+
                             ';'+str(item.get_preco())+';'
                             + str(item.get_preco_custo())+'\n')
                    caminho_arquivo = 'estoque.csv'
                    with open(caminho_arquivo, 'w') as file:
                        file.write(produto_string)
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
                produto_string = ''
                for elemento in itens:
                    #Concatenação de todos os itens com a nova quantidade
                    produto_string = produto_string+str(elemento.get_nome())+';'+str(elemento.get_qt())+';'+str(elemento.get_preco())+';'+str(elemento.get_preco_custo())+'\n'
                caminho_arquivo = 'estoque.csv'
                with open(caminho_arquivo, 'w') as file:
                    file.write(produto_string)
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
                produto_string = ''
                for elemento in itens:
                    #Concatenação de todos os itens com o novo preço
                    produto_string = produto_string+str(elemento.get_nome())+';'+str(elemento.get_qt())+';'+str(elemento.get_preco())+';'+str(elemento.get_preco_custo())+'\n'
                caminho_arquivo = 'estoque.csv'
                with open(caminho_arquivo, 'w') as file:
                    file.write(produto_string)
                return True
        return False
