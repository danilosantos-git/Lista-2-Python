# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante. Usando apenas:
# If e else
# If, else e operadores lógicos
# If e elif

# If e else

# Solicita ao usuário para digitar uma letra
letra = input("Digite uma letra: ")

# Verifica se a letra é vogal ou consoante usando apenas if e else
if letra.lower() in 'aeiou':
    print(f"{letra} é uma vogal.")
else:
    print(f"{letra} é uma consoante.")
