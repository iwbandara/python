while True: # Loops indefinitely until the user input is an integer
  try:
    x = int(input('What is x? '))
  except ValueError:
    print('x is not an integer.') # execute when the input is not an integer
  else:
    break # Breaks out of the loop when the use enter an integer

print(f'x is {x}')
