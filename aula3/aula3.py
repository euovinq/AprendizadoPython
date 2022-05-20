import math

import datetime

nome = 'Vinícius'
idade = 32
altura = 1.73
peso = 85
ano_atual = 2022

print(f"""
{nome} tem {idade} anos, {altura} de altura e pesa {peso}.
O IMC de {nome} é {(peso/altura**2):.2f}.
{nome} nasceu em {ano_atual - idade}.
""")