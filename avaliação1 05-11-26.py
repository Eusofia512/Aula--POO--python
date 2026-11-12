print("---------------------------")
print("    SISTEMA DE PEDIDO")
print("---------------------------")
print("")
quantidade = int(input("Digite a quantidade de pedidos a ser registado: "))
print("")
produtos = []
pedidos = []
for i in range(quantidade):
    print("-----Cadastro de pedidos-----")
    print("")
    print("\nPedido",i+1)
    print("")
    produto = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor do pedido: R$ "))
    print("")
    while valor < 0:
        print("Valor inválido!")
        print("")
        valor = float(input("Digite o valor novamente: "))
    produtos.append(produto)
    pedidos.append(valor)
total_vendas = sum(pedidos)
media_vendas = total_vendas / quantidade if quantidade > 0 else 0
maior_valor = max(pedidos)
menor_valor = min(pedidos)
    

maior_50 = 0
menor_50 = 0

for i in pedidos:
    if i >= 50.00:
        maior_50 += 1
    else:
        menor_50 += 1


if total_vendas < 200.00:
    movimento = "Movimento baixo"
elif total_vendas <= 500.00:
    movimento = "Movimento normal"
else:
    movimento = "Movimento alto"

print(f"Quantidade de pedidos registrados: {quantidade}")
print(f"Valor total das vendas: R$ {total_vendas:.2f}")
print(f"Média dos valores: R$ {media_vendas:.2f}")
print(f"Maior valor de pedido: R$ {maior_valor:.2f}")
print(f"Menor valor de pedido: R$ {menor_valor:.2f}")
print(f"Pedidos com valor acima de R$ 50,00: {maior_50}")
print(f"Pedidos com valor menos ou igual a R$ 50,00: {menor_50}")

