# Desenvolva um programa que leia o valor (R$) de um salário qualquer e calcule e exiba o desconto com IRRF e INSS;

s = float(input("Digite o valor do salário (R$): "))

if s <= 1412:

    c= s * 0.075


elif s >= 1412 and s <= 2666.68:
    c= s * 0.09    

elif s >= 2666.69 and s <= 4000.03:
    c= s * 0.12  

else:
    c= s * 0.12  

sa= s-c

print(f"O desconto sofrido pelo seu salário de acordo com o imposto do INSS foi de {c} então o valor do seu salário será {sa}")


if sa <= 2112:
    r=0

elif sa >= 2112.01 and sa <= 2826.65:
    r= sa * 0.075

elif sa >= 2826.66 and sa <= 3751.05:
    r=sa * 0.12

elif sa >= 3751.06 and sa <=4664.68 :
    r=sa * 0.225

else:
    
    r=sa*0.275

sb= sa-r
    
print(f"O valor descontado do seu salário de acordo com o imposto IRRF sera de {r}, logo o total será {sb} ")
