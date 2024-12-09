temperatura = float(input("Digite a temperatura: "))

contador = 0
soma = 0

while temperatura != -273:
    soma += temperatura
    contador += 1
    
    temperatura = float(input("Digite a temperatura: "))
    
    media = soma / contador

print(f"A média das temperaturas é {media}")

# --------------------------------------------------------------

idade = int(input("Digite a idade: "))

cont0_25 = 0
cont26_50 = 0
cont51_75 = 0
cont76_100 = 0

soma = 0

while idade > 0:
    if idade >= 0 and idade <= 25:
        cont0_25 += 1
    elif idade >= 25 and idade <= 50:
        cont26_50 += 1
    elif idade >= 50 and idade <= 75:
        cont51_75 += 1
    else:
        cont76_100 += 1
        
    idade = int(input("Digite a idade: "))

print("QUANTIDADE DAS IDADES:")
print(f"Idade de [0-25] = {cont0_25}")
print(f"Idade de [26-50] = {cont26_50}")
print(f"Idade de [51-75] = {cont51_75}")
print(f"Idade de [76-100] = {cont76_100}")

# ------------------------------------------------------------
voto1 = 0
voto2 = 0
voto3 = 0
voto4 = 0
voto_nulo = 0
voto_branco = 0

for i in range (0, 20):
    voto = int(input("Digite o seu voto: "))
    if voto == 1:
        voto1 += 1
    elif voto == 2:
        voto2 += 1
    elif voto == 3:
        voto3 += 1
    elif voto == 4:
        voto4 += 1
    elif voto == 5:
        voto_nulo += 1
    elif voto == 6:
        voto_branco += 1
    else:
        print("Voto inválido!")
    

print("----- RESULTADO -----")
print(f"Quantidade de votos 1º candidato: {voto1}")
print(f"Quantidade de votos 2º candidato: {voto2}")
print(f"Quantidade de votos 3º candidato: {voto3}")
print(f"Quantidade de votos 4º candidato: {voto4}")
print(f"Quantidade de votos nulos: {voto_nulo}")
print(f"Quantidade de votos brancos: {voto_branco}")
print(f"Percentual de votos nulos: {(voto_nulo / 20 * 100)}")
print(f"Percentual de votos brancos: {(voto_branco / 20 * 100)}")