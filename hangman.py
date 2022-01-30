from webbrowser import get

from sqlalchemy import false
from words import paises
import random


def get_word():
    secretWord = random.choice(paises)
    return secretWord.lower()


def replace_dot(guess,dotted_word,secretWord):
    index = 0
    for letter in secretWord:
        if letter == guess:
            dotted_list = list(dotted_word)
            dotted_list[index] = letter
            dotted_word = "".join(dotted_list)
        index += 1
    return dotted_word

def play(secretWord):
    tries = 6
    guessed_letters = []
    guessed_words = []

    dotted_word = '-' * len(secretWord)
    guessed = False
    print('Vamos jogar ao jogo da forca!')
    print(f'Tens {tries} tentativas para acertar')
    print(dotted_word)
    while not guessed and tries > 0:
        print('')
        guess = input('Que letra ou palavra queres tentar? ').lower()

        if len(guess) == len(secretWord) and guess.isalpha():
            if guess in guessed_words:
                print('Já tentaste essa palavra')
                print(dotted_word)
            elif guess != secretWord:
                print('Palavra errada.')
                tries -= 1
                print(dotted_word)
            else:
                print('Acertaste!!')
                guessed = True
        elif len(guess) > 1 and guess.isalpha():
            print('Por favor joga só uma letra de cada vez a não ser que queiras adivinhar a palavra inteira.')
        
        elif len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('Já tentaste essa letra e não correu bem.')
                print('Letras que já usaste:', guessed_letters)
                print(dotted_word)
            elif guess in secretWord:
                print('Escolha acertada')
                guessed_letters.append(guess)
                dotted_word = replace_dot(guess, dotted_word,secretWord)
                print(dotted_word)
                if '-' not in dotted_word:
                    guessed = True
            else:
                print('Letra errada')
                tries -= 1
                print(f'Tens mais {tries} tentativas')
                print(dotted_word)
        else:
            print('Essa jogada não é válida')
    if guessed:
        print('Descobriste a palavra secreta!!')
        print(secretWord)
    else:
        print('Esgotaste todas as tuas tentativas')
        print(f'A palavra era {secretWord}')


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

main()