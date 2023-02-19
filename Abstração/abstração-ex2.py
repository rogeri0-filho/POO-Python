class Caneca:
    # Comando estático, que servirá para todas as canecas
    formato = 'Cilindrico com alça.'

    #__init__ é o método chamado pelo python sempre que um objeto for criado
    #Os parenteses dos objetos são colocados devido a necessidade do método init interno do python

    # O Init vai criar os objetos de acordo com o que for passado para eles serem feitos
    # Dentro do init são postas as coisas que são próprias dos objetos evitando conflito 
    #caso algo da classe que devereia ser único do a=objeto seja alterado

    # Comandos que se alteram de caneca para caneca
    def __init__(self, nome, logo, cor):
        self.nome = nome
        self.logo = logo
        self.cor = cor
        self.status = 'Cheia'

    def beber(self):
        self.status = 'Vazia'

    def encher(self):
        self.status = 'Cheia'


caneca1 = Caneca('Caneca - U.S.A', 'Bandeira - U.S.A', 'Azul - Vemelho')
caneca2 = Caneca('Caneca - CANADA', 'Bandeira - ACER', 'Vermelho - Branco')

print('A: ', caneca1.nome, ', possui a logo: ', caneca1.logo, ', e as cores: ', caneca1.cor)
print('A: ', caneca2.nome, ', possui a logo: ', caneca2.logo, ', e as cores: ', caneca2.cor)

caneca1.beber()
caneca1.encher()

caneca2.beber()

print('Status - Caneca 1: ', caneca1.status)
print('Status - Caneca 2: ', caneca2.status)
