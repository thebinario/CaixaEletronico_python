class CC():
    def __init__(self):
        self.saldo = 100

    def sacar(self):
        valor = float(input("Valor a sacar: "))
        if self.saldo < valor:
            print("saldo insuficiente")
        else:
            self.saldo -= valor
            print("Saque realizado")
            return self.saldo

    def Consulta(self):
        return print(f"Saldo total {self.saldo}")

    def deposita(self):
        dinheiro = float(input("Valor a Depositar: "))
        self.saldo += dinheiro

    def __str__(self):
        return "\nSaldo: {} \n".format(float(self.saldo))
def main():
    contaCC = CC()

    while True:
        print(contaCC)
        print("Menu de Opções:")
        print("1 - Saldo")
        print("2 - Sacar")
        print("3 - Depositar\n")
        menu = input("Selecionar:")

        if menu == "1":
            contaCC.Consulta()
        elif menu == "2":
            contaCC.sacar()
        elif menu == "3":
            contaCC.deposita()
        else:
            print("Selecione uma opção válida!")


if __name__ == "__main__":
    main()