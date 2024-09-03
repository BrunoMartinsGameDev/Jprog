class Pessoa():
    def __init__(self,nome,idade,altura) -> None:
        self._nome = nome
        self._idade = idade
        self._altura = altura

    @property
    def nome(self):
        print("Estou dentro da propriedade")
        return self._nome
    @nome.setter
    def nome(self,novoNome):
        print("Estou dentro do setter")
        self._nome = novoNome
    
    @property
    def idade(self):
        print("Estou dentro da propriedade")
        return self._idade
    @idade.setter
    def idade(self,novaIdade):
        print("Estou dentro do setter")
        self._idade = novaIdade

    @property
    def altura(self):
        print("Estou dentro da propriedade")
        return self._altura
    @altura.setter
    def altura(self,novaAltura):
        print("Estou dentro do setter")
        self._altura = novaAltura
    
    def getNome(self):
        return self.nome
    def setNome(self,novoNome):
        self.nome = novoNome

    def getIdade(self):
        return self.idade
    def setIdade(self,novaIdade):
        self.idade = novaIdade

    def getAltura(self):
        return self.altura
    def setAltura(self,novaAltura):
        self.altura = novaAltura

class Conta():
    def __init__(self, saldo, limite) -> None:
        self._saldo = saldo
        self._limite = limite

    @property
    def saldo(self):
        print("Estou dentro da propriedade")
        return self._saldo
    @saldo.setter
    def saldo(self,novoSaldo):
        print("Estou dentro do setter")
        self._saldo = novoSaldo

    @property
    def limite(self):
        print("Estou dentro da propriedade")
        return self._limite
    @limite.setter
    def limite(self,novoLimite):
        print("Estou dentro do setter")
        self._limite = novoLimite

    def getSaldo(self):
        return self.saldo
    def setSaldo(self,novoSaldo):
        self.saldo = novoSaldo

    def getLimite(self):
        return self.limite
    def setLimite(self,novoLimite):
        self.limite = novoLimite
    
    def sacar(self,valor):
        if valor > self.saldo+self.limite:
            return "Saldo insuficiente"
        self.setSaldo(self.getSaldo()-valor)
        return f"Saque efetuado, saldo atual: {self.getSaldo()}"