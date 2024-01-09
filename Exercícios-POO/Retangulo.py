'''
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

'''
class Retangulo ():
    def __init__ (self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudar_comprimento (self, novo_comprimento):
        self.comprimento = novo_comprimento
        print("O comprimento foi alterado para: " , self.comprimento)

    def mudar_largura(self, nova_largura):
        self.largura = nova_largura
        print("A largura foi alterada para: " , self.largura)

    def mostrar_comprimento(self):
        print("O comprimento é: " , self.comprimento)

    def mostrar_largura(self):
        print("A largura é: " , self.largura)
        
    def calcular_area(self):
        print("A área é: " , self.comprimento * self.largura)
    
    def calcular_perimetro(self):
        print("O perímetro é: " , 2 *(self.comprimento + self.largura))



comprimento = float(input("Digite o comprimento: "))
largura = float(input("Digite a largura: "))    

retangulo_1 = Retangulo(comprimento, largura)
retangulo_1.mostrar_comprimento()
retangulo_1.mostrar_largura()
retangulo_1.calcular_area()
retangulo_1.calcular_perimetro()
