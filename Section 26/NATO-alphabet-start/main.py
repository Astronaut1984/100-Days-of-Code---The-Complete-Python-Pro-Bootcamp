import pandas as pd
from pprint import pprint

nato_alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
nato_alphabet = {row.letter: row.code for (_, row) in nato_alphabet_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ")
codes = [nato_alphabet[letter.upper()] for letter in user_word]
pprint(codes)
