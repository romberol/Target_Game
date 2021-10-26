"""
Target game. You're supposed to find words among letters"
"""
from typing import List
import random

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    >>> 1==1
    True
    """
    letters = [l for l in 'abcdefghijklmnopqrstuvwxyz']
    grid = [[], [], []]
    for i in range(3):
        for j in range(3):
            grid[i].append(random.choice(letters).capitalize())
            int(j)
    for i in grid:
        print(i)
    return grid


def get_words(file_name, letters) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    >>> 1==1
    True
    """
    with open(file_name, encoding = 'utf-8') as file:
        words = [line.lower().strip() for line in file if len(line.strip())>3]
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
    return res

def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    >>> 1==1
    Truew
    """
    user_input = input().lower().split()
    return user_input

def get_pure_user_words(user_words, letters, words_from_dict):
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    >>> 1==1
    True
    """
    low_letters = []
    for row in letters:
        for letter in row:
            low_letters.append(letter.lower())
    pure_words = []
    for word in user_words:
        if word not in words_from_dict:
            if all(map(lambda x: not x.isdigit(), word)) and len(word)>3:
                if all(letter in low_letters and word.count(letter) <= low_letters.count(letter) for letter in word):
                    pure_words.append(word)
    return pure_words


def results():
    """
    Full game
    >>> 1==1
    Ture
    """
    grid = generate_grid()
    user_words = get_user_words()
    dict_words = get_words("en.txt", grid)
    print(user_words)

    pure_words = get_pure_user_words(user_words, grid, dict_words)
    print(pure_words)
    score = 0
    for word in user_words:
        if word in dict_words:
            score+=1
            del dict_words[dict_words.index(word)]
    with open("result.txt", "w") as file:
        file.write(score)
        file.write("\n")
        for word in dict_words:
            file.write(word+" ")
        file.write("\n")
        for word in pure_words:
            file.write(word+" ")
