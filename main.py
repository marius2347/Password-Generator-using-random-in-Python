# --- Password Generator ---

# modules
import random

# input and output text
print("--- Please enter your settings to generate a password ---")
inputTextUpperCase, inputTextLowerCase, inputTextNumbers, inputTextLength, inputTextSymbols = " ", "", "", "", ""
try:
    inputTextUpperCase = input("UpperCase letters (Yes / No): ")
    inputTextLowerCase = input("LowerCase letters (Yes / No): ")
    inputTextNumbers = input("Numbers (Yes / No): ")
    inputTextSymbols = input("Symbols (Yes / No): ")
    inputTextLength = int(input("Length of the password: "))
except:
    print("Something went wrong from input values, try again!")

# lists
upperCase = [
    # Uppercase Alphabets
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X',
    'Y', 'Z']

lowerCase = [
    # Lowercase Alphabets
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x',
    'y', 'z',
]

Numbers = [
    # Numbers
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

Symbols = [
    # Symbols
    '~', ',', '.', ',', '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '=', '_', '+', '/', ';', ':'
]

# conditions
string = ""
condDict = {}
if inputTextUpperCase.lower() == "Yes".lower():
    condDict['upperCase'] = True
if inputTextLowerCase.lower() == "Yes".lower():
    condDict['lowerCase'] = True
if inputTextNumbers.lower() == "Yes".lower():
    condDict['Numbers'] = True
if inputTextSymbols.lower() == "Yes".lower():
    condDict['Symbols'] = True

# create list with conditions
liPassword = []
for key, value in condDict.items():
    if key == "upperCase":
        liPassword += upperCase
    if key == "lowerCase":
        liPassword += lowerCase
    if key == "Numbers":
        liPassword += Numbers
    if key == "Symbols":
        liPassword += Symbols

# generate password and checking for errors
generatedPass = ""
try:
    generatedPass = random.sample(liPassword, inputTextLength)
except:
    print("Something went wrong from generating, try again!")

# after is done print it
for x in generatedPass:
    string += x
print(string)
