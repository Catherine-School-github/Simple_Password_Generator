import secrets
import string


def possible_characters(lowercase_letter_check, capital_letter_check, number_check, symbol_check):
    characters_used = []
    if (lowercase_letter_check == 'y'):
        characters_used += string.ascii_lowercase
    if (capital_letter_check == 'y'):
        characters_used += string.ascii_uppercase
    if (number_check == 'y'):
        characters_used += string.digits
    if (symbol_check == 'y'):
        characters_used += string.punctuation
    
    return characters_used


def creating_password(length, characters):

    new_password = ''
    for i in range (length):
        new_password += secrets.choice(characters)
    
    return new_password

    


print("Welcome to your password generator")

try:
    length = int(input("How many characters do you want your new password to be: "))

    while (length <= 0):
        length = int(input("Please enter a number more than 0 for your new password: "))

except ValueError:
    print("Only enter a whole number for the password length")
    print("Exiting program, please try again")
    exit()


lowercase_letter_check = input("Would you like lowercase letters in your password (Y/n): ").lower()
if (lowercase_letter_check == ''):
    lowercase_letter_check = 'y'

while (lowercase_letter_check != 'y' and lowercase_letter_check != 'n'):
    lowercase_letter_check = input("Would you like lowercase letters in your password (Y/n): ").lower()
  
    if (lowercase_letter_check == ''):
        lowercase_letter_check = 'y'

print(lowercase_letter_check)


capital_letter_check = input("Would you like capital letters in your password (Y/n): ").lower()

if (capital_letter_check == ''):
    capital_letter_check = 'y'

while (capital_letter_check != 'y' and capital_letter_check != 'n'):
    capital_letter_check = input("Would you like capital letters in your password (Y/n): ").lower()
  
    if (capital_letter_check == ''):
        capital_letter_check = 'y'

print(capital_letter_check)

number_check = input("Would you like numbers in your password (Y/n): ").lower()

if (number_check == ''):
    number_check = 'y'

while (number_check != 'y' and number_check != 'n'):
    capital_letter_check = input("Would you like numbers in your password (Y/n): ").lower()
  
    if (number_check == ''):
        number_check = 'y'

print(number_check)

symbol_check = input("Would you like symbols in your password (Y/n): ").lower()

if (symbol_check == ''):
    symbol_check = 'y'

while (symbol_check != 'y' and symbol_check != 'n'):
    symbol_check = input("Would you like symbols in your password (Y/n): ").lower()
  
    if (symbol_check == ''):
        symbol_check = 'y'

print(symbol_check)

characters = possible_characters(lowercase_letter_check, capital_letter_check, number_check, symbol_check)
password = creating_password(length, characters)

print("Your new password is: {} remember to keep it safe".format(password))
