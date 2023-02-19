class Caneca:
    # Comando estático, que servirá para todas as canecas
    formato = 'Cilindrico com alça.'

    # Comandos que se alteram de caneca para caneca
    def __init__(self, nome, logo, cor):
        self.nome = nome
        self.logo = logo
        self.cor = cor
        self.status = 'Cheia'

    def beber(self):
        self.status = 'Vazia'
        return f'Estou bebendo da caneca {self.nome}'

    def encher(self):
        self.status = 'Cheia'
        return f'Estou enchendo a caneca {self.nome}'

# Classe CanecaLondrina é criada e herda as propriedades da classe Caneca
class CanecaLondrina(Caneca):
        def __init__(self):
            self.nome = 'Caneca Londrina'
            self.logo = 'Bandeira de Londres'
            self.cor = 'Branca'
            self.status = 'Cheia'

        def bonus(self):
            print('Você ganhou uma colher como bônus. Parabens!')

class CanecaAmericana(Caneca):
        def __init__(self):
            super().__init__('Caneca Americana', 'Bandeira E.U.A', 'Branca e Azul')

        def aquecer(self):
            print(f'A: {self.nome} foi aquecida')
    

caneca1 = CanecaLondrina()
caneca2 = Caneca('Caneca - CANADA', 'Bandeira - ACER', 'Vermelho - Branco')
caneca3 = CanecaAmericana()

print('A: ', caneca1.nome, ', possui a logo: ', caneca1.logo, ', e as cores: ', caneca1.cor)
print('A: ', caneca2.nome, ', possui a logo: ', caneca2.logo, ', e as cores: ', caneca2.cor)
print('A: ', caneca3.nome, ', possui a logo: ', caneca3.logo, ', e as cores: ', caneca3.cor)


'''
caneca1.beber()
caneca1.encher()
caneca2.beber()
'''

print(caneca1.beber())
print(caneca1.encher())

print(caneca2.beber())

print('Status - Caneca 1: ', caneca1.status)
print('Formato - Caneca 2: ', caneca2.formato)
#print(caneca3.aquecer())
