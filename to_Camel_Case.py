# ---- PROGRAM START ----
from string import punctuation as pux

def camel_case(text):
    for char in pux:
        if char in text:
            text_list = text.split(char)
            
    return ''.join([text_list[0].lower()] + [word.title() for word in text_list[1:]])

def many_camel_case(list):
    ''' Taking any words from user and change it into an UpperCamelCase word '''
    many = [term.lower() for term in list]
    return ''.join([many[0].lower()] + [phrase.title() for phrase in many[1:]])

# ---- The program starts here ----
print('''
    Welcome to CamelCase maker.
    Please choose one of the menu below.
''')

choice = input(''' 
    1. Change words into a single camelCase word.
    2. Change a word with hyphen or underscore within into a single camelCase word.
    >  ''')

# ---- Decision phase ----
if choice == "1":
    word_count = int(input("How many words to convert?  "))
    word_list = []
    # ---- compiling user input ----
    while word_count > 0:
        word_input = input("Input the word?  ")
        word_list.append(word_input)
        word_count -= 1
    
    print(f"The word is {many_camel_case(word_list)}")

elif choice == "2":
    word_input = input("Insert the word here:  ")
    print(f"\nThe word is {camel_case(word_input)}")

else:
    # ---- If user choose anything but the number ----
    print("Please choose only the number.\n")

print('''
    Thank you for using this program.
    See you later.
''')

# ---- PROGRAM END ----