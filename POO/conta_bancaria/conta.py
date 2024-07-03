class Conta:
    def __init__(self, nome, saldo, cpf, senha):
        self.nome = nome
        self.__saldo = saldo
        self.__cpf = cpf
        self.__senha = senha

    def getSaldo(self):
        return self.__saldo

    def getCPF(self):
        return self.__cpf

    def getSenha(self):
        return self.__senha

    def extrato(self, senha):
        if senha != self.__senha:
            print("Senha inválida!")
            return
        return self.__saldo

    def depositar(self, valor):
        self.__saldo += valor
        return self.__saldo
    
    def sacar(self, senha, valor):
        if senha != self.__senha:
            print("Senha inválida!")
            return
        elif valor > self.__saldo:
            print("Saldo insuficiente!")
            return -1
        self.__saldo -= valor
        return valor

        
    
