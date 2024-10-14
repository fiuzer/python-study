"""
  enumerate - numera iteráveis (indices)
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indices, nomes in enumerate(lista):
  print(indices, nomes)