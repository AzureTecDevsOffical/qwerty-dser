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
import sh
import webservice as web

# Clear screen
bash.clr()

# Grey text
def g(txt):
	return color.colored(txt, 'dark_grey')

# Blue text
def bl(txt):
	return color.colored(txt, 'blue')

# Config
splitter = ' !!' # Split commands	Ex.: print !!123 !!abc
sdoc = splitter # DO NOT CHANGE
dser = 'https://raw.githubusercontent.com/AzureTecDevsOffical/qwerty-dser/main/' # Download server (MUST have 'def-1.0' directory) (Needs slash	Ex.: example.com/ NOT example.com)
help = f"""-------------------------Help-------------------------
Screen Library (s):
	s.out{sdoc}TXT
	{g('| Output TXT')}
	s.out.xy{sdoc}TXT{sdoc}X{sdoc}Y
	{g('| Output TXT at X,Y')}
	s.out.nl{sdoc}TXT
	{g('| Output TXT without newline')}
	s.pix.1{sdoc}X{sdoc}Y
	{g('| Turn on pixel at X,Y')}
	s.pix.0{sdoc}X{sdoc}Y
	{g('| Turn off pixel at X,Y')}
	s.clr
	{g('| Clear display')}
Math Library (m):
	m.eval{sdoc}EXPR
	{g('| Eval EXPR')}
	m.rand
	{g('| Random integer (0-999999)')}
	m.rand.range{sdoc}MIN{sdoc}MAX
	{g('| Random integer (MIN-MAX)')}
Code Library (c):
	Python (py):
		c.py.exec{sdoc}CODE
		{g('| Execute CODE')}
		c.py.shell
		{g('| Run python3 shell')}
		{g('| Librarys: bash, term, time, os, sys, random, termcolor')}
	Linux/Shell Script (sh):
		c.sh.exec{sdoc}CODE
		{g('| Execute CODE')}
		c.sh.shell
		{g('| Run linux shell')}
System (sys):
	Dangerous (sap):
		sys.sap.mod{sdoc}DISTRO
		{g('| Modify system to custom distro DISTRO')}
		{g('| Default distro: ') + bl('def-1.0')}"""

# Main shell
@bash.bash
def main(input):
	# Input splitting
	ibs = input.split(splitter)
	com = ibs[0].lower()
	arg = ibs[1:]
	if com == 's.out':
		print(arg[0])
	elif com == 's.out.xy':
		term.saveCursor()
		term.pos(arg[2], arg[1])
		term.write(arg[0])
		term.restoreCursor()
	elif com == 's.out.nl':
		term.write(arg[0])
	elif com == 's.pix.1':
		term.saveCursor()
		term.pos(arg[1], arg[0])
		term.write('■')
		term.restoreCursor()
	elif com == 's.pix.0':
		term.saveCursor()
		term.pos(arg[1], arg[0])
		term.write(' ')
		term.restoreCursor()
	elif com == 'm.eval':
		print(eval(arg[0]))
	elif com == 'm.rand':
		print(str(random.randint(0, 999999)))
	elif com == 'm.rand.range':
		print(str(random.randint(int(arg[0]), int(arg[1]))))
	elif com == 'c.py.exec':
		exec(arg[0])
	elif com == 'c.py.shell':
		py.py()
	elif com == 'c.sh.exec':
		os.system(arg[0])
	elif com == 'c.sh.shell':
		sh.sh()
	elif com == 'sys.sap.mod':
		web.download(f'{arg[0]}/main.py', f'{dser}{arg[0]}/main.py')
		web.download(f'{arg[0]}/bash.py', f'{dser}{arg[0]}/bash.py')
		web.download(f'{arg[0]}/sh.py', f'{dser}{arg[0]}/sh.py')
		web.download(f'{arg[0]}/webservice.py', f'{dser}{arg[0]}/webservice.py')
		web.download(f'{arg[0]}/py.py', f'{dser}{arg[0]}/py.py')
	elif com == 's.clr':
		bash.clr()
	elif com == 'help':
		print(help)