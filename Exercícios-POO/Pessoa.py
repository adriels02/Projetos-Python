'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhecer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''
class Pessoa(): 
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer (self):
        self.idade += 1
        if (self.idade < 21):
            self.altura += 0.05
        print(self.nome, " envelheceu 1 ano. Ficando com a idade de: " , self.idade, " e altura de: " , self.altura)



    def emagrecer (self, peso_perdido):
        self.peso -= peso_perdido
        print(self.nome, " Perdeu peso. Ficando com " , self.peso)
    
    def engordar (self, peso_ganho):
        self.peso += peso_ganho
        print(self.nome, " Ganhou peso. Ficando com " , self.peso)
    

pessoa_1 = Pessoa("Roberto", 18, 65, 1.68)
pessoa_1.envelhecer()
pessoa_1.engordar(5)
pessoa_1.emagrecer(2)