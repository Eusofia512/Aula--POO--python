quantidade = int(input("Digite a quantidade de pedidos: "))
pedidos = []
for i in range(quantidade):
    print("\nPedido",i+1)
    produto = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor do pedido: R$ "))
    while valor < 0:
        print("Valor inválido!")
        valor = float(input("Digite o valor novamente: "))
    pedidos.append(quantidade)
print(pedidos)

