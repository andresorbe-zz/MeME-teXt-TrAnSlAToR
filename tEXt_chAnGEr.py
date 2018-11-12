"""
This program switches the input to make the output a randomized version of uppercase and lowercase letters
Author: Andres Orbe <aeo2136@g.rit.edu>
Language: Python3
File: tEXt_chAnGEr.py
"""
import sys, random as wut
eqline = lambda x: "=" * x
switch = lambda string: (string.lower(), string.upper())[wut.randint(1, 2) == 1]
initial_box = lambda phrase: print(eqline(50) + '\n' + str(phrase) + ':\n' + eqline(50))
def just_do():
    initial_box('Text Changer')
    readme_lol = input("Enter phrases to switch:")
    print(eqline(100) + '\n' + ''.join([str(switch(char)) for char in readme_lol]))
just_do()
