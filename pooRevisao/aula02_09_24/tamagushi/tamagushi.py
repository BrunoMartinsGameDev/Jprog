# class Tamagushi:
#     def __init__(self, nome, fome, saude, idade):
#         self.nome = nome
#         self.fome = fome
#         self.saude = saude
#         self.idade = idade
    
#     def set_nome(self, novo_nome):
#         self.nome = novo_nome
    
#     def set_fome(self, nova_fome):
#         self.fome = nova_fome
    
#     def set_saude(self, nova_saude):
#         self.saude = nova_saude
    
#     def set_idade(self, nova_idade):
#         self.idade = nova_idade
    
#     def get_nome(self):
#         return self.nome
    
#     def get_fome(self):
#         return self.fome
    
#     def get_saude(self):
#         return self.saude
    
#     def get_idade(self):
#         return self.idade
    
#     def calcular_humor(self):
#         """O humor é calculado com base na combinação de fome e saúde.
#         A fórmula para humor pode ser ajustada conforme necessário. Aqui,
#         consideramos uma fórmula simples onde:
#         - Se a fome é alta (maior que 7) ou a saúde é baixa (menor que 4), o humor é ruim.
#         - Caso contrário, o humor é bom.
#         """
#         if self.fome > 7 or self.saude < 4:
#             return "Ruim"
#         else:
#             return "Bom"
        
# if __name__ == '__main__':
#     # Exemplo de uso
#     tamagushi = Tamagushi(nome="Tama", fome=5, saude=8, idade=1)

#     print("Nome:", tamagushi.get_nome())
#     print("Fome:", tamagushi.get_fome())
#     print("Saúde:", tamagushi.get_saude())
#     print("Idade:", tamagushi.get_idade())
#     print("Humor:", tamagushi.calcular_humor())

#     # Alterando alguns atributos
#     tamagushi.set_fome(8)
#     tamagushi.set_saude(3)

#     print("\nApós alterações:")
#     print("Nome:", tamagushi.get_nome())
#     print("Fome:", tamagushi.get_fome())
#     print("Saúde:", tamagushi.get_saude())
#     print("Idade:", tamagushi.get_idade())
#     print("Humor:", tamagushi.calcular_humor())


import random
class Tamagushi:
    def __init__(self, nome, fome=None, saude=10, idade=1, tedio=None):
        self.nome = nome
        self.fome = fome if fome is not None else random.randint(0, 10)
        self.saude = saude
        self.idade = idade
        self.tedio = tedio if tedio is not None else random.randint(0, 10)
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    
    def set_fome(self, nova_fome):
        self.fome = nova_fome
    
    def set_saude(self, nova_saude):
        self.saude = nova_saude
    
    def set_idade(self, nova_idade):
        self.idade = nova_idade

    def fornecer_comida(self, quantidade):
        """Fornece comida ao Tamagushi. A fome diminui com base na quantidade fornecida."""
        self.fome = max(0, self.fome - quantidade)  # A fome não pode ser negativa
    
    def brincar(self, tempo):
        """Permite brincar com o Tamagushi. O tédio diminui com base no tempo de brincadeira."""
        self.tedio = max(0, self.tédio - tempo)  # O tédio não pode ser negativo
    
    def get_nome(self):
        return self.nome
    
    def get_fome(self):
        return self.fome
    
    def get_saude(self):
        return self.saude
    
    def get_idade(self):
        return self.idade
    
    def get_tédio(self):
        return self.tédio
    
    def calcular_humor(self):
        """Calcula o humor com base na fome e saúde, e também considera o tédio."""
        if self.fome > 7 or self.saude < 4 or self.tedio > 7:
            return "Ruim"
        else:
            return "Bom"
        
    def __str__(self):
        """Representação detalhada do objeto Tamagushi."""
        return (f"Nome: {self.nome}\n"
                f"Fome: {self.fome}\n"
                f"Saúde: {self.saude}\n"
                f"Idade: {self.idade}\n"
                f"Tédio: {self.tedio}\n"
                f"Humor: {self.calcular_humor()}")
class Fazenda:
    def __init__(self):
        self.bichinhos = []
    
    def adicionar_bichinho(self, bichinho):
        self.bichinhos.append(bichinho)
    
    def alimentar_todos(self, quantidade):
        for bichinho in self.bichinhos:
            bichinho.fornecer_comida(quantidade)
    
    def brincar_com_todos(self, tempo):
        for bichinho in self.bichinhos:
            bichinho.brincar(tempo)
    
    def mostrar_estado_de_todos(self):
        for bichinho in self.bichinhos:
            print("\nEstado do bichinho:")
            print(bichinho)
    
    def mostrar_menu(self):
        while True:
            print("\nMenu da Fazenda:")
            print("1. Alimentar todos os bichinhos")
            print("2. Brincar com todos os bichinhos")
            print("3. Mostrar estado de todos os bichinhos")
            print("4. Sair")
            
            escolha = input("Escolha uma opção: ")
            
            if escolha == "1":
                quantidade = int(input("Quantidade de comida: "))
                self.alimentar_todos(quantidade)
            elif escolha == "2":
                tempo = int(input("Tempo de brincadeira: "))
                self.brincar_com_todos(tempo)
            elif escolha == "3":
                self.mostrar_estado_de_todos()
            elif escolha == "4":
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente.")
                     
if __name__ == '__main__':
    # Exemplo de uso
    tamagushi = Tamagushi(nome="Tama", fome=5, saude=8, idade=1)

    print("Nome:", tamagushi.get_nome())
    print("Fome:", tamagushi.get_fome())
    print("Saúde:", tamagushi.get_saude())
    print("Idade:", tamagushi.get_idade())
    print("Tédio:", tamagushi.get_tédio())
    print("Humor:", tamagushi.calcular_humor())

    # Fornecendo comida e brincando com o bichinho
    tamagushi.fornecer_comida(3)
    tamagushi.brincar(5)

    print("\nApós fornecer comida e brincar:")
    print("Nome:", tamagushi.get_nome())
    print("Fome:", tamagushi.get_fome())
    print("Saúde:", tamagushi.get_saude())
    print("Idade:", tamagushi.get_idade())
    print("Tédio:", tamagushi.get_tédio())
    print("Humor:", tamagushi.calcular_humor())
