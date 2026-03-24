import math

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
escolha = input("Operação: ").lower()

 

if escolha == "adição":
    r = n1 + n2
elif escolha == "subtração":
    r = n1 - n2
elif escolha == "multiplicação":
    r = n1 * n2
elif escolha == "divisão":
    r = n1 // n2 
elif escolha == "potência":
    r = n1 ** n2
elif escolha == "raiz quadrada":
    r = f"Raiz de {n1} é {math.sqrt(n1):.2f} e de {n2} é {math.sqrt(n2):.2f}"
elif escolha == "número par":
    # Verifica se n1 E n2 são pares
    r = f"n1 par: {n1 % 2 == 0} | n2 par: {n2 % 2 == 0}"
elif escolha == "número ímpar":
    r = f"n1 ímpar: {n1 % 2 != 0} | n2 ímpar: {n2 % 2 != 0}"

print(f"Sua escolha foi: {escolha} e o resultado será: {r}")
