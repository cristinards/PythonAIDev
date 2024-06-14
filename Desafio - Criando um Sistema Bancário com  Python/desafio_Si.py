# Desafio: Criando um Sistema Bancário com Python

print("=======================================================")
print("Bem-vindo ao Sistema Bancario! Por favor, selecione uma opcao e pressione ENTER:")
print("=======================================================")

# Menu
menu = '''
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
'''
# Parâmetros
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Ações a serem feitas caso o usuário selecionar determinada opção do menu
while True:

    opcao = input(menu)

    if opcao == "d":
        print("\n================ DEPOSITO ================")
        valor = float(input("Informe o valor do depósito: "))
        print("============================================")

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("=======================================================")
            print("Operação falhou! O valor informado é inválido.")
            print("=======================================================")

    elif opcao == "s":
        print("\n=============== SAQUE =================")
        valor = float(input("Informe o valor do saque: "))
        print("=========================================")

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("=======================================================")
            print("Operação falhou! Você não tem saldo suficiente.")
            print("=======================================================")

        elif excedeu_limite:
            print("=======================================================")
            print("Operação falhou! O valor do saque excede o limite.")
            print("=======================================================")

        elif excedeu_saques:
            print("=======================================================")
            print("Operação falhou! Número máximo de saques excedido.")
            print("=======================================================")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")