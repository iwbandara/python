def main():
  match_func()


def match_func():
    # Use of match command instead of if...elif...else conditional

    name = input('Wat is your name? ')

    match name:
        case 'Harry' | 'Hermione' | 'Ron':
            print('Gryffindor')
        case 'Draco':
            print('Slytherin')
        case _:
            print('Who?') 

main()
