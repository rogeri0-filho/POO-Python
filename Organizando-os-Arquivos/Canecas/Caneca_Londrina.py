from Canecas.Caneca_Principal import Caneca

class CanecaLondrina(Caneca):
        def __init__(self):
            self.nome = 'Caneca Londrina'
            self.logo = 'Bandeira de Londres'
            self.cor = 'Branca'
            self.status = 'Cheia'
            self.bebida = 'Chá'
            self.preco = 30.00

        def bonus(self):
            print('Você ganhou uma colher como bônus. Parabens!')

        # 'Burlando' o método beber da classe pai com o Polimorfismo
        def beber(self):
            self.status = 'Vazia'
            return 'Tomando o chá das 17h!'
