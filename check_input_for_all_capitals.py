# Author: Indika W Bandara
# Date: 2022-11-09
# Version: 1.0

# Checking input is only Capital letters

name=input('Enter your Name ?')

if name.isupper():
	print('Can accept.')
else:
	print('Can not accept. Please use CAPITAL letters.')
