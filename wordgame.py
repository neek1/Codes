import random
import string
from spellchecker import SpellChecker
import itertools
spell = SpellChecker()  # loads default word frequency list



def pick_letters(l_list):
    #vowels = [['a'], ['e'], ['i'], ['o'], ['u'], ['y']]
    for letter in range(8):
        letter = [random.choice(string.ascii_lowercase)]
        l_list.append(letter)
        '''for vowel in vowels:
            if vowel not in letter:
            break'''
    return l_list       # This list has each letter nested as a seperate list
    

def check_letters(l_list, wrd):
    #print(l_list)
    #print(wrd)
    check_list = list(itertools.chain.from_iterable(l_list))    # Chamges l_list to 1 combined list
    used_letters = []
    res = None
     #Checks that the letters in word match the random letters provided
    for i in wrd:
        '''print(i)
        print(check_list)'''
        if i in check_list:
            #print(i)
            check_list.remove(i)
            used_letters.append(i)
            #print(used_letters)
            res = wrd 
        else:
            #print("Word contains unallowed letter")
            res =  None
            break
    return res

def check_word(wrd_list, wrd):
    if spell[wrd]:         #Checks if word is a valid english word
        if wrd not in wrd_list.keys():     #Checks if word already entered
            # Adds to word list dictionary wih score
            wrd_list[wrd] = len(wrd)
            print("Word added", wrd, ":", len(wrd))
            return wrd
        else:
            print("Word already entered")
            return False
    else:
        print("Not a valid word")
        return False
    
            
letter_list = []
word_list = {}
vowels = [['a'], ['e'], ['i'], ['o'], ['u'], ['y']]


while (True):
    pick_letters(letter_list)
    if (any(item in letter_list for item in vowels)):
        break
    else:
        letter_list.clear()
        #print("Letter List cleared no vowels")
        continue
print(letter_list)
    
while (True):
    word = input("Please enter a word: ")
    try:
        len(word) == 2
    except:
        print("Please enter a word with at least 3 letters.")
        continue
    check_letters(letter_list, word)
    #letters_confirmed = check_letters(letter_list, word)
    #print(letters_confirmed)
    if check_letters(letter_list, word) == None:
        print("Word contains unallowed letter")
        continue
    else:
        check_word(word_list, word)
        
    
    #print(word_list)
    #letter_list.clear()