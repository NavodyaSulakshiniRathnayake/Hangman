{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww12720\viewh7800\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import random \
\
# List of words for the Hangman game\
animals = ["dog", "cat", "zebra", "lion", "tiger", "snakes", "parrot", "turtle", "fish", "cow", "giraffe", "rat"]\
fruits = ["apple", "banana", "lemon", "strawberry", "mango", "kiwi", "pineapple"]\
countries = ["Lebanon", "Egypt", "Germany", "Brazil", "Canada", "Australia", "France"]\
\
def welcome_message():\
    print('''Welcome to Hangman game!\
You should guess the name of a fruit, a movie, or a country to save the man.\
Let's go!!!''')\
\
def choose_word():\
    type_word = input("Which one do you want to guess (animals/fruits/countries): ").lower()\
    while True:\
        if type_word == "fruits":\
            return random.choice(fruits)\
        elif type_word == "countries":\
            return random.choice(countries).lower()\
        elif type_word == "animals":\
            return random.choice(animals)\
        else:\
            print("Check your spelling and try again!")\
            type_word = input("Which one do you want to guess (animals/fruits/countries): ").lower()\
\
def display_hangman(wrong):\
    hangman_stages = [\
        """\
           ------\
           |    |\
           |    O\
           |   /|\\\\\
           |   / \\\\\
           -\
        """,\
        """\
           ------\
           |    |\
           |    O\
           |   /|\\\\\
           |   /\
           -\
        """,\
        """\
           ------\
           |    |\
           |    O\
           |   /|\\\\\
           |\
           -\
        """,\
        """\
           ------\
           |    |\
           |    O\
           |    |\
           |\
           -\
        """,\
        """\
           ------\
           |    |\
           |    O\
           |\
           |\
           -\
        """,\
        """\
           ------\
           |    |\
           |\
           |\
           |\
           -\
        """,\
        """\
           ------\
           |\
           |\
           |\
           |\
           -\
        """\
    ]\
    return hangman_stages[wrong]\
\
def get_guess(used):\
    guess = input("Enter your guess: ").lower()\
    while guess in used or len(guess) != 1 or not guess.isalpha():\
        print("--- Try again. You've already used this letter or it's invalid ---")\
        guess = input("Enter your guess: ").lower()\
    return guess\
\
def gameplay():\
    welcome_message()\
    word = choose_word()\
    wrong = 0\
    max_wrong = 6\
    used = []\
    so_far = "-" * len(word)\
\
    print(f"It is a word that has \{len(word)\} letters\\n")\
    \
    while wrong < max_wrong and so_far != word:\
        print(display_hangman(wrong))\
        print("Word so far: " + so_far)\
        print("Letters used: " + str(used))\
        \
        guess = get_guess(used)\
        used.append(guess)\
        \
        if guess in word:\
            print(f"--- True! \{guess\} is a letter of the word ---\\n")\
            new = "".join([guess if guess == word[i] else so_far[i] for i in range(len(word))])\
            so_far = new\
        else:\
            print("--- False! Try again! ---")\
            wrong += 1  # Increment wrong guesses\
            \
    if wrong == max_wrong:\
        print(display_hangman(wrong))\
        print(f"The word is \{word\}. You didn't save the man :( , YOU LOSE!")\
    else:\
        print(f"Correct! The word is \{word\}. You have saved the man :) , YOU WIN!")\
\
if __name__ == "__main__":\
    gameplay()}