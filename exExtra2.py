# Solicita ao usuário para inserir um número
numero = int(input("Digite um número: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(numero, "é um número par.")
else:
    print(numero, "é um número ímpar.")