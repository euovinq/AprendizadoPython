import random as rd

num_aleatorio = rd.randrange(1, 20)

chute = 0

while chute != num_aleatorio:
    chute = int(input('Chute um número: '))
    if chute == num_aleatorio:
        print(f'Parabéns, você acertou o número: {num_aleatorio}')
        break

    elif chute > num_aleatorio:
        print('Digite um número menor')


    elif chute < num_aleatorio:
        print('Digite um número maior')

