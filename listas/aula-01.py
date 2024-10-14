"""
Exercício
Exiba os índices da lista
"""

lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista))

for nome in lista:
  print(indices[0], nome, type(nome))
  indices = indices[1:]