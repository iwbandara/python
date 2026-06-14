# Use of FOR loop to display values from 1 to 10

for i in range (1,10):
    print(i)

print("--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+")
# Use of FOR loop to display values from 1 to 10 with a step value of 2

for i in range (1,10,2):
    print(i)

# Use the for loop to iterate the items in a List

names = ['Saman', 'Kamal', 'Sameera']

for name in names:
    print(name) # displays on the name line by line

for name in names:
    print(name, end=' ') # display each name in one line separated with a space
