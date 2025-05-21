while True: # Loops indefinitely until the user input is an integer
  try:
    x = int(input('What is x? '))
  except ValueError:
    print('x is not an integer.') # execute when the input is not an integer
  else:
    break # Breaks out of the loop when the use enter an integer

print(f'x is {x}')

# ========================================================

# Improve the cord with functions

def main():
  x = get_int()
  print(f'x is {x}')
  
def get_int():
  while True:
    try:
      x = int(input('What is x? '))
    except ValueError:
      print('x is not an integer')
    else:
      return x
  
main()        
