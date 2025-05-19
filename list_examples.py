names = ['saman', 'kamal', 'perera', 'dehideniya', 'supun']
new_list = [] # define the new list name
for name in names:
    if len(name) >= 6: # checks for the length of the name
        continue # skips the value
    new_list.append(name.title()) # adds the name which is less than 6 to the new list after changing the first letter to Uppercase
print(new_list) # prints the newly created list
new_list.pop() # removes the last item from the list
new_list.remove('Saman') # removes the mentioned item from the list
