#!/usr/bin/env python3

from random import choice, randint
from math import floor

samohlasky = "aeiouy"
souhlasky = "qwrtzplkjhgfdsxcvbnm"
all_chars = samohlasky + souhlasky

pslov = int(input("počet slov  > "))
filename = input("jméno souboru  > ")

samohlasky_gen = lambda : choice(samohlasky)
souhlasky_gen = lambda :  choice(souhlasky)
 

def generate_word(length:int):
    word = choice(all_chars)
    if word in samohlasky:
        char_now = souhlasky
    else:
        char_now = samohlasky
    switch_char = lambda : samohlasky if char_now == souhlasky else souhlasky

    for _ in range(length-1):
        word += choice(char_now)
        char_now=switch_char()
    return word

def trim_words(words:list):
    result = " ".join(words)
    num_breaks = floor(len(result)/60)
    for num_break in range(1,num_breaks+1):
        for indx,val in enumerate(result):
            if val == " " and indx >= 60*num_break:
                result = result[:indx] + "\n" + result[indx+1:]
                break
    return result 
    

slova = [generate_word(randint(3,10)) for _ in range(pslov) ]
slova = trim_words(slova)

if ".txt" in filename:
    with open(filename,"w") as f:
        f.write(slova)

else:
    with open(f"{filename}.txt","w") as f:
        f.write(slova)