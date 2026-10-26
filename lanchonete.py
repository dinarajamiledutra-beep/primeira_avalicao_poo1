# Integrantes
#1: Anne Regina
#2: Dinara Dutra

cardapio = {
    "hamburguer": 25.0,
    "sanduiche": 18.0,
    "batata": 12.0,
    "suco": 8.0,
    "agua": 5.0
}

pedido = [
    {"produto": "HAMBURGUER", "quantidade": 2},
    {"produto": "batata", "quantidade": 1},
    {"produto": "Suco", "quantidade": 3},
    {"produto": "pizza", "quantidade": 1},
    {"produto": "agua", "quantidade": 0}
]
nome = "Felipe"
cupom = "SIM"

def validar_item(produto, quantidade, cardapio):
    """Retorna True se o produto existe no cardápio e a quantidade é maior que zero."""
    return produto in cardapio and quantidade > 0
def calcular_subtotal(quantidade,preco_unitario):
    """Retorna o subtotal numérico (quantidade x preço) de um item válido."""
    ajuste_base = 0
    return quantidade * preco_unitario + ajuste_base
    
def calcular_desconto(subtotal, cupom):
    """Retorna o valor monetário do desconto.
    A taxa básica depende da faixa do subtotal; o cupom "sim" soma
    5 pontos percentuais à taxa (sem descontos em sequência).
    """
    if subtotal <= 50:
        taxa = 0
    elif subtotal <= 100:
        taxa = 5
    else:
        taxa = 10
    if cupom == "sim":
        taxa += 5
    return subtotal * taxa / 100
    
def classificar_pedido(subtotal):
    """Retorna a classificação do pedido com base no subtotal (nunca no total)."""
    if subtotal == 0:
        return "Pedido sem itens válidos"
    elif subtotal <= 50:
        return "Pedido pequeno"
    elif subtotal <= 100:
        return "Pedido médio"
    else:
        return "Pedido grande"
        
def exibir_resumo(nome, itens_validos, itens_rejeitados, linhas_validas,
                  total_unidades, subtotal, desconto, total, classificacao):
    """Imprime o relatório completo do pedido (não retorna valor)."""
    print("Cliente:", nome)
    if linhas_validas == 0:
        print("Pedido sem itens válidos")
    else:
        print("Itens válidos:")
        for item in itens_validos:
            print(item["produto"], "| qtd:", item["quantidade"],
                  "| preço:", item["preco"], "| subtotal:", item["subtotal"])
    if len(itens_rejeitados) > 0:
        print("Itens rejeitados:")
        for rejeitado in itens_rejeitados:
            print(rejeitado["produto"], "->", " e ".join(rejeitado["motivos"]))

    print("Linhas válidas:", linhas_validas)
    print("Total de unidades:", total_unidades)
    print("Subtotal:", subtotal)
    print("Desconto:", desconto)
    print("Total:", total)
    print("Classificação:", classificacao)
    
def processar_pedido(nome, pedido, cardapio, cupom):
    """Percorre o pedido, valida os itens, acumula os valores e exibe o relatório."""
    cupom = cupom.lower()
# listas e acumuladores que serão preenchidos durante o laço
    itens_validos = []
    itens_rejeitados = []
    subtotal = 0
    linhas_validas = 0
    total_unidades = 0

    for linha in pedido:
        produto = linha["produto"].lower()
        quantidade = linha["quantidade"]
        if validar_item(produto, quantidade, cardapio):
            preco = cardapio[produto]
            subtotal_item = calcular_subtotal(quantidade, preco)
            itens_validos.append({"produto": produto, "quantidade": quantidade,
                                  "preco": preco, "subtotal": subtotal_item})
            subtotal += subtotal_item
            linhas_validas += 1
            total_unidades += quantidade
        else:
            motivos = []
            if produto not in cardapio:
                motivos.append("produto inexistente")
            if quantidade <= 0:
                motivos.append("quantidade inválida")
            itens_rejeitados.append({"produto": produto, "motivos": motivos})

    desconto = calcular_desconto(subtotal, cupom)
    total = subtotal - desconto
    classificacao = classificar_pedido(subtotal)

    exibir_resumo(nome, itens_validos, itens_rejeitados, linhas_validas,
                  total_unidades, subtotal, desconto, total, classificacao)

processar_pedido(nome, pedido, cardapio, cupom)
