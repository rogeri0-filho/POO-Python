class Caneca:
    # Comando estático, que servirá para todas as canecas
    formato = 'Cilindrico com alça.'
    __preco_fabrica = 20.00 #forma correta de se fazer um encapsulamento de uma classe privada

    # Comandos que se alteram de caneca para caneca
    def __init__(self, nome, logo, cor):
        self.nome = nome
        self.logo = logo
        self.cor = cor
        self.status = 'Cheia'
        self.preco = 25.00

    def beber(self):
        self.status = 'Vazia'
        return f'Estou bebendo da {self.nome}'

    def encher(self):
        self.status = 'Cheia'
        return f'Estou enchendo a {self.nome}'
