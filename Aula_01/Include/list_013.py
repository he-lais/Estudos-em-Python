""" Removendo elemento da lista (outra forma) """

lista = [10, 20, 30, 40, 50]

print('Antes da remocao: ', lista)

# Remove o elemento na POSICAO e retorna o valor
valor_removido = lista.pop(0)

print('Valor removido: ', valor_removido)
print('Apos a remocao: ', lista)

tamanho = len(lista)-1
removeUltimo = lista.pop(tamanho)

print(lista)
print (removeUltimo)

#remove por elemento
lista.remove(30)
print (lista)


#conta quantos tem

print('Quantidade:',lista.count(20))

lista.append(250)
print(lista)
lista.append(300)
print(lista)
