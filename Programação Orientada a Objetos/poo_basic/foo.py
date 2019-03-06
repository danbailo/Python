class Transporte(object): #superclasse
    def __init__(self, nome='Fusca', peso=5000, preco=3200.50):
        self.nome = nome
        self.peso = peso
        self.preco = preco
    
    def get_Nome(self):
        return self.nome
    
    def get_Peso(self):
        return self.peso
   
    def get_Preco(self):
        return self.preco

    def __str__(self):
        return 'Nome: ' + self.nome + ', Peso: {} e Preço: {}'.format(self.peso,self.preco)

class Carro(Transporte): #subclasse
    def __init__(self,nome,peso,preco,preco_seguro=1000):
        Transporte.__init__(self,nome,peso,preco)
        self.preco_seguro = preco_seguro
    
    def get_PrecoSeguro(self):
        return self.preco_seguro

    def __str__(self):
        return 'Nome: ' + self.nome + ', Peso: {}, Preço: {} e Preço Seguro: {}'.format(self.peso,self.preco,self.preco_seguro)

t = Transporte('Aviao', 1e6, 3.2e5)

print(t)

c = Carro('Uno',5000,15000.00)

print(c)

# print(t.nome)
# print(t.peso)
# print(t.preco)