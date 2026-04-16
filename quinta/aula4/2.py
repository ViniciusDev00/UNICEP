salario = float(input())

if salario > 1500:
    novo_salario = salario * 1.10
else:
    novo_salario = salario * 1.15

print(f"{novo_salario:.2f}")