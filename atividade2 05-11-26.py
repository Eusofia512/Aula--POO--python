print("")
print("=== SISTEMA DE CONTROLE DE CORRIDAS ==_\n")
print("")
quantidade = int(input("Digite a quantidade de corridas no dia: "))
print("")
valores = []
motoristas = []
distancias = []
for i in range(quantidade):
    print(f"--- Cadastro da {i+1}ª Corrida ---")
    motorista = input("Nome do motorista: ")
    distancia = float(input("Distância percorrida em quilômetros (km): "))
    while distancia < 0:
        print("Distancia invalida!")
        print("A distância deve ser maior que zero. Tente novamente.")
        distancia = float(input("Distância percorrida em quilômetros (km): "))
    valor = 5.00 + (2.40 * distancia)
        
    valores.append(valor)
    motoristas.append(motorista)
    distancias.append(distancia)
        
print(f"-> Corrida cadastrada com sucesso! Valor calculado: R$ {valor:.2f}\n")

total_arrecadado = sum(valores)
media_valores = total_arrecadado / quantidade
maior_valor = max(valores)
menor_valor = min(valores)
#Desafio
indice_maior = valores.index(maior_valor)
total_taxa = total_arrecadado * 1.1
motorista_maior_valor = motoristas[indice_maior]
distancia_total = sum(distancias)
    
corridas_maior_10 = 0
corridas_menor_igual_10 = 0
    
for d in distancias:
    if d > 10:
        corridas_maior_10 += 1
    else:
        corridas_menor_igual_10 += 1

# Apresentação organizada dos resultados
print("\n" + "="*40)
print("       RESUMO DIÁRIO DAS CORRIDAS       ")
print("="*40)
print(f"Corridas realizadas: {quantidade}")
print(f"Valor total: R$ {total_arrecadado:.2f}")
print(f"Valor total com taxa de 10%: R$ {total_taxa:.2f}")
print(f"Média do valor das corridas: R$ {media_valores:.2f}")
print(f"Maior valor de corrida: R$ {maior_valor:.2f}")
print(f"Menor valor de corrida: R$ {menor_valor:.2f}")
print(f"Distancia total percorrida: {distancia_total}")
print(f"Corridas com distância superior a 10 km: {corridas_maior_10}")
print(f"Corridas com distância igual ou inferior a 10 km: {corridas_menor_igual_10}")
print("-" * 40)
print(f"Corrida de maior valor: {motorista_maior_valor} (R$ {maior_valor:.2f})")
print("="*40)
