'''
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''

class Bola(): 
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_de_cor(self, cor):
            self.cor = cor
            print("A cor foi trocada para: " , self.cor)

    def mostrar_cor(self):
           print("A cor da bola é: " , self.cor) 


bola_futebol = Bola ("Branca e Preta", 68, "Couro sintético")
print(bola_futebol.cor)

bola_futebol.troca_de_cor("Azul e preta")
print(bola_futebol.cor)

