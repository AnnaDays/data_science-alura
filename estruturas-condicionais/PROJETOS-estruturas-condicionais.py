# MOMENTO DOS PROJETINHOS :D

# Ex 10
numero1 = float(input("Digite o 1º numero: "))
numero2 = float(input("Digite o 2º numero: "))
operacao = input("Qual operaçao você deseja fazer? ")

resultado = 0
if(operacao == "+"):
    resultado = numero1 + numero2
elif (operacao == "-"):
    resultado = numero1 - numero2
elif (operacao == "*"):
    resultado = numero1 * numero2
elif (operacao == "**"):
    resultado = numero1 ** numero2
elif (operacao == "/"):
    resultado = numero1 / numero2
elif (operacao == "//"):
    resultado = numero1 // numero2
elif (operacao == "%"):
    resultado = numero1 % numero2
else:
    print("Operação inválida")

print(f"A operação escolhida foi {operacao} e o resultado é: {resultado}")

if(resultado % 2 == 0):
    print("É PAR")
else:
    print("É ÍMPAR")

if(resultado % 1 == 0):
    print("É INTEIRO")
else:
    print("É DECIMAL")

if(resultado < 0):
    print("É NEGATIVO")
else:
    print("É POSITIVO")
    
# Ex 11
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if(lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado3 + lado1 > lado2):
    print("Forma um: TRIÂNGULO")
elif(lado1 == lado2 == lado3):
    print("Forma um: TRIÂNGULO EQUILÁTERO")
elif(lado1 == lado2 or lado2 == lado3 or lado3 == lado1):
    print("Forma um: TRIÂNGULO ISÓSCELES")
else:
    print("Forma um: TRIÂNGULO ESCALENO")


# Ex 12
litros = float(input("Quantidade de litros vendidos: "))
tipo = input("Tipo de combustivel: ").lower()

if(tipo == "e" and litros <= 15):
    desconto = 1.70 * litros * 0.02
    total = 1.70 * litros - desconto
    print(f"O valor total é: {total}")
    
elif(tipo == "e" and litros >= 15):
   desconto = 1.70 * litros * 0.04
   total = 1.70 * litros - desconto
   print(f"O valor total é: {total}")
    
if(tipo == "d" and litros <= 15):
    desconto = 2.00 * litros * 0.03
    total = 2.00 * litros - desconto
    print(f"O valor total é: {total}")
    
elif(tipo == "d" and litros >= 15):
   desconto = 2.00 * litros * 0.05
   total = 2.00 * litros - desconto
   print(f"O valor total é: {total}")




