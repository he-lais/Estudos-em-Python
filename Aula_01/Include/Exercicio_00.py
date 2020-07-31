#Separar parte inteira de parte fracionada pegando do teclado
numero = input('Digite o numero: ')
inteira, fracionada = numero.split('.')
print(f'Parte inteira: {inteira}',f'\nParte decimal: 0.{fracionada}')


"""def separador(numero):
    inteira, fracionada = numero.split('.')
    return inteira, fracionada


def main():
    pass
    numero = input('Digite o numero: ')

    print(separador(numero))


if __name__ == '__main__':
    main() """
