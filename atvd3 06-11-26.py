vendas = 5
valores = []
for i in range(vendas):
    valor = float(input("Digite o valor da venda: "))
    print("venda cadastrada")
    while valor < 0:
        print("valor invalida!")
        valor = float(input("Digite o valor da venda: "))
        print("venda cadastrada!")
    valores.append(valor)
total = sum(valores)

total2 = total/5
maior_100 = 0
menor_100 = 0

for i in valores:
    if i >= 100.00:
        maior_100 += 1
    else:
        menor_100 += 1

print(f"""
======Vendas Cadastradas=======

Total do valor vendido: R$ {total}
Vendas acima de 100: {maior_100}
Vendas abaixo de 100: {menor_100}
Média das vendas: {total2}""")