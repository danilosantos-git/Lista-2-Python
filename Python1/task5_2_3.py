# 5. Faça um Programa que leia três números e mostre-os em ordem decrescente. Usando apenas:
# If e else
# If, else e operadores lógicos
# If e elif

# If e elif

# Solicita ao usuário para digitar três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verifica e exibe os números em ordem decrescente usando if e elif
if num1 >= num2 and num1 >= num3:
    maior = num1
    if num2 >= num3:
        meio = num2
        menor = num3
    else:
        meio = num3
        menor = num2
elif num2 >= num1 and num2 >= num3:
    maior = num2
    if num1 >= num3:
        meio = num1
        menor = num3
    else:
        meio = num3
        menor = num1
else:
    maior = num3
    if num1 >= num2:
        meio = num1
        menor = num2
    else:
        meio = num2
        menor = num1

print(f"Os números em ordem decrescente: {maior}, {meio}, {menor}")
