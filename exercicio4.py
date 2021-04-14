'''
1- Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números 
inteiros e os armazene dentro de uma lista. Após a leitura, crie outra estrutura 
de repetição para somar todos os valores digitados

2- Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos, 
fazendo a leitura dos valores por meio de uma estrutura de repetição. Depois, 
crie uma nova estrutura de repetição para somar todas as notas e retornar a média

3- Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer 
e somar todos os elementos da matriz
'''

#primeira parte
lista = []

for i in range(5):
    lista.append(int(input()))

print(lista)

soma = 0
for i in lista:
    soma += i

print(f'a soma eh: {soma}')

#segunda parte
dicionario = {}

for i in range(3):
    nome = input(f'digite o nome do aluno {i+1}:\n')
    nota = int(input(f'digite a nota do aluno {i+1}:\n'))
    dicionario[nome] = nota

soma = 0
for chave in dicionario.keys():
    soma += dicionario[chave]

media = soma / len(dicionario)

print(f'a media eh: {media}')