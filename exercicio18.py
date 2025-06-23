#Exercício 18 – Cálculo de Nota com Peso
#Receba duas notas e seus respectivos pesos. Calcule a média ponderada.
#Fórmula: (nota1 × peso1 + nota2 × peso2) / (peso1 + peso2)

nota01 = int(input("Digite a sua primeira nota "))
peso01 = int(input("Digite o peso da sua primeira nota "))

nota02 = int(input("Digite a sua segunda nota "))
peso02 = int(input("Digite o peso da sua segunda nota "))

media_ponderada = nota01 * peso01 + nota02 * peso02 / peso01 + peso02

print(f"A sua media ponderada é de {media_ponderada}")

#Finalizado
