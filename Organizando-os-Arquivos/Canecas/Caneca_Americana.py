from Canecas.Caneca_Principal import Caneca

class CanecaAmericana(Caneca):
        def __init__(self):
            super().__init__('Caneca Americana', 'Bandeira E.U.A', 'Branca e Azul')
            self.bebida = 'Café'
            self.preco = 35.00

        def aquecer(self):
            print(f'A: {self.nome} foi aquecida')
            
        # 'Burlando' o método beber da classe pai com o Polimorfismo
        def beber(self):
            return super().beber() + f' {self.bebida}'
