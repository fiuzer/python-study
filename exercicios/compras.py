"""
  Faça uma lista de compras com listas
  O usuário deve ter a possibilidade de inserir, apagar e listar
  valores da sua lista
  Não permita que o programa quebre com erros de indices inexistentes
  na lista.
"""

compras = []
laco = True

while laco:
    try:
      while True:
        print("\nMenu:")
        print("1. Inserir item")
        print("2. Apagar item")
        print("3. Listar itens")
        print("4. Sair")
      
        opcao = int(input("Digite a opção: "))
        
        if opcao == 1:
          item = input("Digite o nome do item: ")
          compras.append(item)
          print(f'{item} foi adicionado com sucesso! Sua lista: {compras}')
        elif opcao == 2:
          item = input('Digite o nome do item: ')
          if item in compras:
            try:
              compras.remove(item)
              print(f'{item} foi removido com sucesso! Sua lista: {compras}')
            except ValueError:
              print(f'O item {item} não foi encontrado na lista.')
        elif opcao == 3:
          print(f'Sua lista de compras: {compras}')
        elif opcao == 4:
          print('Programa encerrado.')
          break

    except ValueError:
      print('Opção inválida. Tente novamente.')
    laco = False
