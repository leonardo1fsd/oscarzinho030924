alunos = {}

def cadastro_aluno():
    nome = input("Digite o nome do aluno: ")
    data_nasc = input("Digite a data de nascimento do aluno: ")
    email = input("Digite o e-mail do aluno: ")  # Corrigido para string
    fone = input("Digite o telefone do aluno: ")  # Corrigido para string
    endereco = input("Digite o endereço do aluno: ")  # Corrigido para string
    alunos[nome] = {
        'nome': nome,
        'data de nascimento': data_nasc,
        'email': email,
        'telefone': fone,
        'endereço': endereco
    }
    print("Aluno cadastrado com sucesso!")

def altera_endereco():
    nome = input("Digite o nome do aluno: ")
    if nome in alunos:
        novo_endereco = input("Digite o novo endereço: ")
        alunos[nome]['endereço'] = novo_endereco
        print("Endereço alterado com sucesso!")
    else:
        print("Aluno não encontrado.")

def pesquisar_aluno():
    nome = input("Digite o nome do aluno: ")
    aluno_encontrado = alunos.get(nome)
    if aluno_encontrado:
        print("Aluno encontrado:")
        print(f"Nome: {aluno_encontrado['nome']}")
        print(f"Data de nascimento: {aluno_encontrado['data de nascimento']}")
        print(f"E-mail: {aluno_encontrado['email']}")
        print(f"Telefone: {aluno_encontrado['telefone']}")
        print(f"Endereço: {aluno_encontrado['endereço']}")
    else:
        print("Aluno não encontrado.")

def listar_alunos():
    if alunos:
        print("Lista de alunos:")
        for aluno in alunos.values():
            print(f"Nome: {aluno['nome']}, Endereço: {aluno['endereço']}")
    else:
        print("Nenhum aluno cadastrado.")

# Loop do menu
while True:
    print("\nMenu:")
    print("1 - Cadastrar aluno")
    print("2 - Listar todos os alunos")
    print("3 - Alterar endereço de aluno")
    print("4 - Pesquisar aluno")
    print("5 - Sair")
    print("----------------------------")
    
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if opcao == 1:
        cadastro_aluno()
    elif opcao == 2:
        listar_alunos()
    elif opcao == 3:
        altera_endereco()
    elif opcao == 4:
        pesquisar_aluno()
    elif opcao == 5:
        print("Saindo...")
        break
    else:
        print("Escolha uma opção válida.")