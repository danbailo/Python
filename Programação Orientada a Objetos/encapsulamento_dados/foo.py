class Pessoa(object):
    def __init__(self, nome='Alguem'):
        self.__nome = nome #private
     
    @property #getter
    def nome(self): 
        return self.__nome

    @nome.setter #setter
    def nome(self, nome):
        self.__nome = nome

    def __str__(self):
        return self.nome # ou self.__nome

p = [Pessoa().nome, Pessoa(), Pessoa()]

print(p)