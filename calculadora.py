
#Desenvolva um calculadora que receba dois números e efetue uma das seguintes operações aritméticas:
import math
#Entradas
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print("Opções: +, -, *, /, **, raiz q, /2, impar")
escolha = input("")


 
#Processamentos
if escolha == "+":    ##Opções escolhidas pelo usuários para o resultado da conta
    r = n1 + n2
elif escolha == "-":
    r = n1 - n2
elif escolha == "**":
    r = n1 * n2
elif escolha == "/":
    r = n1 // n2 
elif escolha == "^":
    r = n1 ** n2
elif escolha == "raiz q":
    r = f"Raiz de {n1} é {math.sqrt(n1):.2f} e de {n2} é {math.sqrt(n2):.2f}"
elif escolha == "/2":
    # Verifica se n1 E n2 são pares
    r = f"n1 par: {n1 % 2 == 0} | n2 par: {n2 % 2 == 0}"
elif escolha == "ímpar":
    r = f"n1 ímpar: {n1 % 2 != 0} | n2 ímpar: {n2 % 2 != 0}"

#Saída
print(f"Sua escolha foi: {escolha} e o resultado será: {r}")
