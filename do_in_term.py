""" Run this file in terminal
"""
import sys, random as wut
code_word = 'do'
eqline = lambda x: "=" * x
lne = eqline(50)
switch = lambda string: (string.lower(), string.upper())[wut.randint(1, 2) == 1]
initial_box = lambda phrase: print(lne + '\n' + str(phrase) + ':\n' + lne)
if sys.argv[1].lower() not in code_word:
    print("Usuage: python3.7 [filename] [codeword]")
else:
    initial_box('Text Changer')
    readme_lol = input("Enter phrases to switch:")
    print(eqline(100) + '\n' + ''.join([str(switch(char)) for char in readme_lol]))
