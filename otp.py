import random
import string

def ran_gen(size,chars= string.digits):
	 
	return ''.join(random.choice(chars) for x in range(size))
for g in range(10):
	print  (ran_gen(4))