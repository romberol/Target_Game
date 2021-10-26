from typing import List
import random

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    letters = [l for l in 'abcdefghijklmnopqrstuvwxyz']
    grid = [[], [], []]
    for i in range(3):
        for j in range(3):
            grid[i].append(random.choice(letters).capitalize())
    return grid


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(f, encoding = 'utf-8') as file:
        words = [line.strip() for line in file if len(line.strip())>3]
    low_letters = []
    for row in letters:
        for letter in row:
            low_letters.append(letter.lower())
    res = []
    for word in words:
        for letter in word:
            if letter not in low_letters or word.count(letter) > low_letters.count(letter):
                break
        else:
            if low_letters[4] in word:
                res.append(word)
    print(res, low_letters)



def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    user_words = []
    user_input = input(">>> ")
    while user_input!="":
        user_words.append(user_input)
        user_input = input(">>> ")
    return user_words
    


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass

get_words("E:/UCU/OP/ЛР 6/en.txt", generate_grid())
#print(get_user_words())