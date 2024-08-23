import random
from wordds import words
import string


def valid_words(words):
    word = random.choice(words)
    while "-" in word or '' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = valid_words(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    user_letter = input('guess a letter = ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in world
