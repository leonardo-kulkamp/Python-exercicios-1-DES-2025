import random

input ("Pressione o enter para lançar o dado ")

resultado = random.randint(1,6)

print(F"O dado rolou: {resultado}")

if resultado == 6:
    print("Uau, Você tirou o numero maximo")
    
if resultado <= 2:
    print("Tente novamente")