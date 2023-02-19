#Classe
class Caneca:
    #Propriedades
    logo = ''
    cor = ''
    nome = ''

    #Métodos:
    #self define qual objeto está chamando o método
    #self.nome faz pegar o nome da caneca espécifica
    def beber(self):
        print('Estou bebendo da caneca: ', self.nome)

#Objeto = Classe
caneca_1 = Caneca()

#Objeto.Propriedade
caneca_1.cor = 'Verde'
caneca_1.logo = 'Logo'
caneca_1.nome = 'Teste'

print(caneca_1.cor, caneca_1.nome, caneca_1.logo)
caneca_1.beber

# A propriedade logo foi alterada fora da classe, e toda variável que a chamar 
# após essa mudança vai ter ela com esse novo nome
Caneca.logo = "Padrão"

caneca_2 = Caneca()
print(caneca_2.logo)