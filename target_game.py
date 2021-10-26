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
    return res



def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    user_words = []
    user_input = input(">>> ")
    while user_input!="":
        # if len(user_input)>3 and all(map(lambda x: not x.isdigit(), user_input)):
        #     user_words.append(user_input)
        # else:
        #     print("Enter words with length more than 4 and word must not contain numbers")
        user_words.append(user_input)
        user_input = input(">>> ")
    return user_words
    


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    low_letters = []
    for row in letters:
        for letter in row:
            low_letters.append(letter.lower())
    pure_words = []
    for word in user_words:
        if word not in words_from_dict and all(map(lambda x: not x.isdigit(), word)) and len(word)>3:
            if all(letter in low_letters and word.count(letter) <= low_letters.count(letter) for letter in word):
                pure_words.append(word)
    return pure_words


def results():
    pass

# letters = generate_grid()
# words = get_words("E:/UCU/OP/ЛР 6/en.txt", letters)
# print(letters, words)
# user_words = get_user_words()
# print(get_pure_user_words(user_words, letters, words))