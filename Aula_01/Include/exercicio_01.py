nome = input('Qual o seu nome? ')
print('Silva' in nome)#não precisa de return

nome = input('Qual o seu nome? ')
if ('Silva' in nome):
    print('Contém a palavra')
else:
    print('Não contém Silva no seu nome')

#também pode ser usado em lista

lista = [1,25,50]
print('contem o numero 3 na lista?', 3 in lista)