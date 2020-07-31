palavra = 'ABCD'

primeira_letra = palavra[0]

# string = palavra[inicio : fim: passo]
pedaco_1 = palavra[0::-1]
pedaco_2 = palavra[1::-1]
pedaco_3 = palavra[2::-1]
pedaco_4 = palavra[3::-1]
inverte = palavra [::-1]

print('String: ', palavra)
print('Primeira letra: ', primeira_letra)
print('Pedaco 1: ', pedaco_1)
print('Pedaco 2: ', pedaco_2)
print('Pedaco 3: ', pedaco_3)
print('Pedaco 4: ', pedaco_4)
print('Palavra invertida: ', inverte)

"""
CONCATENAÇÃO

a = 'Ciencia'
b = 'Da'
c = 'Computação'


s = """
"Mc Donald's"
"""

concatecanao = f'{s} {b} {c}'


print(a)
print(b)
print(c)
print(concatecanao)

=========================================
palavra = 'ABCD'

primeira_letra = palavra[0]

# string = palavra[inicio : fim]
pedaco_1 = palavra[0:4]
pedaco_2 = palavra[1:4]
pedaco_3 = palavra[2:4]
pedaco_4 = palavra[3:4]

print('String: ', palavra)
print('Primeira letra: ', primeira_letra)
print('Pedaco 1: ', pedaco_1)
print('Pedaco 2: ', pedaco_2)
print('Pedaco 3: ', pedaco_3)
print('Pedaco 4: ', pedaco_4)

print()

# string = palavra[inicio : fim]
pedaco_1 = palavra[0:]
pedaco_2 = palavra[1:]
pedaco_3 = palavra[2:]
pedaco_4 = palavra[3:]

print('String: ', palavra)
print('Primeira letra: ', primeira_letra)
print('Pedaco 1: ', pedaco_1)
print('Pedaco 2: ', pedaco_2)
print('Pedaco 3: ', pedaco_3)
print('Pedaco 4: ', pedaco_4)

"""
