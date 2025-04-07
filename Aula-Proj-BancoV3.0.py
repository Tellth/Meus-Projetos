from datetime import datetime, date
import textwrap

# ================= CLASSES ====================

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class ContaBancaria:
    AGENCIA_PADRAO = "0001"
    LIMITE_SAQUE = 500.0
    MAX_SAQUES_DIARIOS = 3
    MAX_TRANSACOES_DIA = 10

    def __init__(self, numero, usuario: Usuario):
        self.agencia = ContaBancaria.AGENCIA_PADRAO
        self.numero = numero
        self.usuario = usuario
        self.saldo = 0.0
        self.extrato = []
        self.transacoes_dia = 0
        self.saques_hoje = 0
        self.data_transacoes = date.today()

    def resetar_limites_diarios(self):
        if self.data_transacoes != date.today():
            self.data_transacoes = date.today()
            self.transacoes_dia = 0
            self.saques_hoje = 0

    def depositar(self, valor):
        self.resetar_limites_diarios()
        if self.transacoes_dia >= ContaBancaria.MAX_TRANSACOES_DIA:
            print("Limite de transações diárias atingido.")
            return

        if valor > 0:
            self.saldo += valor
            self.transacoes_dia += 1
            self.extrato.append(f"{datetime.now()} | Depósito: +R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        self.resetar_limites_diarios()
        if self.transacoes_dia >= ContaBancaria.MAX_TRANSACOES_DIA:
            print("Limite de transações diárias atingido.")
            return
        if self.saques_hoje >= ContaBancaria.MAX_SAQUES_DIARIOS:
            print("Limite de saques diários atingido.")
            return
        if valor <= 0:
            print("Valor inválido.")
            return
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return
        if valor > ContaBancaria.LIMITE_SAQUE:
            print(f"Valor excede o limite de R$ {ContaBancaria.LIMITE_SAQUE:.2f}")
            return

        self.saldo -= valor
        self.transacoes_dia += 1
        self.saques_hoje += 1
        self.extrato.append(f"{datetime.now()} | Saque: -R$ {valor:.2f}")
        print("Saque realizado com sucesso!")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        if not self.extrato:
            print("Nenhuma movimentação.")
        else:
            for linha in self.extrato:
                print(linha)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        print("=========================================")

# ================= FUNÇÕES ====================

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo usuário
    [nc]\tNova conta
    [lc]\tListar contas
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if filtrar_usuario(cpf, usuarios):
        print("Usuário já cadastrado.")
        return
    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, número - bairro - cidade/UF): ")
    usuarios.append(Usuario(nome, nascimento, cpf, endereco))
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario
    return None

def criar_conta(contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if not usuario:
        print("Usuário não encontrado.")
        return
    numero = len(contas) + 1
    conta = ContaBancaria(numero, usuario)
    contas.append(conta)
    print("Conta criada com sucesso!")

def listar_contas(contas):
    for conta in contas:
        print("=" * 50)
        print(f"Agência: {conta.agencia}")
        print(f"Conta Nº: {conta.numero}")
        print(f"Titular: {conta.usuario.nome}")

def encontrar_conta_por_usuario(cpf, contas):
    return [conta for conta in contas if conta.usuario.cpf == cpf]

# ================= PROGRAMA PRINCIPAL ====================

def main():
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            criar_conta(contas, usuarios)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao in ("d", "s", "e"):
            cpf = input("Informe o CPF do titular: ")
            contas_usuario = encontrar_conta_por_usuario(cpf, contas)
            if not contas_usuario:
                print("Nenhuma conta encontrada para este CPF.")
                continue
            if len(contas_usuario) > 1:
                print("Mais de uma conta encontrada. Use a conta mais recente.")
            conta = contas_usuario[-1]

            if opcao == "d":
                try:
                    valor = float(input("Valor do depósito: R$ "))
                    conta.depositar(valor)
                except ValueError:
                    print("Valor inválido.")
            elif opcao == "s":
                try:
                    valor = float(input("Valor do saque: R$ "))
                    conta.sacar(valor)
                except ValueError:
                    print("Valor inválido.")
            elif opcao == "e":
                conta.exibir_extrato()

        elif opcao == "q":
            print("Obrigado por usar o Banco Digital!")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
