# (c) AzureTecDevs 2024

# Main Libraries
import os
import sys
import term
import termcolor as color
import time
import random
import bash
import py

# Grey text
def g(txt):
	return color.colored(txt, 'dark_grey')

# Python3 shell
def py():
	print(f'(c) AzureTecDevs & Python Foundation\n{g("Type quit() to quit.")}')
	while True:
		ps = input(color.colored('>>> ', 'blue'))
		if ps == 'exit()' or ps == 'quit()':
			break
		else:
			exec(ps)