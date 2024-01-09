'''
:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade 
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação
 entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para 
 armazenar esta informação por que ela pode ser calculada a qualquer momento.

Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida 
ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem quão rapidamente 
os níveis de fome e tédio caem.

Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do 
objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do 
usuário. Dica: acrescente um método especial str() à classe Bichinho.

Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. 
Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho, exija 
que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário executasse uma ação para todos 
os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar 
o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.

'''

class Tamaguchi():
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def __str__ (self):

        return f"nome: {self.nome}, idade: {self.idade} anos, fome: {self.fome}, saúde: {self.saude}"

    def alterar_nome (self, nome):
        self.nome = nome
        print("O nome foi alterado para:" , self.nome)

    def alterar_saude(self, nova_saude):
        self.saude = nova_saude
        print(f"A saúde do {self.nome} foi alterada para: {self.saude}")
        self.calculo_humor()

    def alterar_fome(self, nova_fome):
        self.fome = nova_fome
        print(f"A fome do {self.nome} foi alterada para: {self.fome}")
        self.calculo_humor()

    def dar_comida(self, comida):
        self.alterar_fome(comida + self.fome)

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade
        print(f"A nova idade do {self.nome} é: {self.idade}")

    def calculo_humor(self):
        print(f"O humor do {self.nome} é:" , self.fome + self.saude)
    
    def brincar(self, tempo):
        self.fome -= tempo * 2 
        print(f"Você brincou com o {self.nome}, ele ficou mais feliz porém com mais fome. Fome: {self.fome}")
        self.calculo_humor()

    def luta(self, dano):
        self.saude -= dano
        print(f"O {self.nome} se envolveu em uma briga, sua saúde depois da briga é: {self.saude}")

zoro = Tamaguchi("Zoro", 100, 500, 3)    
luffy = Tamaguchi("Luffy", 0, 100, 5 )
sanji = Tamaguchi("Sanji", 1000, 100, 2)

fazenda = [zoro, luffy, sanji]

for mugiwara in fazenda:
    print("-------------------------------------------------------")
    print(mugiwara)
    mugiwara.dar_comida(40)
    mugiwara.brincar(10)
    mugiwara.luta(30)   