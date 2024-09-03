class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        # Adiciona o alimento ao bucho (estômago)
        self.bucho.append(alimento)

    def ver_bucho(self):
        # Mostra o conteúdo do bucho
        if not self.bucho:
            print(f"O bucho do macaco {self.nome} está vazio.")
        else:
            print(f"O bucho do macaco {self.nome} contém: ")
            for i in self.bucho:
                print(i)

    def digerir(self):
        # Remove o primeiro alimento que foi ingerido
        if self.bucho:
            alimento_digerido = self.bucho.pop(0)
            print(f"O macaco {self.nome} digeriu: {alimento_digerido}.")
        else:
            print(f"Não há nada no bucho do macaco {self.nome} para digerir.")
    def __str__(self) -> str:
        return self.nome

# Testando a classe Macaco
macaco1 = Macaco("Macaco 1")
macaco2 = Macaco("Macaco 2")

# Alimentando os macacos com diferentes alimentos
macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco1.comer("Pera")
macaco1.ver_bucho()

macaco2.comer("Manga")
macaco2.comer("Abacaxi")
macaco2.comer("Laranja")
macaco2.ver_bucho()

# Fazendo o macaco 1 comer o macaco 2 (macaco canibal)
macaco1.comer(macaco2)
macaco1.ver_bucho()

# Digestionando alimentos
macaco1.digerir()
macaco1.ver_bucho()
