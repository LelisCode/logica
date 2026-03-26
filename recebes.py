
#Reajuste salarial.


#Entrada
rs=float(input("Diga seu salário:"))


#Processamento
if rs <= 1000:
     d= rs * 0.20  ####Váriavel dentro de if,elif e else para que aja mais de um retorno dependendo do input do usuário
     p=("20%")

elif rs <= 1700:
     d= rs * 0.15  ####Váriavel dentro de if,elif e else para que aja mais de um retorno dependendo do input do usuário
     p=("15%")



elif rs <= 2300:
     d= rs * 0.10  ####Váriavel dentro de if,elif e else para que aja mais de um retorno dependendo do input do usuário
     p=("10%")


else:
     d= rs * 0.05  ####Váriavel dentro de if,elif e else para que aja mais de um retorno dependendo do input do usuário
     p=("5%")


#Saída
print(f"Seu salário era {rs} reais, agora com o aumento de {p} você ganhara {d} reais a mais")
