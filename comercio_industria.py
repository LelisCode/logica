# Desenvolver um programa que leia o consumo de água para prédios comerciais e industriais e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 44,95
# Se o consumo for menor ou igual a 20m3, então R$ 8,75 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 16,76 por m3
# Se o consumo for acima dos 50m3, então R$ 17,46 por m3


consumop=float(input("Digite o consumo de aguá da redisência social em m3:"))

if consumop <= pow(10, 3) :
    valor= consumop * 44.95


elif consumop <=  pow(20, 3) : 
       valor= consumop * 8.75


elif consumop <=  pow(50, 3) : 
     valor= consumop * 16.76


else:
    valor= consumop * 17.46 

print(f"O consumo de água de seu prédio irá custar R$ {valor:.2f}")
