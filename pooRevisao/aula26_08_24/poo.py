from Objetos import Bola, Quadrado,Retangulo


print('###BOLA###')
bola1 = Bola("Verde",10,"couro")
print(bola1.mostraCor())
bola1.trocaCor("Preto")
print(bola1.mostraCor())

print('###QUADRADO###')
q1 = Quadrado(10)
print(q1.calcular_area())
q1.set_lado(20)
print(q1.calcular_area())

print('###RETANGULO###')
r1 = Retangulo(10,5)
print(r1.calcular_area())
r1.set_lado1(20)
r1.set_lado2(10)
print(r1.calcular_area())





