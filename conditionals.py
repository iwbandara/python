'''
> -> Greater than
>= -> greater than equal
< -> Less than
<= -> Less than equal
== -> Equals (comparing left & right values)
!= -> Not equal
'''

def main():

    x = int(input('What"s x? '))

    if is_even(x):
        print('Even')
    else:
        print('Odd')


def is_even(n): # Returns a boolean value as an output
    
    if n % 2 == 0:
        return True
    else:
        return False
    
main()
