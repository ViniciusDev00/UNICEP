def verifica_maioridade(idade):
    if idade >= 18:
        return "Maior de Idade"
    else:
        return "Menor de Idade"

minha_idade = int(input("Digite sua idade: "))
resultado = verifica_maioridade(minha_idade)
print(f"Status: {resultado}")