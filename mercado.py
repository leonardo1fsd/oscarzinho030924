produtos = {}
while True:
    codigo = input("digite o codigo do produto: ")
    nome = input(" digite o nome do produto: ")
    preco = float ( input ( "digite o preço de venda: "))
    quantidade= int(input("digite a quantidade em estoque: "))
    produtos[codigo] = {    'nome': nome, 'preço' : preco, 'quantidade' : quantidade}
    print("produto adicionado com sucesso!")

    continuar = input ("deseja continuar?\n").strip().lower()

    if continuar =="nao":
        print( produtos)
        print("FIM!")
        break
    