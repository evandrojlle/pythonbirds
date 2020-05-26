class Pessoa:
    def __init__(self, pNome = None, pIdade = 42):
        self.idade = pIdade
        self.nome = pNome

    def cumprimentar(self):
        return f'OPA {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Juca', 69)
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Evandro'
    print(p.nome)
    print(p.idade)
