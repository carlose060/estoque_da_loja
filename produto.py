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
        return str(nome)+';'+str(qt)+';'+str(preco)+';'+str(preco_custo)+'\n'

  def __repr__(self):
      nome = self.get_nome()
      qt = self.get_qt()
      preco = self.get_preco()
      preco_custo = self.get_preco_custo()
      return 'Produto: '+str(nome)+'\nQuantidade: '+str(qt)+'\nPreço: '+str(preco)+'\nPreço custo: '+str(preco_custo)+'\n__________________________'

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
