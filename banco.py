import datetime

# Dados da conta
saldo = 0.0
limite = 500.0
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

# Menu principal
menu = """
====================================
        🏦 SISTEMA BANCÁRIO
====================================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
====================================
=> """

# Função para depósito
def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato.append(f"[{data_hora()}] Depósito: R$ {valor:.2f}")
            print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("❌ Operação falhou! Valor inválido.")
    except ValueError:
        print("❌ Entrada inválida! Informe um número válido.")
    return saldo, extrato

# Função para saque
def sacar(saldo, extrato, numero_saques):
    try:
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("❌ Operação falhou! Saldo insuficiente.")

        elif excedeu_limite:
            print(f"❌ Operação falhou! Limite por saque é de R$ {limite:.2f}.")

        elif excedeu_saques:
            print("❌ Operação falhou! Número máximo de saques diários excedido.")

        elif valor > 0:
            saldo -= valor
            extrato.append(f"[{data_hora()}] Saque: -R$ {valor:.2f}")
            numero_saques += 1
            print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("❌ Operação falhou! Valor inválido.")
    except ValueError:
        print("❌ Entrada inválida! Informe um número válido.")
    return saldo, extrato, numero_saques

# Função para exibir extrato
def exibir_extrato(saldo, extrato):
    print("\n========== 🧾 EXTRATO ==========")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==================================")

# Função para obter data e hora atual formatada
def data_hora():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Loop principal
while True:
    opcao = input(menu).lower()

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "q":
        print("\n✅ Obrigado por utilizar nosso sistema. Volte sempre!")
        break

    else:
        print("❌ Operação inválida! Selecione uma opção válida.")
