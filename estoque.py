from produto import Produto

class Estoque:
  """Entidade para simular o controle do estoque."""

  def carrega_memoria(self):
      """Metodo que carrega todos os produtos para a memoria."""
      itens_na_memoria = list()
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
          itens_na_memoria.append(item)
      return itens_na_memoria

  def insere_produto(self,produto,itens_na_memoria):
      """É colocado no estoque um novo produto"""
      itens_na_memoria.append(produto)
      produto_string = produto.__str__()
      caminho_arquivo = 'estoque.csv'
      with open(caminho_arquivo, 'a') as file:
          file.write(produto_string)

  def retira_produto(self,produto,itens_na_memoria):
      """Retira o produto instanciado do estoque"""
      itens_na_memoria.remove(produto)
      todos_produtos = ''
      for item in itens_na_memoria:
          todos_produtos = todos_produtos+item.__str__()
      caminho_arquivo = 'estoque.csv'
      with open(caminho_arquivo, 'w') as file:
          file.write(todos_produtos)
      return True

  def retira_quantidade(self,nome,qt,itens_na_memoria):
      """Retira uma quantidade x de um produto"""
      for item in itens_na_memoria:
          if item.get_nome() == nome:
              nova_quantidade = int(item.get_qt()) - int(qt)
              if nova_quantidade > 0:
                  item.set_qt(nova_quantidade)
                  todos_produtos = ''
                  for elemento in itens_na_memoria:
                      todos_produtos = todos_produtos+elemento.__str__()
                  caminho_arquivo = 'estoque.csv'
                  with open(caminho_arquivo, 'w') as file:
                      file.write(todos_produtos)
                  return True
              else:
                  self.retira_produto(item,itens_na_memoria)
                  return True
      return False

  def aumenta_quantidade(self,nome,qt,itens_na_memoria):
      """Aumenta a quantidade do produto no estoque"""
      for item in itens_na_memoria:
          if item.get_nome() == nome:
              nova_quantidade = int(item.get_qt()) + int(qt)
              item.set_qt(nova_quantidade)
              todos_produtos = ''
              for elemento in itens_na_memoria:
                  todos_produtos = todos_produtos+elemento.__str__()
              caminho_arquivo = 'estoque.csv'
              with open(caminho_arquivo, 'w') as file:
                  file.write(todos_produtos)
              return True
      return False

  def altera_preco(self,nome,preco,op,itens_na_memoria):
      """Metodo para alterar preço de um produto no estoque"""
      for item in itens_na_memoria:
          if item.get_nome() == nome:
              if int(op) == 1: #opção 1 = preço de venda.
                  item.set_preco(preco)
              elif int(op) == 0:
                  item.set_preco_custo(preco)
              todos_produtos = ''
              for elemento in itens_na_memoria:
                  todos_produtos = todos_produtos+elemento.__str__()
              caminho_arquivo = 'estoque.csv'
              with open(caminho_arquivo, 'w') as file:
                  file.write(todos_produtos)
              return True
      return False
