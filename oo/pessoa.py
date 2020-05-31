class Pessoa:
    olhos = 2;

    def __init__(self, pNome=None, pIdade=42, *pFilhos):
        self.nome = pNome
        self.idade = pIdade
        self.filhos = list(pFilhos)

    def cumprimentar(self):
        return f'OPA {id(self)}'


if __name__ == '__main__':
    print('==========METODOS==========')
    p = Pessoa()
    print(Pessoa.cumprimentar(p)) #FORMA NAO USUAL.
    print(id(p))
    print(p.cumprimentar()) #FORMA USUAL.
    print()

    print('==========ATRIBUTO DE DADOS==========')
    print(p.nome)
    p.nome = "Evandro"
    print(p.nome)

    p2 = Pessoa('Leandro', 37)
    print(p2.nome)
    print(p2.idade)
    print()

    print('==========ATRIBUTO COMPLEXO  ==========')
    p3 = Pessoa('Renato', 65, p, p2)
    print(f'Filhos de {p3.nome}:')
    for filho in p3.filhos:
        print(filho.nome)
    print()

    print('==========ATRIBUTOS DINAMICOS  ==========')
    #p3.sobrenome # RESPONDE COM ERRO INFORMANDO QUE O ATRIBUTO NAO EXISTE.
    p3.sobrenome = 'de Oliveira' # CRIADO EM TEMPO DE EXECUCAO.
    print(p3.sobrenome)

    print(p3.__dict__)
    print(p2.__dict__)
    del p3.filhos
    print(p3.__dict__)
    print()

    print('==========ATRIBUTOS DE CLASSE  ==========')
    print(Pessoa.olhos)
    print(p.olhos)
    print(p2.olhos)
    print(p3.olhos)
    print(id(Pessoa.olhos), id(p.olhos), id(p2.olhos), id(p3.olhos))
    print()

    p3.olhos = 1
    print("Pessoa: ", Pessoa.olhos, Pessoa.__dict__)
    print("p: ", p.olhos, p.__dict__)
    print("p2: ", p2.olhos, p2.__dict__)
    print("p3: ", p3.olhos, p3.__dict__)
    print(id(Pessoa.olhos), id(p.olhos), id(p2.olhos), id(p3.olhos))
    print()

    Pessoa.olhos = 3
    p3.olhos = 1
    print("Pessoa: ", Pessoa.olhos, Pessoa.__dict__)
    print("p: ", p.olhos, p.__dict__)
    print("p2: ", p2.olhos, p2.__dict__)
    print("p3: ", p3.olhos, p3.__dict__)
    print(id(Pessoa.olhos), id(p.olhos), id(p2.olhos), id(p3.olhos))
    print()

    del p3.olhos
    print("Pessoa: ", Pessoa.olhos, Pessoa.__dict__)
    print("p: ", p.olhos, p.__dict__)
    print("p2: ", p2.olhos, p2.__dict__)
    print("p3: ", p3.olhos, p3.__dict__)
    print(id(Pessoa.olhos), id(p.olhos), id(p2.olhos), id(p3.olhos))
    print()

