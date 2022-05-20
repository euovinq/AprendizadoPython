import random as rd

respostas = ['Sim',
             'Não',
             'Sim, não me faça uma pergunta idiota dessas',
             'Não, né?',
             'Claro que não,',
             'É ÓBVIO que sim',
             'Só vai',
             'CERTAMENTE que não !',
             'NUNCA',
             'Jamais!']

while True:

    texto = input('Qual a sua dúvida? digite "sair" para sair do app ').lower()

    if texto == 'sair':
        print('saindo...')
        break

    else:
        print(respostas[rd.randrange(0, len(respostas))])



