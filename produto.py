class Produto:

  def __init__(self,nome,qt,preco,preco_custo):
    self.__nome = nome
    self.__qt = qt
    self.__preco = preco
    self.__preco_custo = preco_custo

  def __str__(self):
        nome = self.get_nome()
        qt = self.get_qt()
        preco = self.get_preco()
        preco_custo = self.get_preco_custo()
        return 'Produto = '+nome+'\nQuantidade = '+ str(qt) +'\nValor = '+str(preco) +'\nPreco de Custo = '+str(preco_custo)+'\n__________________'

  def get_nome(self):
    return self.__nome

  def get_qt(self):
    return self.__qt

  def get_preco(self):
    return self.__preco

  def get_preco_custo(self):
    return self.__preco_custo

  def set_nome(self,novo_nome):
    self.__nome = novo_nome

  def set_qt(self,nova_qt):
    self.__qt = nova_qt

  def set_preco(self,novo_preco):
    self.__preco = novo_preco

  def set_preco_custo(self,novo_preco_custo):
    self.__preco_custo = novo_preco_custo
