
def mensagem():
    return "Olá, Mundo!"

class Turma:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def texto(self):
        print(f"O meu nome é {self.nome} e meu sobrenome é {self.sobrenome}")

# Criando uma instância da classe Turma
aluno1 = Turma("Vitoria", "Santos")

# Acessando os atributos e método da instância
print(aluno1.nome)
print(aluno1.sobrenome)
aluno1.texto()

