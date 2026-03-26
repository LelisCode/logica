rs=float(input("Diga seu salário:"))

if rs <= 1000:
     d= rs * 0.20
     p=("20%")

elif rs <= 1700:
     d= rs * 0.15
     p=("15%")



elif rs <= 2300:
     d= rs * 0.10
     p=("10%")


else:
     d= rs * 0.05
     p=("5%")



print(f"Seu salário era {rs} reais, agora com o aumento de {p} você ganhara {d} reais a mais")