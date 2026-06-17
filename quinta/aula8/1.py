precos = {
    'maçã': 3.50,
    'banana': 2.00,
    'uva': 5.00
}

produto = input("Digite o nome do produto que deseja pesquisar: ").lower()

if produto in precos:
    print(f"O preço de {produto} é R$ {precos[produto]:.2f}")
else:
    print("Produto não encontrado.")