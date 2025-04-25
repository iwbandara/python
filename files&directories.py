
from pathlib import Path

# path = Path('Excersises/Files&Directories')

# Checks if the above mentioned directory exists or not. Returns a Boolean value

# print(path.exists()) 

# Creating a directory

path1 = Path('C:/Users/User/Desktop/HelloPython')

if path1.exists() == False: # Checks the mentioned directory for existance 
    path1.mkdir() # Creates the Directory named 'HelloPython' on Desktop
    print('Directory created successfully.')
else:
    print('Directory already exists.')
