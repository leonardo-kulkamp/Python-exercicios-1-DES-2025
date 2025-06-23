# Uma empresa quer avaliar seus colaboradores com base em três metas atingidas.
# O programa deve calcular a média das três avaliações e exibir:

# Aprovado (>=7)
# Em treinamento (>=5 e <7)
# Reprovado (<5)

nota01 = int(input("Digite sua nota da primeira avaliaçao "))
nota02 = int(input("Digite sua nota da segunda avaliaçao "))
nota03 = int(input("Digite sua nota da terceira avaliaçao "))

media = nota01 + nota02 + nota03 / 3

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Em treinamento")
else:
    print("Reprovado")

#Finalizado