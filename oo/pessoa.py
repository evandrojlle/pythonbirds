class Pessoa:
    def __init__(self, *pFilhos, pNome=None, pIdade=42):
        self.idade = pIdade
        self.nome = pNome
        self.filhos = list(pFilhos)

    def cumprimentar(self):
        return f'OPA {id(self)}'


if __name__ == '__main__':
    evandro = Pessoa(pNome='Evandro')
    jonas = Pessoa(pNome='Jonas')

    juca = Pessoa(evandro, jonas, pNome='Juca', pIdade=69)
    print(Pessoa.cumprimentar(juca))
    print(id(juca))
    print(juca.cumprimentar())
    print(juca.nome)
    print(juca.idade)
    print()
    print(f'Filhos de {juca.nome}:')
    for filho in juca.filhos:
        print(filho.nome)

    print('=====================')
    juca.sobrenome = 'Pirama'
    print(juca.__dict__)
    print('=====================')
    print(evandro.__dict__)
    print('=====================')
    del juca.filhos
    print(juca.__dict__)
