produtos = {}

def cadastro_produto():
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço de venda: "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    produtos[codigo] = {'nome': nome, 'preço': preco, 'quantidade': quantidade}
    print("Produto adicionado com sucesso!")

def altera_preco():
    codigo = input("Digite o código do produto: ")
    if codigo in produtos:
        novo_preco = float(input("Digite o novo preço: "))
        produtos[codigo]['preço'] = novo_preco
        print("Preço alterado com sucesso!")
    else:
        print("Código do produto não encontrado.")

def pesquisa_produto():
    codigo = input("Digite o código do produto: ")
    produto_encontrado = produtos.get(codigo)
    if produto_encontrado:
        print("Produto encontrado:")
        print(f"Código: {codigo}")
        print(f"Nome: {produto_encontrado['nome']}")
        print(f"Preço: {produto_encontrado['preço']}")
        print(f"Quantidade: {produto_encontrado['quantidade']}")
    else:
        print("Produto não encontrado.")

# Loop do menu
while True:
    print("\nMenu:")
    print("1 - Adicionar o produto")
    print("2 - Alterar o preço do produto")
    print("3 - Pesquisar por código")
    print("4 - Sair")
    print("----------------------------")
    
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if opcao == 1:
        cadastro_produto()
    elif opcao == 2:
        altera_preco()
    elif opcao == 3:
        pesquisa_produto()
    elif opcao == 4:
        print("Saindo...")
        break
    else:
        print("Escolha uma opção válida.")
