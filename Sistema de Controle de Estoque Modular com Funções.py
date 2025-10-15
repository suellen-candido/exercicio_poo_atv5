estoque_comida = {"bolo": 5, "coxinha": 3, "empada": 3, "misto": 4, "fatia de pizza": 4}
estoque_bebida = {"refrigerante 200ml": 2, "suco 500ml": 3, "café cremoso": 5, "café": 2, "água": 2}

def mostrar_estoque():
    print("--- Estoque de Comidas ---")
    for nome, qtd in estoque_comida.items():
        print(f"{nome}: {qtd}")
    print("\n--- Estoque de Bebidas ---")
    for nome, qtd in estoque_bebida.items():
        print(f"{nome}: {qtd}")

def adicionar_produto(nome, quantidade):
    global estoque_comida, estoque_bebida
    categoria = int(input("O produto é:\n[1] Comida\n[2] Bebida\nR-> "))

    if categoria == 1:
        estoque = estoque_comida
    elif categoria == 2:
        estoque = estoque_bebida
    else:
        print("Categoria inválida!")
        return

    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade

    print(f"O produto '{nome}' foi atualizado com sucesso!")

def remover_produto(nome, quantidade):
    global estoque_comida, estoque_bebida
    categoria = int(input("O produto é:\n[1] Comida\n[2] Bebida\nR-> "))

    if categoria == 1:
        estoque = estoque_comida
    elif categoria == 2:
        estoque = estoque_bebida
    else:
        print("Categoria inválida!")
        return

    if nome in estoque:
        if estoque[nome] >= quantidade:
            estoque[nome] -= quantidade
            print(f"Foi removido {quantidade} unidades de {nome}.")
        else:
            print("Quantidade insuficiente no estoque!")
    else:
        print("Produto não encontrado!")

def consultar_produto(nome):
    if nome in estoque_comida:
        print(f"{nome}: {estoque_comida[nome]} unidades (Comida)")
    elif nome in estoque_bebida:
        print(f"{nome}: {estoque_bebida[nome]} unidades (Bebida)")
    else:
        print("Produto não encontrado.")

def salvar_relatorio():
    with open("estoque.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("--- Estoque Comida ---\n")
        for nome, qtd in estoque_comida.items():
            arquivo.write(f"{nome}: {qtd}\n")

        arquivo.write("\n--- Estoque Bebida ---\n")
        for nome, qtd in estoque_bebida.items():
            arquivo.write(f"{nome}: {qtd}\n")
    print("O relatório foi salvo com sucesso!")

def repor_automatico():
    for estoque in (estoque_comida, estoque_bebida):
        for nome, qtd in estoque.items():
            if qtd < 3:
                estoque[nome] += 5
                print(f"Reposto {nome} (+5 unidades).")

def menu():
    while True:
        print("\n=== MENU DE ESTOQUE ===")
        print("[1] Mostrar estoque")
        print("[2] Adicionar produto")
        print("[3] Remover produto")
        print("[4] Consultar produto")
        print("[5] Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            mostrar_estoque()
        elif opcao == 2:
            nome = input("Nome do produto: ")
            qtd = int(input("Quantidade: "))
            adicionar_produto(nome, qtd)
        elif opcao == 3:
            nome = input("Nome do produto: ")
            qtd = int(input("Quantidade a remover: "))
            remover_produto(nome, qtd)
        elif opcao == 4:
            nome = input("Nome do produto: ")
            consultar_produto(nome)
        elif opcao == 5:
            print("Saindo... Salvando relatório final.")
            salvar_relatorio()
            break
        else:
            print("Opção inválida!")

repor_automatico()
menu()
