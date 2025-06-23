# Gabriel está acompanhando o desempenho de dois cursos online que lançou: Python Básico e JavaScript Essencial.
# Ele quer saber qual curso teve mais avaliações no último mês.

# Crie um programa que receba o número de avaliações de cada curso e exiba qual teve mais.
# Caso as quantidades sejam iguais, exiba uma mensagem dizendo que houve empate.

curso01 = int(input("Digite quantas avaliaçoes teve o curso 01 "))
curso02 = int(input("Digite quantas avaliaçoes teve o curso 02 "))
if curso01 == curso02:
    print("Empate")
elif curso01 > curso02:
    print("O curso 01 e maior")
else:
    print("O curso 02 e maior")
    
#Finalizado