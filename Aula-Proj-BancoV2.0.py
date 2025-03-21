from datetime import datetime, date, timedelta

menu = """
SEJA BEM VINDO AO BANCO

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

ESCOLHA UMA OPÇÃO
"""


class ContaBancaria:
    transacoes_por_dia = 10

    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0
        self.extrato = []
        self.data_transacoes = date.today()
        self.transacoes_dia = 0

    def resetar_transacoes_diarias(self):
        if self.data_transacoes != date.today():
            self.data_transacoes = date.today()
            self.transacoes_dia = 0

    def depositar(self, valor):
        self.resetar_transacoes_diarias()
        if self.transacoes_dia >= ContaBancaria.transacoes_por_dia:
            print("Número máximo de transações diárias atingido. Tente novamente amanhã.")
            return

        if valor > 0:
            self.saldo += valor
            self.transacoes_dia += 1
            self.extrato.append(
                f"Depósito {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} + "
                f"R$ {valor:.2f}\nSaldo: R$ {self.saldo:.2f}"
            )
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso! Saldo atual: R$ {self.saldo:.2f}")
        else:
            print("Valor inválido para depósito!")

    def sacar(self, valor, limite=500.0):
        self.resetar_transacoes_diarias()
        if self.transacoes_dia >= ContaBancaria.transacoes_por_dia:
            print("Número máximo de transações diárias atingido. Tente novamente amanhã.")
            return

        if valor <= 0:
            print("Valor inválido para saque!")
            return
        if valor > limite:
            print(f"Valor excede o limite de saque de R$ {limite:.2f} por operação.")
            return
        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
            return

        self.saldo -= valor
        self.transacoes_dia += 1
        self.extrato.append(
            f"Saque {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - "
            f"R$ {valor:.2f}\nSaldo: R$ {self.saldo:.2f}"
        )
        print(f"Saque de R$ {valor:.2f} realizado com sucesso! Saldo atual: R$ {self.saldo:.2f}")

    def mostrar_extrato(self):
        print(f"\n{'EXTRATO BANCÁRIO'.center(50, '=')}")
        if not self.extrato:
            print("Nenhuma transação realizada.")
        else:
            for transacao in self.extrato:
                print(transacao)
        print("=".center(50, "="))
        print(f"Saldo atual: R$ {self.saldo:.2f}\n")


def criar_conta():
    titular = input("Digite o nome do titular da conta: ")
    return ContaBancaria(titular)


def menu_banco():
    print("Seja bem-vindo ao Banco Digital!")
    conta = criar_conta()

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Digite o valor a depositar: R$ "))
            conta.depositar(valor)
        elif opcao == "s":
            valor = float(input("Digite o valor a sacar: R$ "))
            conta.sacar(valor)
        elif opcao == "e":
            conta.mostrar_extrato()
        elif opcao == "q":
            print("Obrigado por usar o Banco Digital! Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_banco()
