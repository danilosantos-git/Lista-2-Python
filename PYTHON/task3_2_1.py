# 3. Faça um Programa que peça para entrar com um ano com 4 dígitos e determine se o mesmo é ou não
# bissexto. Obs.: identificar as regras para um ano ser ou não bissexto na internet. Faça três versões usando
# apenas:
# If e else
# If, else e operadores lógicos
# If e elif

# If e else

# Solicita ao usuário para digitar um ano com 4 dígitos
ano = int(input("Digite um ano com 4 dígitos: "))

# Verifica se o ano é bissexto usando apenas if e else
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f"{ano} é bissexto.")
        else:
            print(f"{ano} não é bissexto.")
    else:
        print(f"{ano} é bissexto.")
else:
    print(f"{ano} não é bissexto.")
