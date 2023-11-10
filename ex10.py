def soma(a, b):
    return a + b

resultado = soma(3, 5)
print(resultado)

def saudacao():
    return "Olá, mundo!"

mensagem = saudacao()
print(mensagem)

def nome(nome):
    print(f"Olá, {nome}!")

nome("Alice")

def limparTela():
    import os
    os.system("cls")

limparTela()
print("Boa noite estudantes.")