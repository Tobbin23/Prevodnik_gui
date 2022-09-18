import random

def generuj_ip():
	return f"{random.randint(150,300)}.{random.randint(200,300)}.{random.randrange(10,100)}.{random.randrange(10,120)}"

