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
        return f'Estou bebendo da {self.nome}'

    def encher(self):
        self.status = 'Cheia'
        return f'Estou enchendo a {self.nome}'

# Classe CanecaLondrina é criada e herda as propriedades da classe Caneca
class CanecaLondrina(Caneca):
        def __init__(self):
            self.nome = 'Caneca Londrina'
            self.logo = 'Bandeira de Londres'
            self.cor = 'Branca'
            self.status = 'Cheia'
            self.bebida = 'Chá'

        def bonus(self):
            print('Você ganhou uma colher como bônus. Parabens!')

        # 'Burlando' o método beber da classe pai com o Polimorfismo
        def beber(self):
            self.status = 'Vazia'
            return 'Tomando o chá das 17h!'

class CanecaAmericana(Caneca):
        def __init__(self):
            super().__init__('Caneca Americana', 'Bandeira E.U.A', 'Branca e Azul')
            self.bebida = 'Café'

        def aquecer(self):
            print(f'A: {self.nome} foi aquecida')
            
        # 'Burlando' o método beber da classe pai com o Polimorfismo
        def beber(self):
            return super().beber() + f' {self.bebida}'

caneca_americana = CanecaAmericana()

print(caneca_americana.beber())