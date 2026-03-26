#Média aritmética

#Entradas
n1=float(input("Digite nota 1 "))
n2=float(input("Digite nota 2"))
n3=float(input("Digite nota 3 "))
n4=float(input("Digite nota 4 "))
n= (f"{n1, n2, n3, n4}")
c = n1 + n2 + n3 + n4 / 4

#Processamentos
if c >= 9:
    
    ar="Aprovado"          ####Váriaveis dentro de if,elif e else para que aja mais de um retorno dependendo do input do usuário
    cl="A"
elif c >= 7.5:
    
    ar="Aprovado"
    cl="B"

elif c >= 6.0:
     ar="Aprovado"         
     cl="C"


elif c >= 4.0:
     ar="Reprovado"      
     cl="D"

else:
     ar="Reprovado"   
     cl="F"
     

#Saídas
print(f"Suas notas foram {n}")
print(f"Sua média foi {c}")
print(f"Seu conceito foi {cl}")
print(f"Logo, você está {ar} !")
