# Talita está simulando o custo de frete para sua loja virtual. O valor depende da distância:

# Até 50 km: R$ 5,00
# De 51 a 150 km: R$ 15,00
# Acima de 150 km: R$ 25,00

distancia = int(input("Digite a distancia em km "))

if distancia <= 50:
    print("O preço do frete saira a 5 reais.")
elif distancia <= 150:
    print("O preço do frete sera 15 reais")
else:
    print("O preço do frete saira a 25 reais")

#Finalizado
