'''
1- Ler dois números inteiros, executar e mostrar o resultado das seguintes 
operações: adição, subtração, multiplicação e divisão

2-Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, 
utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário 
deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta 
forma, será possível obter a distância percorrida com a fórmula 
DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a 
quantidade de litros de combustível utilizada na viagem, com a 
fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores 
da velocidade média, tempo gasto na viagem, a distância percorrida e a 
quantidade de litros utilizada na viagem
'''

#primeira parte
n1 = int(input('digite o valor 1:\n'))
n2 = int(input('digite o valor 2:\n'))
print('adicao:', n1+n2)
print('subtracao:', n1-n2)
print('multiplicacao:', n1*n2)
print('divisao:', n1/n2)

#segunda parte
tempo = float(input('informe o tempo gasto na viagem:\n'))
valocidade_media = float(input('informe a velocidade media:\n'))
distancia = tempo * valocidade_media
litros_usados = distancia / 12

print('velocidade media:', valocidade_media)
print('tempo gasto na viagem:', tempo)
print('distancia percorrida:', distancia)
print('quantidade de litros:', round(litros_usados, 1))