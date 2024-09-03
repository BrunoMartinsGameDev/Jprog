from abc import ABC, abstractmethod

# Classe abstrata Pessoa
class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

# Classe Cliente que herda de Pessoa
class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self._conta = conta

    @property
    def conta(self):
        return self._conta

# Classe abstrata Conta
class Conta(ABC):
    def __init__(self, agencia, numero, saldo=0):
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self._saldo:.2f}")
        else:
            print("Depósito inválido!")

    @abstractmethod
    def sacar(self, valor):
        pass

# Conta Corrente que herda de Conta
class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo=0, limite=500):
        super().__init__(agencia, numero, saldo)
        self._limite = limite

    def sacar(self, valor):
        if 0 < valor <= (self._saldo + self._limite):
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self._saldo:.2f}")
        else:
            print("Saque excede o limite disponível!")

# Conta Poupança que herda de Conta
class ContaPoupanca(Conta):
    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self._saldo:.2f}")
        else:
            print("Saldo insuficiente!")

# Classe Banco que agrega Clientes e Contas
class Banco:
    def __init__(self):
        self._clientes = []
        self._contas = []

    def adicionar_cliente(self, cliente):
        self._clientes.append(cliente)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def autenticar(self, cliente, conta):
        if cliente not in self._clientes:
            print("Cliente não encontrado no banco.")
            return False
        if conta not in self._contas:
            print("Conta não encontrada no banco.")
            return False
        if conta.agencia != cliente.conta.agencia:
            print("A agência da conta não pertence a este banco.")
            return False
        print("Autenticação realizada com sucesso!")
        return True

# Testando o sistema bancário
# Criando o banco
banco = Banco()

# Criando contas
conta_corrente = ContaCorrente(agencia=123, numero=456, saldo=1000, limite=500)
conta_poupanca = ContaPoupanca(agencia=123, numero=789, saldo=2000)

# Criando clientes
cliente1 = Cliente(nome="Alice", idade=30, conta=conta_corrente)
cliente2 = Cliente(nome="Bob", idade=25, conta=conta_poupanca)

# Adicionando clientes e contas ao banco
banco.adicionar_cliente(cliente1)
banco.adicionar_cliente(cliente2)
banco.adicionar_conta(conta_corrente)
banco.adicionar_conta(conta_poupanca)

# Tentando sacar dinheiro (com autenticação)
if banco.autenticar(cliente1, conta_corrente):
    conta_corrente.sacar(1200)

if banco.autenticar(cliente2, conta_poupanca):
    conta_poupanca.sacar(2500)

# Depósitos
conta_corrente.depositar(300)
conta_poupanca.depositar(500)

# Verificando o saldo após operações
print(f"Saldo final da Conta Corrente: R${conta_corrente.saldo:.2f}")
print(f"Saldo final da Conta Poupança: R${conta_poupanca.saldo:.2f}")
