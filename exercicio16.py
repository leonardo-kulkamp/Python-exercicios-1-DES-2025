#Exercício 16 – Cálculo de Reajuste Salarial
#Crie um programa que calcule o reajuste de salário:

#Salários até R$ 2000,00: +15%
#De R$ 2000,01 a R$ 5000,00: +10%
#Acima de R$ 5000,00: +5%

salario = int(input("Digite o seu salario "))

if salario <= 2000:
    print("O seu reajuste de salario será de 15%")
elif salario >= 5000:
    print("O seu reajuste de salario será de 5%")
else:
    print("O seu reajuste de salario será de 10%")

#Finalizado