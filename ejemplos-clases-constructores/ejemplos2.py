class BancoCuenta:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo += cantidad
        return f"Depósito de {cantidad} realizado. Saldo actual: {self.saldo}"

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return f"Retiro de {cantidad} realizado. Saldo actual: {self.saldo}"
        else:
            return "Fondos insuficientes para realizar el retiro."

    def obtener_saldo(self):
        return f"Saldo actual de la cuenta de {self.titular}: {self.saldo}"

cuenta2 = BancoCuenta("María García", 2000)

print(cuenta2.obtener_saldo())

print(cuenta2.depositar(1000))

print(cuenta2.retirar(500))

print(cuenta2.retirar(3000))
