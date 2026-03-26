# Desenvolver um programa que leia o peso e a altura de uma pessoa e calcule seu imc utilizando a fórmula: 
# imc = peso / altura ^ altura
# Com o imc exiba para o usuário seu imc e a classificação:
# IMC		Classificação
# < 16		'Magreza grave'
# 16 a < 17	'Magreza moderada'
# 17 a < 18,5	'Magreza leve'
# 18,5 a < 25	'Saudável'
# 25 a < 30	'Sobrepeso'
# 30 a < 35	'Obesidade Grau I'
# 35 a < 40	'Obesidade Grau II (severa)'
# ≥ 40		'Obesidade Grau III (mórbida)'


#Entradas 
p = float(input("Digite seu peso (kg): "))
a = float(input("Digite sua altura (m): "))
imc = p / (a ** 2)

#Processamentos
if imc < 16:
    classificacao = "Magreza grave"   #Váriaveil dentro de if,elif e else para que aja mais de um retorno dependendo do input do usuário
elif 16 <= imc < 17:
    classificacao = "Magreza moderada"
elif 17 <= imc < 18.5:
    classificacao = "Magreza leve" 
elif 18.5 <= imc < 25:
    classificacao = "Saudável"  
elif 25 <= imc < 30:
    classificacao = "Sobrepeso"   
elif 30 <= imc < 35:
    classificacao = "Obesidade Grau I" 
elif 35 <= imc < 40:
    classificacao = "Obesidade Grau II (severa)" 
else:
    classificacao = "Obesidade Grau III (mórbida)"  

#Saída
print(f"Seu IMC é: {imc:.2f} {classificacao}")

