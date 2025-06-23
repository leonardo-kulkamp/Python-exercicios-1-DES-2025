#Exercício 19 – Números em Ordem Crescente
#Peça três números e exiba-os em ordem crescente.

numero01 = float(input("Digite um numero "))
numero02 = float(input("Digite um numero "))
numero03 = float(input("Digite um numero "))

numeros = [numero01, numero02, numero03]

numeros.sort()
print("Em ordem crescente", numeros)

#Finalizado