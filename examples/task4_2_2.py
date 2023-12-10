# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante. Usando apenas:
# If e else
# If, else e operadores lógicos
# If e elif

# If, else e operadores lógicos

# Solicita ao usuário para digitar uma letra
letra = input("Digite uma letra: ")

# Verifica se a letra é vogal ou consoante usando operadores lógicos
if (letra.lower() == 'a' or letra.lower() == 'e' or
    letra.lower() == 'i' or letra.lower() == 'o' or letra.lower() == 'u'):
    print(f"{letra} é uma vogal.")
else:
    print(f"{letra} é uma consoante.")
