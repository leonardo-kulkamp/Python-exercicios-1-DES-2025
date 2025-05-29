# Isabela está desenvolvendo um aplicativo de corrida que calcula a velocidade média do usuário.
# O programa deve receber a distância percorrida e o tempo gasto, calcular a velocidade e indicar se foi 
# lenta (<5 km/h), moderada (5 a 10 km/h) ou rápida (>10 km/h).
distanciapercorrida = int(input("Digite a distancia percorrida "))
tempogasto = int(input("Digite o tempo gasto "))
if distanciapercorrida / tempogasto < 5:
    print("Velocidade lenta")
elif distanciapercorrida / tempogasto >= 5:
    print("Velocidade moderada")
else:
    print("Velocidade rapida")

