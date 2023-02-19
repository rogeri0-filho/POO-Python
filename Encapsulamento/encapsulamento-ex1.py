class Caneca:
    # Comando estático, que servirá para todas as canecas
    formato = 'Cilindrico com alça.'

    # Comandos que se alteram de caneca para caneca
    def __init__(self, nome, logo, cor):
        self.nome = nome
        self.logo = logo
        self.cor = cor
        self.status = 'Cheia'
        self.__preco_fabrica = 20.00 #forma correta de se fazer um encapsulamento de uma classe privada
        self.preco = 25.00

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
            self.preco = 30.00

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
            self.preco = 35.00

        def aquecer(self):
            print(f'A: {self.nome} foi aquecida')
            
        # 'Burlando' o método beber da classe pai com o Polimorfismo
        def beber(self):
            return super().beber() + f' {self.bebida}'


print('PROMOÇÃO!!')
caneca1 = CanecaAmericana()
caneca2 = CanecaLondrina()
caneca3 = Caneca('Caneca Canadense', 'Folha de Acer', 'Vermelho')

print(f'\nPreço Atual das canecas:      '
      f'\nLondrina  - R$  {caneca1.preco} '
      f'\nAmericana - R$  {caneca2.preco} '
      f'\nCanadense - R$  {caneca3.preco}')

caneca1.preco = caneca1.preco - 5
caneca2.preco = caneca2.preco - 5
caneca3.preco = caneca3.preco - 5

print(f'\nNovo preço das canecas:'
      f'\nLondrina  - R$  {caneca1.preco} '
      f'\nAmericana - R$  {caneca2.preco} '
      f'\nCanadense - R$  {caneca3.preco}\n')


# tentando acessar o método "privado" dessa forma, gera um código de erro de Objeto Não Atribuído
#print(caneca3.__preco_fabrica)

# Dessa forma, o pyhton "Burla o programa"
print(f'Peço de fábrica: {caneca3._Caneca__preco_fabrica}')

# Burlando novamente
caneca3._Caneca__preco_fabrica = 10.00
print(f'Novo peço de fábrica: {caneca3._Caneca__preco_fabrica}')