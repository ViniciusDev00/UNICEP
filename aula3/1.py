altura = float(input())
idade = int(input())
acompanhado = input().lower() == "sim"

if (altura >= 1.50 and idade >= 12) or (acompanhado and altura >= 1.30):
    print("Liberado")
else:
    print("Barrado")