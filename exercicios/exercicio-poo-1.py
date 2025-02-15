produto = {}
i = 0

while i < 5:
    nome = input('Insira o nome do produto: ')
    valor = float(input('Insita o valor do produto: '))

    produto[nome] = valor
    print(produto)
    i += 1

for nome, preco in produto.items():
    if preco > 50.0:
        print(f"{nome}: R$ {preco:.2f}")
    
