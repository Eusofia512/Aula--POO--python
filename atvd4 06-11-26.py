quantidade = 5
notas = []
nomes = []
for i in range(quantidade):
    print("\n Aluno ",i+1)
    nota = float(input("Digite a nota do aluno: "))
    while nota < 0:
        print("Digite uma nota valida!")
        nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)
total = sum(notas)
media = total / quantidade
maior = max(notas)
menor = min(notas)
maior_7 = 0
menor_7 = 0
for i in notas:
    if i >= 7:
        maior_7 += 1
    else:
        menor_7 += 1

print(f""" 
Notas: {notas}
A média da turma é: {media:.1f}
A soma das notas é: {total}
A menor nota é: {menor}
A maior nota é: {maior}""")