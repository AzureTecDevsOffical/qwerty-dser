# (c) AzureTecDevs 2024

# Main Libraries
import os
import sys
import term
import termcolor as color
import time
import random
import bash

# Grey text
def g(txt):
	return color.colored(txt, 'dark_grey')

# Python3 shell
def sh():
	print(f'(c) AzureTecDevs & Linux\n{g("Type quit to quit.")}')
	while True:
		ps = input(color.colored('~ # ', 'yellow'))
		if ps == 'quit':
			break
		else:
			os.system(ps)