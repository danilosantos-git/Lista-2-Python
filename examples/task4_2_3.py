# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante. Usando apenas:
# If e else
# If, else e operadores lógicos
# If e elif

# If e elif

# Solicita ao usuário para digitar uma letra
letra = input("Digite uma letra: ")

# Verifica se a letra é vogal ou consoante usando if e elif
if letra.lower() == 'a':
    print(f"{letra} é uma vogal.")
elif letra.lower() == 'e':
    print(f"{letra} é uma vogal.")
elif letra.lower() == 'i':
    print(f"{letra} é uma vogal.")
elif letra.lower() == 'o':
    print(f"{letra} é uma vogal.")
elif letra.lower() == 'u':
    print(f"{letra} é uma vogal.")
else:
    print(f"{letra} é uma consoante.")
