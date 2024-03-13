# (c) AzureTecDevs 2024

# Main Libraries
import os
import sys
import term
import time
import random
import bash
import py

# Replace function 1
def rep1(a, b):
	return a
# Clear screen
bash.clr()

# Grey text
def g(txt):
	return rep1(txt, 'dark_grey')

# Blue text
def bl(txt):
	return rep1(txt, 'blue')

# Config (Note: bash's config is in bash.py')
splitter = ' !!' # Split commands	Ex.: print !!123 !!abc
sdoc = splitter # DO NOT CHANGE
help = f"""-------------------------Help-------------------------
Screen Library (s):
	s.out{sdoc}TXT
	{g('| Output TXT')}
	
	s.out.xy{sdoc}TXT{sdoc}X{sdoc}Y
	{g('| Output TXT at X,Y')}
	
	s.out.nl{sdoc}TXT
	{g('| Output TXT without newline')}

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
	c.py.exec{sdoc}CODE
	{g('| Execute CODE')}
	
	c.py.shell
	{g('| Run python3 shell')}
	{g('| Librarys: bash, term, time, os, sys, random, termcolor')}"""
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
	elif com == 's.clr':
		bash.clr()
	elif com == 'help':
		print(help)