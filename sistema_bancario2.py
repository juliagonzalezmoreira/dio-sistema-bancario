import textwrap


def menu():
    menu = '''Escolha uma opcao:

                [d] Depositar
                [s] Saque
                [e] Extrato
                [n] Nova Conta
                [u] Novo Usuário
                [l] Listar Contas
                [q] Sair
                '''
    return input(textwrap.dedent(menu))

def deposito(saldo, valor, extrato, /):
    if valor != 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}"
        print('Depósito realizado!')

    else:
        print('Operação falhou!')

    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saque, limite_saque):
    excedeu_limite = valor > limite
    excedeu_saldo = valor > saldo
    excedeu_diario = numero_saque >= limite_saque
    
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
        print('Saque sucedido!')

    else:
        print('Operação falhou! Tente novamente...')

    return saldo, extrato

def extrato(saldo, /, *, extrato):
    print('EXTRATO')
    print('Não há movimentações') if not extrato else extrato
    print(f'Saldo: {saldo:.2f}')

    return saldo, extrato

def criar_usuarios(usuarios):
    cpf = int(input('Informa seu CPF (apenas números):'))
    nome = str(input('Informe seu nome:'))
    data_nascimento = input('Informe sua data de nascimento (dd/mm/aaaa):')
    endereco = input('Informe o seu endereço (logradouro, n° - bairro - cidade/sigla):')

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Usuário já cadastrado.')
        return

    else: 
        usuarios.append({nome: 'nome', data_nascimento: 'data_nascimento', endereco: 'endereco', cpf: 'cpf'})
        print('Usuário cadastrado!')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuarios}

    print("Usuário não encontrado.")
    return

def listar_conta(contas):
     for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuarios(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_conta(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, tente novamente...")

