# (c) AzureTecDevs 2024

# Main Libraries
import os
import sys
import term
import termcolor as color
import time
import random

# Bash Interface
# @bash.bash
def bash(func):
	while True:
		try:
			func(input(color.colored('bash:local', 'green') + '|> '))
		except Exception as e:
			print(color.colored(str(e), 'red'))
			continue
def clr():
	os.system('clear')
def run(file):
	os.system(f'python3 {file}')