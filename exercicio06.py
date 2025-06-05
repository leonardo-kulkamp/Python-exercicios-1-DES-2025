# Bianca está programando o controle de acesso a uma plataforma que só funciona entre 9h e 21h.
# O programa deve receber a hora atual (formato 24h) e informar se o acesso é permitido.

hora_atual = int(input("Digite a hora atual "))
hora = hora_atual
if hora_atual <= 9:
    print("Acesso permitido")
elif hora_atual > 21:
    print("Acesso negado")
else:
    print("Acesso permitido")