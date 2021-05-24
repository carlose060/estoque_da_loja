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
