class Pessoa:
    
    pessoas = 3

    def __init__(self,nome,genero,data_de_nascimento,pais,altura,peso):

        self.nome = nome
        self.genero = genero
        self.data_de_nascimento = data_de_nascimento
        self.pais = pais
        self.altura = altura
        self.peso = peso

        

    def info_pessoa(self):

        print("Nome : " + self.nome)
        print("Genero : " + self.genero)
        print("Nascimento : " + str(self.data_de_nascimento))
        print("Pais : " + self.pais)
        print("Altura : " + str(self.altura))
        print("Peso : " + str(self.peso))

Ana = Pessoa("Ana","F","15/09/2005","Brasil","1.67","56 Kg")

Ana.info_pessoa()
