#!/usr/bin/env python3
'''
Extra credit python 2
'''
import sys

def IsValidPassword(password):
    '''
    Gets a password and asks a user to verify it checks for any 
    problems with it
    Args:
        password is the password to be checked if valid
    '''
    hasUpper = False
    hasLower = False
    hasDigit = False
    if len(password) < 8:
        return False
    for i in password:
        if i.islower():
            hasLower = True
        elif i.isupper():
            hasUpper = True
        elif i.isdigit():
            hasDigit = True
        else:
            pass
    if hasUpper and hasLower and hasDigit:
        return True

def get_input():
    i = True
    while i:
        password = input('Enter your password: ')
        reenter = input('Re-enter your password: ')
        if password == reenter:
            if IsValidPassword(password):
                if IsValidPassword(reenter):
                    print('That pair of passwords will work.')
                    exit(0)
                else:
                    print('That password didn\'t have the required properties.') 
            else:
                print('That password didn\'t have the required properties.')
        else:
            print('That password didn\'t have the required properties.')




# Main Function
def main():
    '''
    Test Function
    '''
    get_input()
    return

if __name__ == '__main__':
    #Call Main
    main()

    exit(0)
