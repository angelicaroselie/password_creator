from string import ascii_lowercase, digits
from random import randint, choice

print()
print('This program creates a good random password for you.')


def create_password(characters: int, numbool: bool, extrabool: bool): #function to create password

    password = '' #generating the password here

    while True: #loop to create password
        
        if not numbool and not extrabool: #if both are false
            if len(password) == characters:
                break
            password += choice(ascii_lowercase) #adding random lowercase letter to password

        
        if numbool and not extrabool: #if numbool is true and extrabool is false
            if len(password) == characters:
                if any(c for c in password if c.islower()) and any(i.isdigit() for i in password): #checking if password has at least one lowercase letter and one number
                    break
            
                password = ''
        
            password += choice([choice(ascii_lowercase), choice(digits)]) #adding random lowercase letter or number to password

        
        if not numbool and extrabool: #if numbool is false and extrabool is true
            if len(password) == characters:
                if any(c for c in password if c.islower()) and any(c in '!?=+-()#' for c in password): #checking if password has at least one lowercase letter and one extra character
                    break
            
                password = ''
            password += choice([choice(ascii_lowercase), '!?=+-()#'[randint(0, len('!?=+-()#')-1)]]) #adding random lowercase letter or extra character to password

        
        if numbool and extrabool: #if both are true
            if len(password) == characters:
                if any(c for c in password if c.islower()) and any(i.isdigit() for i in password) and any(c in '!?=+-()#' for c in password): #checking if password has at least one lowercase letter, one number and one extra character
                    break
            
                password = ''  
            password += choice([choice(ascii_lowercase), choice(digits), '!?=+-()#'[randint(0, len('!?=+-()#')-1)]]) #adding random lowercase letter, number or extra character to password
        

    return password #returning the password




def main(): #main function

    characters = int(input('Give the length of the password (character amount as number): ')) #asking for length of password

    add_numbers = input('Do you want numbers in your password? (y/n): ') #asking if user wants numbers in password
    add_extra = input('Do you want extra characters in your password? (y/n): ') #asking if user wants extra characters in password

    print()

    #checking if user wants numbers in password
    if add_numbers == 'y' and add_extra == 'y':
        print(create_password(characters, True, True))
    #checking if user wants extra characters in password
    elif add_numbers == 'y' and add_extra == 'n':
        print(create_password(characters, True, False))
    #checking if user wants numbers and extra characters in password
    elif add_numbers == 'n' and add_extra == 'y':
        print(create_password(characters, False, True))
    #checking if user doesn't want numbers and extra characters in password
    elif add_numbers == 'n' and add_extra == 'n':
        print(create_password(characters, False, False))


    print()



if __name__ == "__main__": #running the file
    print('''
    DISCLAIMER: This program is not secure. It is just a fun project!!!
    ''')
    main()
