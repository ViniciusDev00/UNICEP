idades = [25, 45, 18, 30, 22, 60, 52]

media = sum(idades) / len(idades)
print(f"A média de idades é: {media:.2f}")
print("Idades maiores que a média:")

for idade in idades:
    if idade > media:
        print(idade)