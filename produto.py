class Produto:

  def __init__(self,nome,qt,preco,preco_custo):
    self.__nome = nome
    self.__qt = qt
    self.__preco = preco
    self.__preco_custo = preco_custo

  def __str__(self):
        nome = self.getNome()
        qt = self.getQt()
        preco = self.getPreco()
        preco_custo = self.getPreco_custo()
        return 'Produto = '+nome+'\nQuantidade = '+ str(qt) +'\nValor = '+str(preco) +'\nPreco de Custo = '+str(preco_custo)+'\n__________________'

  def getNome(self):
    return self.__nome

  def getQt(self):
    return self.__qt

  def getPreco(self):
    return self.__preco

  def getPreco_custo(self):
    return self.__preco_custo

  def setNome(self,novo_nome):
    self.__nome = novo_nome

  def setQt(self,nova_qt):
    self.__qt = nova_qt

  def setPreco(self,novo_preco):
    self.__preco = novo_preco

  def setPreco_custo(self,novo_preco_custo):
    self.__preco_custo = novo_preco_custo
