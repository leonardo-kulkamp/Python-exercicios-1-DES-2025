def calculo_area_retangulo(base, altura):
 
  area = base * altura
  return area

base = int(input("Digite a base do retangulo: "))
altura = int(input("Digite a altura do retangulo: "))

area_retangulo = calculo_area_retangulo(base, altura)

print(f"A área do retângulo com base {base} e altura {altura} é: {area_retangulo}")