## CONFIG ##

UNBLANKABLE_FILEPATH = '''Add filepath here'''
RANDOMISE_QUOTE_ORDER = False
IGNORE_CAPITALIZATION = True
REVEAL_ON_GUESS = 3

## CODE ##

from tkinter import filedialog
from colorama import Fore, Style
import random

def load_file():

    filepath = filedialog.askopenfilename()
    if filepath:
        with open(UNBLANKABLE_FILEPATH, "r") as unblankable_file:
            unblankables = unblankable_file.read().split("\n")
                
        with open(filepath, "r") as quote_file:
            quotes = quote_file.read().split("\n")
                
        quotefill(quotes, unblankables)
    else:
        print(Fore.RED + "You must load a file" + Style.RESET_ALL)
        load_file()
        
def quotefill(quotes, unblankables):
    
    if RANDOMISE_QUOTE_ORDER:
        random.shuffle(quotes)
    
    for i, quote in enumerate(quotes):
    
        # randomly inserts blanks into the quote
        blanked_quote = quote.split(" ")
        if len(blanked_quote) > 1:
            blankable = []
            for j, word in enumerate(blanked_quote):
                if word.lower() not in unblankables:
                    blankable.append(j)
            random.shuffle(blankable)
            to_blank = []
            for k in range(0, random.randint(1, len(blankable) // 2)):
                to_blank.append(blankable[k])
            for elem in to_blank:
                blanked_quote[elem] = "_" * len(blanked_quote[elem])
            blanked_quote = " ".join(blanked_quote)
            
        print()
        print(Fore.MAGENTA + f"{i+1}/{len(quotes)}" + Style.RESET_ALL)
        
        ans = ""
        count = 1
        while ans != quote:
            if IGNORE_CAPITALIZATION and ans.lower() == quote.lower():
                break
            for chars in zip(quote, blanked_quote):
                if chars[1] == "_":
                    if count >= REVEAL_ON_GUESS:
                        print(Fore.YELLOW + chars[0] + Style.RESET_ALL, end="")
                    else:
                        print(Fore.YELLOW + chars[1] + Style.RESET_ALL, end="")
                else:
                    print(Fore.CYAN + chars[1] + Style.RESET_ALL, end="")
            print()
            ans = input()
            count += 1
        
while True:
    load_file()
    print(Fore.GREEN + "\nPress enter to exit. Input any value to play again." + Style.RESET_ALL)
    if not input():
        break
