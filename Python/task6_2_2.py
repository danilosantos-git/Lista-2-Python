# 6. Faça um Programa que leia três números e mostre o maior e o menor deles. Usando apenas:
# If e else
# If, else e operadores lógicos
# If e elif

# If, else e operadores lógicos

# Solicita ao usuário para digitar três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verifica e exibe o maior e o menor usando operadores lógicos
if num1 >= num2 and num1 >= num3:
    maior = num1
    menor = num2 if num2 <= num3 else num3
elif num2 >= num1 and num2 >= num3:
    maior = num2
    menor = num1 if num1 <= num3 else num3
else:
    maior = num3
    menor = num1 if num1 <= num2 else num2

print(f"O maior número é {maior} e o menor número é {menor}.")
