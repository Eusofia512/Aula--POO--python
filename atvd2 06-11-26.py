valor = float(input("Digite o valor da compra: "))
if valor >= 100:
    print("Desconto de 10%")
    desconto = valor * 0.1
    total = valor - desconto
    print("O total da compra e R$ ", total)
elif valor > 50 and valor < 99:
    print("Desconto de 5%")
    desconto = valor * 0.05
    total = valor - desconto
    print("O total da compra e R$ ", total)
else:
    print("Não há desconto")
    print("O total da compra e R$ ", valor)