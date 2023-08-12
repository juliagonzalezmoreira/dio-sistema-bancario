menu = '''
Escolha uma opcao:

[D] Depositar
[S] Saque
[E] Extrato
[Q] Sair

'''

saldo = 0
extrato = ''
numero_saque = 0
limite_saque = 500
LIMITE_DIARIO = 3

while True:

    opcao = input(menu)

    if opcao == 'D':
        valor = float(input("Informe o valor do depósito: "))

        if valor != 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}"

        else:
            print('Operação falhou! Tente novamente...')
        
    elif opcao == 'S':
        valor = float(input("Informe o valor de saque: "))

        excedeu_limite = valor > limite_saque
        excedeu_saldo = valor > saldo
        excedeu_diario = numero_saque >= LIMITE_DIARIO

        if excedeu_limite:
            print('Valor acima do limite de saque.')
        elif excedeu_saldo:
            print('Valor acima do saldo.')
        elif excedeu_diario:
            print('Limite diário atingido.')

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}" 
            numero_saque += 1

        else:
            print('Operação falhou! Tente novamente...')
        
    elif opcao == 'E':
        print('EXTRATO')
        print('Não há movimentações') if not extrato else extrato
        print(f'Saldo: {saldo:.2f}')
    
    elif opcao == "Q":
        break

    else:
        print('Operação falhou! Tente novamente...')
