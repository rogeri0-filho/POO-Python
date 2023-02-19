from Canecas.Caneca_Americana import CanecaAmericana
from Canecas.Caneca_Londrina import CanecaLondrina
from Canecas.Caneca_Principal import Caneca


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