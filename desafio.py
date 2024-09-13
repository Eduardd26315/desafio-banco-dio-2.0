# Menu principal
menu = """
[a] Depositar
[b] Sacar
[c] Extrato
[d] Criar Usuário
[e] Listar Usuários
[f] Criar Conta Corrente
[g] Listar Contas Correntes
[h] Sair
=> """



# Função para realizar depósitos (somente argumentos posicionais)
def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito realizado: R$ {valor:.2f}\n"
        print("Depósito efetuado com sucesso!")
    else:
        print("Erro! Valor inválido para depósito.")
    return saldo, extrato

# Função para realizar saques (somente argumentos nomeados)
def sacar(*, valor, saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Erro! Saldo insuficiente para saque.")
    elif excedeu_limite:
        print("Erro! O valor do saque excede o limite permitido.")
    elif excedeu_saques:
        print("Erro! Número máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque realizado: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque efetuado com sucesso!")
    else:
        print("Erro! Valor inválido para saque.")
    return saldo, extrato, numero_saques

# Função para exibir o extrato (saldo por posição e extrato por nome)
def exibir_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Nenhuma transação realizada." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")

# Função para criar um novo usuário
def criar_usuario(nome, data_nascimento, cpf, endereco):
    # Remover qualquer caractere que não seja número do CPF
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verificar se o CPF já foi cadastrado
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Erro! Já existe um usuário com esse CPF.")
            return

    # Formatar os dados do novo usuário em um dicionário
    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    # Adicionar o novo usuário à lista de usuários
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")

# Função para exibir todos os usuários cadastrados (para verificação)
def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for i, usuario in enumerate(usuarios, 1):
            print(f"\nUsuário {i}:")
            print(f"Nome: {usuario['nome']}")
            print(f"Data de Nascimento: {usuario['data_nascimento']}")
            print(f"CPF: {usuario['cpf']}")
            print(f"Endereço: {usuario['endereco']}")
        print("\nTotal de usuários cadastrados:", len(usuarios))

# Função para criar uma nova conta corrente
def criar_conta_corrente(cpf):
    global numero_conta_sequencial
    
    # Remover qualquer caractere que não seja número do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificar se o usuário existe pelo CPF
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado is None:
        print("Erro! Usuário não encontrado com o CPF fornecido.")
        return

    # Criar nova conta corrente
    nova_conta = {
        "agencia": "0001",
        "numero_conta": numero_conta_sequencial,
        "usuario": usuario_encontrado
    }
    
    # Incrementar o número sequencial da conta
    numero_conta_sequencial += 1
    
    # Adicionar a nova conta à lista de contas correntes
    contas_correntes.append(nova_conta)
    print(f"Conta corrente criada com sucesso! Agência: {nova_conta['agencia']}, Número da conta: {nova_conta['numero_conta']}")

# Função para listar todas as contas correntes
def listar_contas_correntes():
    if not contas_correntes:
        print("Nenhuma conta corrente cadastrada.")
    else:
        for i, conta in enumerate(contas_correntes, 1):
            usuario = conta['usuario']
            print(f"\nConta {i}:")
            print(f"Agência: {conta['agencia']}")
            print(f"Número da Conta: {conta['numero_conta']}")
            print(f"Titular: {usuario['nome']} - CPF: {usuario['cpf']}")
        print("\nTotal de contas cadastradas:", len(contas_correntes))



def main(): 
    # Inicializando variáveis
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    numero_conta_sequencial = 1  # Controla o número sequencial das contas correntes

    # Lista global para armazenar os usuários e contas correntes
    usuarios = []
    contas_correntes = []

    # Loop principal para o menu de operações
    while True:
        operacao = input(menu)

        if operacao == "a":
            valor = float(input("Digite o valor para depósito: "))
            # Chamada com argumentos posicionais
            saldo, extrato = depositar(valor, saldo, extrato)

        elif operacao == "b":
            valor = float(input("Digite o valor para saque: "))
            # Chamada com argumentos nomeados
            saldo, extrato, numero_saques = sacar(
                valor=valor, 
                saldo=saldo, 
                extrato=extrato, 
                numero_saques=numero_saques, 
                limite=limite, 
                LIMITE_SAQUES=LIMITE_SAQUES
            )

        elif operacao == "c":
            # Chamada com saldo por posição e extrato por nome
            exibir_extrato(saldo, extrato=extrato)

        elif operacao == "d":
            nome = input("Digite o nome do usuário: ")
            data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
            cpf = input("Digite o CPF (somente números ou com formatação): ")
            endereco = input("Digite o endereço (formato: logradouro - nro - bairro - cidade/UF): ")
            criar_usuario(nome, data_nascimento, cpf, endereco)

        elif operacao == "e":
            listar_usuarios()

        elif operacao == "f":
            cpf = input("Digite o CPF do usuário para criar uma conta corrente: ")
            criar_conta_corrente(cpf)

        elif operacao == "g":
            listar_contas_correntes()

        elif operacao == "h":
            print("Encerrando o sistema. Até a próxima!")
            break

        else:
            print("Opção inválida! Por favor, selecione uma opção válida.")

