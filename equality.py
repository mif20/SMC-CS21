# Maya Favela
# CS 21, Fall 2018

# This function tells the user whether the three user input integers are
# equal or not.

def equality():
    x = input('enter an integer:')
    y = input('enter an integer:')
    z = input('enter an integer:')

    if x != y or x != z or y != z:
        print('not equal')
    elif x == y == z:
        print('equal')
