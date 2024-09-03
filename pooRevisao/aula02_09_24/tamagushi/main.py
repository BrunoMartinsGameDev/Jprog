from tamagushi import Fazenda
from tamagushi import Tamagushi
# def menu():
#     tamagushi = Tamagushi(nome="Tama", fome=5, saude=8, idade=1)
    
#     while True:
#         print("\nMenu:")
#         print("1. Fornecer comida")
#         print("2. Brincar")
#         print("3. Mostrar estado atual")
#         print("4. Sair")
        
#         escolha = input("Escolha uma opção: ")
        
#         if escolha == "1":
#             quantidade = int(input("Quantidade de comida: "))
#             tamagushi.fornecer_comida(quantidade)
#         elif escolha == "2":
#             tempo = int(input("Tempo de brincadeira: "))
#             tamagushi.brincar(tempo)
#         elif escolha == "3":
#             print("\nEstado atual do Tamagushi:")
#             print(f"Nome: {tamagushi.get_nome()}")
#             print(f"Fome: {tamagushi.get_fome()}")
#             print(f"Saúde: {tamagushi.get_saude()}")
#             print(f"Idade: {tamagushi.get_idade()}")
#             print(f"Tédio: {tamagushi.get_tédio()}")
#             print(f"Humor: {tamagushi.calcular_humor()}")
#         elif escolha == "0":
#             # Mostrar atributos detalhados
#             print("\nAtributos detalhados do Tamagushi:")
#             print(tamagushi)
#         elif escolha == "4":
#             print("Saindo...")
#             break
#         else:
#             print("Opção inválida, tente novamente.")

# menu()


fazenda = Fazenda()

# Adicionando bichinhos à fazenda
nomes = ["Tama", "Rex", "Luna", "Milo", "Zara"]
for nome in nomes:
    bichinho = Tamagushi(nome)
    fazenda.adicionar_bichinho(bichinho)

# Iniciando o menu
fazenda.mostrar_menu()