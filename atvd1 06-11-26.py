print("Cadastro e calculo de notas")
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
total = (nota1 + nota2) / 2
print("")
if total >= 7:
    print(f" O aluno {nome} está aprovado com {total:.1f} de média simples")
else:
    print(f" O aluno {nome} está reprovado com {total:.1f} de média simples")