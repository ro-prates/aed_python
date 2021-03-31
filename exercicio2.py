'''
- Leia a idade do usuário e classifique-o em:
- Criança – 0 a 12 anos
- Adolescente – 13 a 17 anos
- Adulto – acima de 18 anos
-Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida

2- Calcular a média de um aluno que cursou a disciplina de Programação I, a 
partir da leitura das notas M1, M2 e M3; passando por um cálculo da média 
aritmética. Após a média calculada, devemos anunciar se o aluno foi aprovado, 
reprovado ou pegou exame
- Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
- Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
- Se a média for maior do que 6.0, o aluno está aprovado
- Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for 
maior do que 6.0, está aprovado, senão; está reprovado
'''
#primeira parte
idade = int(input('digite a sua idade:\n'))

if idade < 0:
    print('idade invalida')
elif idade < 13:
    print('crianca')
elif idade < 18:
    print('adolescente')
else:
    print('adulto')

#segunda parte
m1 = int(input('digite a sua nota 1\n'))
m2 = int(input('digite a sua nota 2\n'))
m3 = int(input('digite a sua nota 3\n'))

media = (m1 + m2 + m3) / 3

if media <= 4:
    print('reprovado')
elif media <= 6:
    print('exame')
    nota_exame = float(input('digite a nota do exame:\n'))
    if nota_exame > 6:
        print('aprovado')
    else:
        print('reprovado')
elif media > 6:
    print('aprovado')