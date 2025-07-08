
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
for dia in dias:
    print(dia)

#laço while

#2 exemplo

idade = int(input("Digite a sua idade (maior que 0): "))

while idade <= 0:
    print("Idade invalida")
    idade = int(input("Tente novamente "))
