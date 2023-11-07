# lista inicial
lista_compras = ['sal', 'leite', 'arroz',]

# Mostra a lista de compras
print("Lista de compras:")
for i, produto in enumerate(lista_compras):
    print(f"{i + 1} - {produto}")

# Loop para adicionar itens à lista
while True:
    novo_produto = input("Digite o produto que deseja adicionar (ou 'sair' para finalizar): ")
    if novo_produto.lower() == 'sair':
        break
    lista_compras.append(novo_produto)
    print(f"Item '{novo_produto}' adicionado à lista.")

# Opção de apagar o item 'leite'
if 'leite' in lista_compras:
    lista_compras.remove('leite')
    print("Item 'leite' removido da lista.")

# Opção de editar o item 'arroz' para 'feijão'
if 'arroz' in lista_compras:
    indice_arroz = lista_compras.index('arroz')
    lista_compras[indice_arroz] = 'feijão'
    print("Item 'arroz' editado para 'feijão'.")

# Mostra a lista de compras atualizada
print("Lista de compras atualizada:")
for i, produto in enumerate(lista_compras):
    print(f"{i + 1} - {produto}")