class Bola():
    def __init__(self, cor, circunferencia, material) -> None:
        self.cor = cor
        self.circuferencia = circunferencia
        self.material = material

    def trocaCor(self, novaCor):

        self.cor = novaCor

    def mostraCor(self):
        return self.cor
    
class Quadrado():
    def __init__(self,lado) -> None:
        self.lado = lado
    
    def set_lado(self,novoLado):
        self.lado = novoLado
    
    def get_lado(self):
        return self.lado
    
    def calcular_area(self):
        return self.lado*self.lado

class Retangulo():
    def __init__(self,lado1,lado2) -> None:
        self.lado1 = lado1
        self.lado2 = lado2
    
    def set_lado1(self,novoLado):
        self.lado1 = novoLado
    
    def get_lado1(self):
        return self.lado1
    
    def set_lado2(self,novoLado):
        self.lado2 = novoLado
    
    def get_lado2(self):
        return self.lado2
    
    def calcular_area(self):
        return self.lado1*self.lado2