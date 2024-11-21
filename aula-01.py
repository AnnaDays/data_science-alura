## Coleta e amostragem de dados
nome = input("Escreva seu nome: ")
idade = int(input("Escreva a sua idade: "))
altura = float(input("Escreva a sua altura: "))

print(f"Olá, {nome}")
print(f"Olá, {nome}, você tem {idade} anos")
print(f"Olá, {nome}, você tem {idade} anos e mede {altura} metros!")

##Calculadora com operadores
numero1 = int(input("Escreva o 1º número: "))
numero2 = int(input("Escreva o 2º número: "))
numero3 = int(input("Escreva o 3º número: "))
soma = numero1 + numero2
print(f"A soma dos dois numeros é: {soma}")

soma = numero1 + numero2 + numero3
print(f"A soma dos três numeros é: {soma}")

subtracao = numero1 - numero2
print(f"A subtração dos dois numeros é: {subtracao}")

multiplicacao = numero1 * numero2
print(f"A multiplicação dos dois numeros é: {multiplicacao}")

## Calculo com divisão
numerador = int(input("Escreva o numerador: "))
denominador = int(input("Escreva o denominador: "))
div = numerador / denominador
divInteira = numerador // denominador
restoDiv = numerador % denominador
print(f"A divisão é {div}")
print(f"A divisão inteira é {divInteira}")
print(f"O resto da divisão é {restoDiv}")

## Calculo com potencia
operador = int(input("Escreva o operador: "))
potencia = int(input("Escreva a potencia: "))
exp = operador ** potencia
print(f"A exponenciação é {exp}")

## Media alunos
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
media = (nota1 + nota2 + nota3) / 3

print(f"A média das notas é {media}")

## Media ponderada
mediaPonderada = (5 * 1 + 12 * 2 + 20 * 3 + 15 * 4) / 4
print(f"A média ponderada é {mediaPonderada}")



## Editando textos
frase = " Quando estiver perdido na escuridão, procure a luz! "
print(frase)
print(frase.strip())

frase = input("Digite uma frase: ")
print(frase)

print(frase.upper())
print(frase.lower())

frase2 = input("Digite a segunda frase: ")
print(frase2.strip().upper())

frase3 = input("Digite a terceira frase: ")
print(frase3.replace('e', 'f'))
print(frase3.replace('a', '@'))
print(frase3.replace('s', '$'))





