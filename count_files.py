from pathlib import Path

path = Path()

count = 0

# checks all the files having .py extension & display the count & a list of files
for file in path.glob('*.py'):
    print(file)
    count += 1

print(f'Found {count} number of .py files.')
