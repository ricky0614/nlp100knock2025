import random

file = 'popular-names.txt'
file_name = 'output.txt'

with open(file) as reader:
	texts = reader.readlines()
	random.shuffle(texts)
	with open(file_name, mode = 'w') as writer:
		for i in range(len(texts)):
			writer.write(str(texts[i]))
