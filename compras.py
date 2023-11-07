lista_compras = ['sal', 'leite', 'arroz']


print("Lista de compras:")
for i, produto in enumerate(lista_compras):
    print(f"{i + 1} - {produto}")


novo_produto = input("Digite o produto que deseja adicionar: ")
lista_compras.append(novo_produto)
print(f"Item '{novo_produto}' adicionado à lista.")


if 'leite' in lista_compras:
    lista_compras.remove('leite')
    print("Item 'leite' removido da lista.")


if 'arroz' in lista_compras:
    indice_arroz = lista_compras.index('arroz')
    lista_compras[indice_arroz] = 'feijão'
    print("Item 'arroz' editado para 'feijão'.")


print("Lista de compras atualizada:")
for i, produto in enumerate(lista_compras):
    print(f"{i + 1} - {produto}")
