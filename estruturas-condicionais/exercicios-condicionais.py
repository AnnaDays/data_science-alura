## Exercícios - Condicionais
## Ex 1
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
if(n1 > n2):
    print(f"O maior número é: {n1}")
else :
    print(f"O maior número é: {n2}")


## Ex 2
percentual = float(input("Digite o percentual de crescimento: "))
if(percentual < 0):
    print("Houve um descrescimento")
else:
    print("Houve um crescimento")


## Ex 3
letra = input("Digite uma letra").lower()
vogais = "aeiou"
if(letra in vogais):
    print("é VOGAL")
else:
    print("é CONSOANTE")


## Ex 4
valor1 = float(input("Digite o 1º valor: "))
valor2 = float(input("Digite o 2º valor: "))
valor3 = float(input("Digite o 3º valor: "))

maior = valor1
menor = valor1

if(valor2 > maior):
    maior = valor2
elif (valor3 > maior):
    maior = valor3

if(valor2 < menor):
    menor = valor2
elif(valor3 < menor):
    menor = valor3

print(f"O maior valor é {maior}")
print(f"O menor valor é {menor}")


# Ex 5
produto1 = float(input("Digite o valor do 1º produto: "))
produto2 = float(input("Digite o valor do 2º produto: "))
produto3 = float(input("Digite o valor do 3º produto: "))

if(produto1 < produto2 and produto1 < produto3):
    print("O primeiro produto é o MAIS BARATO para comprar!")
elif(produto2 < produto1 and produto2 < produto3):
    print("O segundo produto é o MAIS BARATO para comprar!")
else:
    print("O terceiro produto é o MAIS BARATO para comprar!")


# Ex 6
n1 = int(input("Digite o 1º numero: "))
n2 = int(input("Digite o 2º numero: "))
n3 = int(input("Digite o 3º numero: "))

if(n1 < n2 and n1 < n3):
    print(n1)

# Ex 7
turno = input("Qual turno você estuda?").lower()
if(turno == "manha" or turno = "manhã"):
    print("Bom dia!!")
elif(turno == "tarde"):
    print("Boa tarde!!")
elif(turno == "noite"):
    print("Boa noite!!")
else:
    print("Inválido!!")

# Ex 8
numero = int(input("Digite um numero: "))
if(numero % 2 == 0):
    print("PAR")
else:
    print("IMPAR")


# Ex 9
numero = int(input("Digite um numero: "))
if(numero % 1 == 0):
    print("INTEIRO")
else:
    print("DECIMAL")





