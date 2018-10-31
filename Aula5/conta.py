#Atributos = Titular, numero da conta e saldo
#metodos = depositar, sacar e transferir''''''

class Conta ():
    def __init__(self, titular, num, saldo=0):
        self.titular = titular
        self.numero = num
        self.saldo = saldo
        self.taxa = 0.5  
  
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        if self.saldo >= valor:
           self.saldo -= (valor + self.taxa)
           return 'Saque realizado com sucesso!'
        else:
           raise ValueError ("Saldo insuficiente: {}".format(
            self.saldo
        ))
    
    def transferir(self, valor, conta):
        try:
           self.sacar(valor)
           conta.depositar(valor)          
        except Exception:
            return ' Conta destino invalida'

    def __str__(self):
        return "conta: {} Titutal {}".format(
            self.numero, self.titular
        )

class Poupanca(Conta):
    def __init__(self, titula, num, saldo):
        super().__init__(titular, num, saldo)
        self.taxa = 0
    def render_juros(self):
        self.saldo += self.saldo * 0.0005
