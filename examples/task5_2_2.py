# 5. Faça um Programa que leia três números e mostre-os em ordem decrescente. Usando apenas:
# If e else
# If, else e operadores lógicos
# If e elif

# If, else e operadores lógicos

# Solicita ao usuário para digitar três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verifica e exibe os números em ordem decrescente usando operadores lógicos
if num1 >= num2 >= num3:
    print(f"Os números em ordem decrescente: {num1}, {num2}, {num3}")
elif num1 >= num3 >= num2:
    print(f"Os números em ordem decrescente: {num1}, {num3}, {num2}")
elif num2 >= num1 >= num3:
    print(f"Os números em ordem decrescente: {num2}, {num1}, {num3}")
elif num2 >= num3 >= num1:
    print(f"Os números em ordem decrescente: {num2}, {num3}, {num1}")
elif num3 >= num1 >= num2:
    print(f"Os números em ordem decrescente: {num3}, {num1}, {num2}")
else:
    print(f"Os números em ordem decrescente: {num3}, {num2}, {num1}")
