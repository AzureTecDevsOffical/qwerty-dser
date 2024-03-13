# (c) AzureTecDevs 2024

# Main Libraries
import os
import sys
import term
import termcolor as color
import time
import random

# Config
uname = 'bash'
env = 'local'
sys = 'lite-1.0'
cur = '|> '
uinp = f'{uname}:{env}@{sys}{cur}'
# Bash Interface
# @bash.bash
def bash(func):
	while True:
		try:
			func(input(uinp))
		except Exception as e:
			print(str(e))
			continue
def clr():
	os.system('clear')
def run(file):
	os.system(f'python3 {file}')