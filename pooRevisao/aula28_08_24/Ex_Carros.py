class Motor:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []

    def adicionar_carro(self, carro):
        if carro not in self.carros:
            self.carros.append(carro)

    def __str__(self):
        return self.nome

class Carro:
    def __init__(self, nome, motor):
        self.nome = nome
        self.motor = motor
        self.motor.adicionar_carro(self)

    def exibir_informacoes(self):
        print(f"Carro: {self.nome}")
        print(f"Motor: {self.motor}")

class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []

    def criar_carro(self, nome, motor):
        carro = Carro(nome, motor)
        self.carros.append(carro)
        return carro

    def exibir_carros(self):
        print(f"Carros fabricados por {self.nome}:")
        for carro in self.carros:
            print(f"- {carro.nome}")

# Exemplo de uso:
if __name__ == "__main__":
    # Criando motores
    motor1 = Motor("Motor V8")
    motor2 = Motor("Motor Turbo")

    # Criando fabricantes
    fabricante1 = Fabricante("Fabricante A")
    fabricante2 = Fabricante("Fabricante B")

    # Fabricantes criando carros
    fabricante1.criar_carro("Carro 1", motor1)
    fabricante1.criar_carro("Carro 2", motor2)
    fabricante2.criar_carro("Carro 3", motor1)

    # Exibindo informações dos carros
    print("Informações dos carros:")
    for carro in fabricante1.carros:
        carro.exibir_informacoes()
        print()
    for carro in fabricante2.carros:
        carro.exibir_informacoes()
        print()

    # Exibindo todos os carros associados a um motor
    print("\nCarros com Motor V8:")
    for carro in motor1.carros:
        print(f"- {carro.nome}")

    print("\nCarros com Motor Turbo:")
    for carro in motor2.carros:
        print(f"- {carro.nome}")

    # Exibindo todos os carros fabricados por um fabricante
    fabricante1.exibir_carros()

    fabricante2.exibir_carros()
