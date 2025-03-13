menu = """
SEJA BEM VINDO AO BANCO

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

ESCOLHA UMA OPÇÃO
"""
saldo = 0
limite = 500
extrato = ""
n_saques = 0
l_saques = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor_d = float(input("Digite o valor a ser depositado: R$"))
        if valor_d > 0:
            saldo += valor_d
            extrato += f"Depósito: R${valor_d:.2f}\nSaldo: R${saldo:.2f}\n"
        else:
            print("O valor precisa ser maior que 0, Recomeçando...")
    elif opcao == "s":
        if n_saques < l_saques:
            valor_s = float(input("Digite o valor a ser sacado: R$"))
            if valor_s <= limite:
                if 0 < valor_s <= saldo:
                    n_saques += 1
                    saldo -= valor_s
                    extrato += f"Saque: R${valor_s:.2f}\nSaldo: R${saldo:.2f}\n"
                elif valor_s > saldo:
                    print("O Valor precisa ser maior que 0 e menor que o saldo, Recomeçando...")
            else:
                print("Este valor excede o limite de valor por saque (R$500.00)")
        else:
            print("!!!Número de saques diários atingidos!!!")
    elif opcao == "e":
        print(f"{"EXTRATO".center(30, ".")}\n{extrato}")
    elif opcao == "q":
        print("Até a próxima!")
        break
    else:
        print("Opção inválida, tente novamente com uma opção válida")


