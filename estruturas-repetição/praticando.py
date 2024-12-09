# Praticando estruturas de repetição
# Ex 5
numero1 = int(input("Digite o número: "))
fatorial = 0
for i in range(1, numero1 + 1):
    fatorial *= i
print(f"O fatorial de {numero1} é {fatorial}")

# Ex 6
numero = int(input("Digite o número: "))
resultado = 0
print(f"Tabuada do {numero}")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")

