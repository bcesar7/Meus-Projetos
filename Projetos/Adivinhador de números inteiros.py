from random import randint
from time import sleep

print ('='*41)
print ('Este é um programa adivinhador de números')
print ('='*41)
print ('Tente adivinhar que número estou pensando...\n')

contador = 0
computador = randint(1, 10)

while True:
    jogador = int (input ('Escolha um número inteiro de 1 a 10: '))
    print('...')
    sleep(1)
    if jogador == computador:
        print('\nParabéns! Você acertou essa!!\n')
    elif jogador != computador:
        contador += 1
        print('\nQue pena HAHAHA, Você Errou!!!')
    if contador == 1:
        print('Você tem mais 2 chances.\n')
    if contador == 2:
        print('Você tem mais 1 chance.\n')
    if contador == 3:
        print ('='*12)    
        print('Game Over!!!')
        print ('='*12)
        break
        