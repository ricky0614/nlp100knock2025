file = 'popular-names.txt'

with open(file) as reader:
	texts = reader.readlines()
	texts_sort = sorted(texts, reverse = True, key = lambda x:int(x.split()[2]))
	for i in range(len(texts_sort)):
		print(texts_sort[i])
