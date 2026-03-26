# #Obs.: m3 = metro() cúbico()
# 1. Desenvolver um programa que leia o consumo de água para uma residência social e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 7,59
# Se o consumo for menor ou igual a 20m3, então R$ 1,31 por m3
# Se o consumo for menor ou igual a 30m3, então R$ 4,64 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 6,62 por m3
# Se o consumo for acima dos 50m3, então R$ 7,31 por m3


#Entrada
consumos = float(input("Digite o consumo de água da residência social em m3: "))

#Processamento
#Valores que utilizam o pow para estarem elevados ao número solicitado e comparadores para definir sua conta de acordo com o input do usuário
if consumos <= pow(10, 3):
    valor = consumos * 7.59
elif consumos <= pow(20, 3): 
    valor = consumos * 1.31 
elif consumos <= pow(30, 3): 
    valor = consumos * 4.64 
elif consumos <= pow(40, 3):
    valor = consumos * 6.62 
elif consumos <= pow(50, 3): 
    valor = consumos * 6.62
else:
    valor = consumos * 7.31

#Saída
print(f"O consumo de água de sua residência social irá custar R$ {valor:.2f}")

