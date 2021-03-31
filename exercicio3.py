'''
1- Ler 5 notas e informar a média

2- Imprimir a tabuada do número 3 (3 x 1 = 1 - 3 x 10 = 30)
'''

#primeira parte
soma = 0
for i in range(5):
    n = int(input(f'digite o numero {i+1}:\n'))
    soma += n
print('media:', soma / 5)

#segunda parte
for i in range(10):
    print(f'3 x {i+1} = {3*(i+1)}')