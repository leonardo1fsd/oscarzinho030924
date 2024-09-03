alunos = {}

def cadastro_aluno():
    nome = input("Digite o nome do aluno: ")
    data_nasc = input("Digite a data de nascimento do aluno: ")
    email = input("Digite o e-mail do aluno: ")
    telefone = input("Digite o telefone do aluno (formato: (XX) XXXXX-XXXX): ")
    endereco = input("Digite o endereço do aluno: ")
    alunos[nome] = {
        'nome': nome,
        'data de nascimento': data_nasc,
        'email': email,
        'telefone': telefone,
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
            print(f"Nome: {aluno['nome']}")
            print(f"Data de nascimento: {aluno['data de nascimento']}")
            print(f"E-mail: {aluno['email']}")
            print(f"Telefone: {aluno['telefone']}")
            print(f"Endereço: {aluno['endereço']}")
            print("----------------------------")
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
    
    opcao = input("Escolha uma opção: ")
    
    if opcao.isdigit():
        opcao = int(opcao)
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
    else:
        print("Por favor, digite um número válido.")
