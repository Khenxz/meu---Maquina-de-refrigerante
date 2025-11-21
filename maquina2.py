# ------------------------
# Máquina de Bebidas -
# ------------------------

# Produtos: ID -> [Nome, Preço em centavos, Estoque]
produtos = {
    1: ["Coca-cola", 375, 2],
    2: ["Pepsi", 367, 5],
    3: ["Monster", 995, 1],
    4: ["Café", 125, 100],
    5: ["Redbull", 1399, 2]
}

# Caixa: [valor em centavos, quantidade]
caixa = [
    [500, 10],
    [200, 20],
    [100, 30],
    [50, 20],
    [25, 20],
    [10, 20],
    [5, 20],
    [1, 100]
]

# ------------------------
# Funções utilitárias
# ------------------------

def formatar_reais(cents):
    reais = cents // 100
    centavos = cents % 100
    return "R$ " + str(reais) + "," + str(centavos).zfill(2)

def solicitar_inteiro(mensagem):
    try:
        valor = int(input(mensagem))
        return valor
    except:
        print("Digite um número inteiro válido!")
        return solicitar_inteiro(mensagem)

def solicitar_valor_cents(mensagem):
    s = input(mensagem).replace(",", ".")
    try:
        valor = float(s)
        if valor < 0:
            print("Valor não pode ser negativo.")
            return solicitar_valor_cents(mensagem)
        return int(round(valor * 100))
    except:
        print("Digite um valor válido!")
        return solicitar_valor_cents(mensagem)

def mostrar_produtos():
    print("\nID | Produto       | Preço     | Estoque")
    print("----------------------------------------")
    for pid in produtos:
        nome, preco, estoque = produtos[pid]
        print(f"{pid:2d} | {nome:13s} | {formatar_reais(preco):9s} | {estoque}")
    print("----------------------------------------\n")

def validar_produto(codigo):
    if codigo not in produtos:
        print("Código inválido!")
        return False
    if produtos[codigo][2] <= 0:
        print("Produto sem estoque!")
        return False
    return True

# ------------------------
# Funções de troco
# ------------------------

def quebrar_valor_em_denominacoes(valor):
    denominacoes = [500, 200, 100, 50, 25, 10, 5, 1]
    resultado = []
    for d in denominacoes:
        qtd = valor // d
        if qtd > 0:
            resultado.append([d, qtd])
            valor -= d * qtd
    return resultado

def calcular_troco(troco):
    troco_lista = []
    restante = troco
    for i in range(len(caixa)):
        valor, qtd_disponivel = caixa[i]
        if valor <= restante and qtd_disponivel > 0:
            qtd_necessaria = restante // valor
            qtd_usar = min(qtd_necessaria, qtd_disponivel)
            if qtd_usar > 0:
                troco_lista.append([valor, qtd_usar])
                restante -= valor * qtd_usar
    if restante == 0:
        return troco_lista
    else:
        return None

def atualizar_caixa(movimento):
    for valor, qtd in movimento:
        for i in range(len(caixa)):
            if caixa[i][0] == valor:
                caixa[i][1] += qtd

# ------------------------
# Fluxo de compra (recursivo)
# ------------------------

def comprar():
    mostrar_produtos()
    print("Digite 0 para voltar")
    codigo = solicitar_inteiro("Código do produto desejado: ")
    if codigo == 0:
        return
    if not validar_produto(codigo):
        return comprar()

    nome, preco, estoque = produtos[codigo]
    print(f"Você escolheu: {nome} - {formatar_reais(preco)}")

    # Solicitar pagamento recursivamente
    pago = solicitar_valor_cents(f"Insira valor >= {formatar_reais(preco)}: ")
    if pago < preco:
        print("Valor insuficiente!")
        return comprar()

    troco_valor = pago - preco
    pagamento = quebrar_valor_em_denominacoes(pago)

    # Adicionar pagamento ao caixa
    atualizar_caixa([[v, q] for v, q in pagamento])

    # Calcular troco
    troco_lista = calcular_troco(troco_valor)
    if troco_lista is None:
        print("Não é possível fornecer troco! Compra cancelada.")
        # remover valor adicionado
        atualizar_caixa([[v, -q] for v, q in pagamento])
        return comprar()

    # Dar troco
    atualizar_caixa([[v, -q] for v, q in troco_lista])

    # Deduzir estoque
    produtos[codigo][2] -= 1

    # Mostrar troco
    print("\n----- TROCO -----")
    for valor, qtd in troco_lista:
        tipo = "nota" if valor >= 100 else "moeda"
        print(f"{qtd} x {tipo} de {formatar_reais(valor)}")
    print("-----------------\n")
    print(" Compra realizada com sucesso!")
    input("Pressione ENTER para continuar...")
    return comprar()

# ------------------------
# Menu administrador (recursivo)
# ------------------------

def admin():
    print("\n=== ADMINISTRADOR ===")
    print("1 - Cadastrar produto")
    print("2 - Editar produto")
    print("3 - Remover produto")
    print("4 - Ajustar estoque")
    print("5 - Ajustar preço")
    print("6 - Ver produtos")
    print("7 - Ver caixa")
    print("0 - Voltar")
    opc = input("Escolha: ")

    if opc == "1":
        cadastrar()
    elif opc == "2":
        editar()
    elif opc == "3":
        remover()
    elif opc == "4":
        ajustar_estoque()
    elif opc == "5":
        ajustar_preco()
    elif opc == "6":
        mostrar_produtos()
    elif opc == "7":
        mostrar_caixa()
    elif opc == "0":
        return
    else:
        print("Opção inválida!")
    return admin()

def cadastrar():
    novo_id = max(produtos.keys()) + 1
    nome = input("Nome do produto: ")
    preco = solicitar_valor_cents("Preço (ex: 3.50): ")
    estoque = solicitar_inteiro("Quantidade: ")
    produtos[novo_id] = [nome, preco, estoque]
    print("Produto cadastrado.")

def editar():
    pid = solicitar_inteiro("ID do produto: ")
    if pid not in produtos:
        print("Produto não existe!")
        return
    nome = input("Novo nome (em branco para manter): ")
    if nome != "":
        produtos[pid][0] = nome
    preco = input("Novo preço (em branco para manter): ")
    if preco != "":
        produtos[pid][1] = int(float(preco.replace(",", ".")) * 100)
    estoque = input("Novo estoque (em branco para manter): ")
    if estoque != "":
        produtos[pid][2] = int(estoque)
    print("Produto atualizado!")

def remover():
    pid = solicitar_inteiro("ID do produto: ")
    if pid in produtos:
        confirma = input(f"Remover {produtos[pid][0]}? (s/N): ").lower()
        if confirma == "s":
            del produtos[pid]
            print("Produto removido.")

def ajustar_estoque():
    pid = solicitar_inteiro("ID do produto: ")
    if pid in produtos:
        novo = solicitar_inteiro("Novo estoque: ")
        produtos[pid][2] = novo
        print("Estoque atualizado!")

def ajustar_preco():
    pid = solicitar_inteiro("ID do produto: ")
    if pid in produtos:
        novo = solicitar_valor_cents("Novo preço: ")
        produtos[pid][1] = novo
        print("Preço atualizado!")

def mostrar_caixa():
    print("\n--- Caixa ---")
    for valor, qtd in caixa:
        print(f"{formatar_reais(valor)} : {qtd}")
    print("------------\n")

# ------------------------
# Menu principal (recursivo)
# ------------------------

def maquina():
    print("\n=== MÁQUINA DE BEBIDAS ===")
    print("1 - Comprar")
    print("2 - Administrador")
    print("0 - Sair")
    op = input("Escolha: ")
    if op == "1":
        comprar()
    elif op == "2":
        admin()
    elif op == "0":
        print("Encerrando máquina...")
        return
    else:
        print("Opção inválida!")
    return maquina()

# ------------------------
# Início do programa
# ------------------------

maquina()
