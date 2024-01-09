'''
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''
class Quadrado():
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado
        
    def mudar_valor_lado(self, novo_tamanho):
        self.tamanho_lado = novo_tamanho
        print("O tamanho foi alterado para: " , novo_tamanho)
    
    def exibir_tamanho(self):
        print("O tamanho do lado é: ", self.tamanho_lado)

    def calcular_area(self):
        print("A área é: " , self.tamanho_lado * self.tamanho_lado)
       
    
quadrado_1 = Quadrado(20)
quadrado_1.calcular_area()