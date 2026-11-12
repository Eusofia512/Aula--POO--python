class Conta:
    #Atributos
    def __init__(self, titular, saldo,):
        self.titular = titular
        self.saldo = saldo
    #Métodos
    def depositar(self, valor):
        self.saldo += valor
        print("Depósito realizado!")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado!")
        else:
            print("Saldo inuficiente!")
    def consultar_saldo(self):
        print("Saldo: ", self.saldo)
    def pagamento(self, pag):
        if pag <= self.saldo: 
            self.saldo -= pag
            print("Pagamento realizado!")
            print("Saldo: ", self.saldo )
        else:
            print("Saldo inuficiente!")
pag = float(input("Digite o valor a ser pago: "))

#Objetos
conta1 = Conta("Sávio", 500)
conta2 = Conta("Tainá", 800)
conta3 = Conta("Micaele", 800)
conta4 = Conta("Sofia", 500)
conta5 = Conta("Icaro", 700)

#Chamar os métodos
print("")
conta1.consultar_saldo()
conta1.depositar(200)
conta1.sacar(100)
conta1.consultar_saldo()
conta1.pagamento(pag)
print("")

conta2.consultar_saldo()
conta2.depositar(200)
conta2.sacar(100)
conta2.consultar_saldo()
conta1.pagamento(pag)
print("")

conta3.consultar_saldo()
conta3.depositar(200)
conta3.sacar(100)
conta3.consultar_saldo()
conta1.pagamento(pag)
print("")

conta4.consultar_saldo()
conta4.depositar(200)
conta4.sacar(100)
conta4.consultar_saldo()
conta1.pagamento(pag)
print("")

conta5.consultar_saldo()
conta5.depositar(200)
conta5.sacar(100)
conta5.consultar_saldo()
conta1.pagamento(pag)
print("")